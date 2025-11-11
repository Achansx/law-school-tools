"""Claude API client with retry logic and error handling."""

import time
from typing import Optional

import anthropic
from anthropic import APIError, APIStatusError, RateLimitError

from .logger import get_logger

logger = get_logger(__name__)


class ClaudeAPIClient:
    """Wrapper for Claude API with retry logic and error handling."""

    def __init__(
        self,
        api_key: str,
        model: str = "claude-3-5-sonnet-20241022",
        max_retries: int = 3,
        retry_delay: float = 2.0,
    ):
        """Initialize the Claude API client.

        Args:
            api_key: Anthropic API key
            model: Claude model to use
            max_retries: Maximum number of retry attempts
            retry_delay: Base delay between retries (exponential backoff)
        """
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model
        self.max_retries = max_retries
        self.retry_delay = retry_delay

        logger.info(f"Initialized Claude API client with model: {model}")

    def generate_completion(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        max_tokens: int = 4096,
        temperature: float = 1.0,
    ) -> tuple[str, int]:
        """Generate a completion with retry logic.

        Args:
            prompt: User prompt
            system_prompt: System prompt (optional)
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature

        Returns:
            Tuple of (response_text, token_count)

        Raises:
            APIError: If all retries fail
        """
        for attempt in range(self.max_retries):
            try:
                logger.debug(f"API call attempt {attempt + 1}/{self.max_retries}")

                # Prepare message
                message_params = {
                    "model": self.model,
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                    "messages": [{"role": "user", "content": prompt}],
                }

                # Add system prompt if provided
                if system_prompt:
                    message_params["system"] = system_prompt

                # Make API call
                response = self.client.messages.create(**message_params)

                # Extract response text
                response_text = ""
                for block in response.content:
                    if block.type == "text":
                        response_text += block.text

                # Get token usage
                token_count = response.usage.input_tokens + response.usage.output_tokens

                logger.debug(f"API call successful. Tokens used: {token_count}")

                return response_text, token_count

            except RateLimitError as e:
                logger.warning(f"Rate limit hit on attempt {attempt + 1}: {e}")
                if attempt < self.max_retries - 1:
                    delay = self.retry_delay * (2**attempt)  # Exponential backoff
                    logger.info(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                else:
                    logger.error("Max retries reached for rate limit error")
                    raise

            except APIStatusError as e:
                logger.warning(f"API status error on attempt {attempt + 1}: {e}")
                if attempt < self.max_retries - 1 and e.status_code >= 500:
                    # Retry on server errors (5xx)
                    delay = self.retry_delay * (2**attempt)
                    logger.info(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                else:
                    logger.error(f"API error (status {e.status_code}): {e}")
                    raise

            except APIError as e:
                logger.error(f"API error on attempt {attempt + 1}: {e}")
                if attempt < self.max_retries - 1:
                    delay = self.retry_delay * (2**attempt)
                    logger.info(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                else:
                    logger.error("Max retries reached")
                    raise

            except Exception as e:
                logger.error(f"Unexpected error during API call: {e}")
                raise

        # This shouldn't be reached, but just in case
        raise APIError("Failed to generate completion after all retries")

    def estimate_tokens(self, text: str) -> int:
        """Estimate the number of tokens in a text.

        This is a rough estimate (4 characters per token) for planning purposes.

        Args:
            text: Text to estimate tokens for

        Returns:
            Estimated token count
        """
        return len(text) // 4

    def estimate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """Estimate the cost of an API call.

        Pricing as of implementation (check Anthropic's pricing page for current rates):
        - Claude 3.5 Sonnet: $3/MTok input, $15/MTok output
        - Claude 3.5 Haiku: $1/MTok input, $5/MTok output

        Args:
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens

        Returns:
            Estimated cost in USD
        """
        if "sonnet" in self.model.lower():
            input_cost = (input_tokens / 1_000_000) * 3.0
            output_cost = (output_tokens / 1_000_000) * 15.0
        elif "haiku" in self.model.lower():
            input_cost = (input_tokens / 1_000_000) * 1.0
            output_cost = (output_tokens / 1_000_000) * 5.0
        else:
            # Default to Sonnet pricing
            input_cost = (input_tokens / 1_000_000) * 3.0
            output_cost = (output_tokens / 1_000_000) * 15.0

        return input_cost + output_cost
