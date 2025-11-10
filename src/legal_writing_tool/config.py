"""Configuration management for legal writing tool."""

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv


@dataclass
class Config:
    """Application configuration.

    Attributes:
        api_key: Anthropic API key
        model: Claude model to use
        max_retries: Maximum API retry attempts
        retry_delay: Base delay between retries
        log_level: Logging level
        api_delay: Delay between API calls
        context_paragraphs: Number of context paragraphs
        claim_detection_mode: Claim detection mode
    """

    api_key: str
    model: str = "claude-3-5-sonnet-20241022"
    max_retries: int = 3
    retry_delay: float = 2.0
    log_level: str = "INFO"
    api_delay: float = 0.5
    context_paragraphs: int = 1
    claim_detection_mode: str = "simple"

    @classmethod
    def from_env(cls, env_file: Optional[Path] = None) -> "Config":
        """Load configuration from environment variables.

        Args:
            env_file: Path to .env file (optional)

        Returns:
            Config object with values from environment
        """
        # Load .env file if specified or if it exists in current directory
        if env_file and env_file.exists():
            load_dotenv(env_file)
        else:
            load_dotenv()  # Load from default locations

        # Get API key (required)
        api_key = os.getenv("ANTHROPIC_API_KEY", "")

        # Get optional settings with defaults
        model = os.getenv("CLAUDE_MODEL", "claude-3-5-sonnet-20241022")
        max_retries = int(os.getenv("MAX_RETRIES", "3"))
        retry_delay = float(os.getenv("RETRY_DELAY", "2.0"))
        log_level = os.getenv("LOG_LEVEL", "INFO")
        api_delay = float(os.getenv("API_DELAY", "0.5"))

        return cls(
            api_key=api_key,
            model=model,
            max_retries=max_retries,
            retry_delay=retry_delay,
            log_level=log_level,
            api_delay=api_delay,
        )

    def update_from_args(self, **kwargs) -> None:
        """Update configuration from command-line arguments.

        Args:
            **kwargs: Keyword arguments to update
        """
        for key, value in kwargs.items():
            if value is not None and hasattr(self, key):
                setattr(self, key, value)

    def validate(self) -> list[str]:
        """Validate configuration.

        Returns:
            List of validation errors (empty if valid)
        """
        errors = []

        if not self.api_key:
            errors.append("API key is required (set ANTHROPIC_API_KEY environment variable)")

        if self.max_retries < 1:
            errors.append("max_retries must be at least 1")

        if self.retry_delay < 0:
            errors.append("retry_delay must be non-negative")

        if self.api_delay < 0:
            errors.append("api_delay must be non-negative")

        if self.context_paragraphs < 0:
            errors.append("context_paragraphs must be non-negative")

        valid_modes = ["simple", "advanced"]
        if self.claim_detection_mode not in valid_modes:
            errors.append(
                f"claim_detection_mode must be one of: {', '.join(valid_modes)}"
            )

        return errors

    def __str__(self) -> str:
        """Return string representation (hiding API key)."""
        masked_key = (
            f"{self.api_key[:7]}...{self.api_key[-4:]}" if self.api_key else "NOT_SET"
        )
        return (
            f"Config(api_key={masked_key}, model={self.model}, "
            f"max_retries={self.max_retries}, log_level={self.log_level})"
        )
