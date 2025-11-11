"""Counterargument generator using Claude API."""

import time
from typing import Optional

from tqdm import tqdm

from ..models import Claim, CounterargumentResult, LegalDocument
from ..utils import get_logger
from ..utils.api_client import ClaudeAPIClient

logger = get_logger(__name__)


class CounterargumentGenerator:
    """Generate counterarguments for legal claims using Claude AI."""

    SYSTEM_PROMPT = """You are an expert legal research assistant helping law students analyze arguments in their research papers.

Your task is to generate thoughtful, well-reasoned counterarguments to legal claims and arguments. For each claim:

1. Identify the core legal argument being made
2. Generate 2-3 substantive counterarguments that challenge the claim
3. Include relevant case citations, legal principles, or doctrinal considerations where appropriate
4. Present counterarguments in an educational, analytical style suitable for law students

Your counterarguments should:
- Be intellectually rigorous and substantive
- Consider multiple perspectives (doctrinal, policy, practical)
- Include specific legal reasoning, not just general disagreement
- Cite relevant cases, statutes, or legal principles when possible (you may use placeholder citations like "[See, e.g., Case Name v. Case Name]" if specific citations are not immediately available)
- Be formatted clearly with numbered points or paragraphs

Remember: The goal is to help law students think critically about their arguments and anticipate opposing views."""

    USER_PROMPT_TEMPLATE = """Please generate counterarguments for the following legal claim from a research paper:

CLAIM:
{claim_text}

{context_section}

Please provide 2-3 substantive counterarguments that challenge this claim. Include relevant legal citations, principles, or doctrinal considerations where appropriate.

Format your response as a clear, well-organized analysis suitable for inclusion in a legal research paper."""

    def __init__(
        self,
        api_client: ClaudeAPIClient,
        api_delay: float = 0.5,
        include_context: bool = True,
    ):
        """Initialize the counterargument generator.

        Args:
            api_client: Configured Claude API client
            api_delay: Delay between API calls (for rate limiting)
            include_context: Whether to include surrounding context in prompts
        """
        self.api_client = api_client
        self.api_delay = api_delay
        self.include_context = include_context

        logger.info("Initialized CounterargumentGenerator")

    def generate_for_document(
        self, document: LegalDocument, show_progress: bool = True
    ) -> tuple[LegalDocument, list[CounterargumentResult]]:
        """Generate counterarguments for all claims in a document.

        Args:
            document: LegalDocument with claims to process
            show_progress: Whether to show progress bar

        Returns:
            Tuple of (updated_document, results_list)
        """
        if not document.claims:
            logger.warning("No claims found in document")
            return document, []

        logger.info(f"Generating counterarguments for {len(document.claims)} claims")

        results = []
        total_tokens = 0

        # Set up progress bar
        iterator = (
            tqdm(document.claims, desc="Generating counterarguments", unit="claim")
            if show_progress
            else document.claims
        )

        for claim in iterator:
            try:
                result = self.generate_for_claim(claim)
                results.append(result)

                if result.success:
                    claim.counterargument = result.counterargument
                    total_tokens += result.token_count

                # Rate limiting
                if self.api_delay > 0:
                    time.sleep(self.api_delay)

            except Exception as e:
                logger.error(f"Failed to generate counterargument for claim: {e}")
                results.append(
                    CounterargumentResult(
                        claim=claim, success=False, error=str(e)
                    )
                )

        # Log summary
        successful = sum(1 for r in results if r.success)
        failed = len(results) - successful

        logger.info(
            f"Generation complete: {successful} successful, {failed} failed, "
            f"{total_tokens} total tokens"
        )

        # Estimate cost
        estimated_cost = self.api_client.estimate_cost(
            input_tokens=total_tokens // 2,  # Rough estimate
            output_tokens=total_tokens // 2,
        )
        logger.info(f"Estimated cost: ${estimated_cost:.4f}")

        return document, results

    def generate_for_claim(self, claim: Claim) -> CounterargumentResult:
        """Generate a counterargument for a single claim.

        Args:
            claim: Claim to generate counterargument for

        Returns:
            CounterargumentResult with generated counterargument
        """
        logger.debug(f"Generating counterargument for claim at paragraph {claim.paragraph_index}")

        try:
            # Build the prompt
            prompt = self._build_prompt(claim)

            # Call API
            response_text, token_count = self.api_client.generate_completion(
                prompt=prompt,
                system_prompt=self.SYSTEM_PROMPT,
                max_tokens=4096,
                temperature=1.0,
            )

            # Extract citations (simple pattern matching)
            citations = self._extract_citations(response_text)

            return CounterargumentResult(
                claim=claim,
                counterargument=response_text,
                citations=citations,
                token_count=token_count,
                success=True,
            )

        except Exception as e:
            logger.error(f"Error generating counterargument: {e}")
            return CounterargumentResult(
                claim=claim, success=False, error=str(e)
            )

    def _build_prompt(self, claim: Claim) -> str:
        """Build the prompt for generating a counterargument.

        Args:
            claim: Claim to build prompt for

        Returns:
            Formatted prompt string
        """
        # Add context if enabled
        context_section = ""
        if self.include_context:
            context_parts = []

            if claim.context_before:
                context_parts.append(f"PRECEDING CONTEXT:\n{claim.context_before}")

            if claim.context_after:
                context_parts.append(f"FOLLOWING CONTEXT:\n{claim.context_after}")

            if context_parts:
                context_section = "\n\n".join(context_parts)

        return self.USER_PROMPT_TEMPLATE.format(
            claim_text=claim.text,
            context_section=context_section,
        )

    def _extract_citations(self, text: str) -> list[str]:
        """Extract case citations from generated text.

        This is a simple pattern-based extraction.

        Args:
            text: Generated counterargument text

        Returns:
            List of extracted citations
        """
        import re

        # Pattern for case citations: "Case v. Case" or "[Case v. Case]"
        pattern = r"\[?([A-Z][a-zA-Z]+\s+v\.\s+[A-Z][a-zA-Z]+)\]?"
        citations = re.findall(pattern, text)

        return list(set(citations))  # Remove duplicates

    def estimate_cost_for_document(self, document: LegalDocument) -> dict:
        """Estimate the cost of processing a document.

        Args:
            document: LegalDocument to estimate cost for

        Returns:
            Dictionary with cost estimates
        """
        if not document.claims:
            return {
                "num_claims": 0,
                "estimated_input_tokens": 0,
                "estimated_output_tokens": 0,
                "estimated_cost_usd": 0.0,
            }

        # Estimate tokens per claim
        avg_claim_length = sum(len(c.text) for c in document.claims) / len(document.claims)
        avg_context_length = sum(
            len(c.context_before) + len(c.context_after) for c in document.claims
        ) / len(document.claims)

        # Rough estimate: system prompt + user prompt + claim + context
        system_tokens = self.api_client.estimate_tokens(self.SYSTEM_PROMPT)
        per_claim_input = system_tokens + self.api_client.estimate_tokens(
            self.USER_PROMPT_TEMPLATE
        )
        per_claim_input += int((avg_claim_length + avg_context_length) / 4)

        # Estimate output tokens (counterarguments are typically 500-1000 tokens)
        per_claim_output = 750

        total_input = per_claim_input * len(document.claims)
        total_output = per_claim_output * len(document.claims)

        cost = self.api_client.estimate_cost(total_input, total_output)

        return {
            "num_claims": len(document.claims),
            "estimated_input_tokens": total_input,
            "estimated_output_tokens": total_output,
            "estimated_total_tokens": total_input + total_output,
            "estimated_cost_usd": cost,
        }
