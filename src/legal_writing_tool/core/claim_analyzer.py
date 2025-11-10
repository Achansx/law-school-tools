"""Claim analyzer for identifying legal claims and arguments in documents."""

import re
from typing import Optional

from ..models import Claim, LegalDocument
from ..utils import get_logger

logger = get_logger(__name__)


class ClaimAnalyzer:
    """Analyzer for detecting legal claims and arguments in documents."""

    # Pattern categories for claim detection
    ASSERTION_PATTERNS = [
        # Explicit argument markers
        r"I argue that",
        r"I contend that",
        r"I submit that",
        r"I propose that",
        r"My position is",
        r"The argument is",
        r"The claim is",
        # Thesis statements
        r"This (?:paper|essay|brief) argues",
        r"This (?:paper|essay|brief) contends",
        r"This (?:paper|essay|brief) demonstrates",
        r"This analysis shows",
        # Strong assertion markers
        r"It is (?:clear|evident|obvious) that",
        r"(?:Clearly|Evidently|Obviously),",
        r"There is no doubt that",
        r"It must be (?:concluded|recognized) that",
    ]

    LEGAL_CLAIM_PATTERNS = [
        # Legal reasoning
        r"(?:Therefore|Thus|Hence|Consequently),",
        r"It follows that",
        r"This (?:means|suggests|indicates|demonstrates) that",
        # Legal standards
        r"(?:under|according to) the (?:law|statute|rule|standard)",
        r"the court (?:should|must|ought to)",
        r"(?:applying|under) this (?:standard|test|rule)",
        # Comparative reasoning
        r"(?:Similarly|Likewise|By contrast|However),",
        r"(?:Unlike|Like) in",
        # Legal conclusions
        r"(?:ultimately|finally|in conclusion),",
    ]

    NUMBERED_PATTERNS = [
        # Roman numerals
        r"^[IVX]+\.",
        # Arabic numerals
        r"^\d+\.",
        # Lettered lists
        r"^[A-Z]\.",
        r"^\([a-z]\)",
    ]

    def __init__(self, context_paragraphs: int = 1):
        """Initialize the claim analyzer.

        Args:
            context_paragraphs: Number of paragraphs before/after to include as context
        """
        self.context_paragraphs = context_paragraphs
        logger.info(f"Initialized ClaimAnalyzer with context_paragraphs={context_paragraphs}")

    def analyze(self, document: LegalDocument, mode: str = "simple") -> LegalDocument:
        """Analyze a document to identify claims.

        Args:
            document: LegalDocument to analyze
            mode: Detection mode ('simple' or 'advanced')

        Returns:
            Updated LegalDocument with claims added
        """
        logger.info(f"Analyzing document for claims (mode={mode})")

        if mode == "simple":
            self._detect_simple_claims(document)
        elif mode == "advanced":
            self._detect_advanced_claims(document)
        else:
            logger.warning(f"Unknown mode '{mode}', defaulting to 'simple'")
            self._detect_simple_claims(document)

        logger.info(f"Found {len(document.claims)} claims")
        return document

    def _detect_simple_claims(self, document: LegalDocument) -> None:
        """Detect claims using pattern matching (simple mode).

        Args:
            document: LegalDocument to update with detected claims
        """
        for idx, paragraph in enumerate(document.paragraphs):
            # Skip very short paragraphs (likely not substantive claims)
            if len(paragraph.split()) < 10:
                continue

            claim_type = None
            confidence = 0.0

            # Check numbered patterns (highest priority)
            if self._matches_patterns(paragraph, self.NUMBERED_PATTERNS):
                claim_type = "numbered"
                confidence = 0.9

            # Check explicit assertion patterns
            elif self._matches_patterns(paragraph, self.ASSERTION_PATTERNS):
                claim_type = "assertion"
                confidence = 0.85

            # Check legal reasoning patterns
            elif self._matches_patterns(paragraph, self.LEGAL_CLAIM_PATTERNS):
                claim_type = "legal_reasoning"
                confidence = 0.7

            # If a pattern matched, create a claim
            if claim_type:
                claim = self._create_claim(
                    text=paragraph,
                    paragraph_index=idx,
                    document=document,
                    claim_type=claim_type,
                    confidence=confidence,
                )
                document.add_claim(claim)
                logger.debug(f"Detected {claim_type} claim at paragraph {idx}")

    def _detect_advanced_claims(self, document: LegalDocument) -> None:
        """Detect claims using advanced heuristics (advanced mode).

        This mode is more aggressive and may detect more claims.

        Args:
            document: LegalDocument to update with detected claims
        """
        # For now, use simple detection + additional heuristics
        self._detect_simple_claims(document)

        # Additional heuristics for advanced mode
        for idx, paragraph in enumerate(document.paragraphs):
            # Skip if already identified as a claim
            if any(c.paragraph_index == idx for c in document.claims):
                continue

            # Skip short paragraphs
            if len(paragraph.split()) < 15:
                continue

            # Heuristic: Long paragraphs with legal terminology
            legal_terms = [
                "court",
                "case",
                "statute",
                "law",
                "rule",
                "holding",
                "plaintiff",
                "defendant",
                "precedent",
                "doctrine",
            ]

            legal_term_count = sum(
                1 for term in legal_terms if term.lower() in paragraph.lower()
            )

            # If paragraph has multiple legal terms and makes assertions
            if legal_term_count >= 2 and (
                "should" in paragraph.lower()
                or "must" in paragraph.lower()
                or "cannot" in paragraph.lower()
            ):
                claim = self._create_claim(
                    text=paragraph,
                    paragraph_index=idx,
                    document=document,
                    claim_type="inferred",
                    confidence=0.6,
                )
                document.add_claim(claim)
                logger.debug(f"Detected inferred claim at paragraph {idx}")

    def _matches_patterns(self, text: str, patterns: list[str]) -> bool:
        """Check if text matches any of the given regex patterns.

        Args:
            text: Text to check
            patterns: List of regex patterns

        Returns:
            True if any pattern matches
        """
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return True
        return False

    def _create_claim(
        self,
        text: str,
        paragraph_index: int,
        document: LegalDocument,
        claim_type: str,
        confidence: float,
    ) -> Claim:
        """Create a Claim object with context.

        Args:
            text: Claim text
            paragraph_index: Index of paragraph containing claim
            document: Source document
            claim_type: Type of claim detected
            confidence: Confidence score

        Returns:
            Claim object with context
        """
        # Get context before
        context_before = ""
        start_idx = max(0, paragraph_index - self.context_paragraphs)
        if start_idx < paragraph_index:
            context_before = " ".join(document.paragraphs[start_idx:paragraph_index])

        # Get context after
        context_after = ""
        end_idx = min(len(document.paragraphs), paragraph_index + 1 + self.context_paragraphs)
        if end_idx > paragraph_index + 1:
            context_after = " ".join(document.paragraphs[paragraph_index + 1 : end_idx])

        return Claim(
            text=text,
            paragraph_index=paragraph_index,
            context_before=context_before,
            context_after=context_after,
            claim_type=claim_type,
            confidence=confidence,
        )

    def filter_claims_by_confidence(
        self, document: LegalDocument, min_confidence: float = 0.7
    ) -> list[Claim]:
        """Filter claims by minimum confidence threshold.

        Args:
            document: LegalDocument with claims
            min_confidence: Minimum confidence score

        Returns:
            List of claims meeting confidence threshold
        """
        filtered = [c for c in document.claims if c.confidence >= min_confidence]
        logger.info(
            f"Filtered {len(document.claims)} claims to {len(filtered)} "
            f"with min_confidence={min_confidence}"
        )
        return filtered
