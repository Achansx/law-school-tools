"""Data models for legal claims and counterarguments."""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Claim:
    """Represents a legal claim or argument extracted from a document.

    Attributes:
        text: The full text of the claim
        paragraph_index: Index of the paragraph where the claim was found
        context_before: Text preceding the claim (for context)
        context_after: Text following the claim (for context)
        counterargument: Generated counterargument (populated after API call)
        claim_type: Type of claim detected (e.g., 'numbered', 'assertion', 'conclusion')
        confidence: Confidence score of claim detection (0.0-1.0)
    """

    text: str
    paragraph_index: int
    context_before: str = ""
    context_after: str = ""
    counterargument: Optional[str] = None
    claim_type: str = "assertion"
    confidence: float = 1.0

    def __str__(self) -> str:
        """Return a readable string representation."""
        preview = self.text[:100] + "..." if len(self.text) > 100 else self.text
        return f"Claim[{self.claim_type}]: {preview}"

    def get_full_context(self) -> str:
        """Get the claim with its surrounding context."""
        parts = []
        if self.context_before:
            parts.append(f"[Context before]: {self.context_before}")
        parts.append(f"[Claim]: {self.text}")
        if self.context_after:
            parts.append(f"[Context after]: {self.context_after}")
        return "\n\n".join(parts)

    def has_counterargument(self) -> bool:
        """Check if a counterargument has been generated."""
        return self.counterargument is not None and len(self.counterargument.strip()) > 0


@dataclass
class CounterargumentResult:
    """Represents the result of counterargument generation.

    Attributes:
        claim: The original claim
        counterargument: Generated counterargument text
        citations: List of case citations included
        token_count: Number of tokens used for this generation
        success: Whether generation was successful
        error: Error message if generation failed
    """

    claim: Claim
    counterargument: Optional[str] = None
    citations: list[str] = field(default_factory=list)
    token_count: int = 0
    success: bool = True
    error: Optional[str] = None

    def __str__(self) -> str:
        """Return a readable string representation."""
        if self.success:
            return f"CounterargumentResult[Success]: {len(self.counterargument or '')} chars"
        else:
            return f"CounterargumentResult[Failed]: {self.error}"
