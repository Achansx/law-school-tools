"""Data models for document representation."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .claim import Claim


@dataclass
class DocumentMetadata:
    """Metadata about the document.

    Attributes:
        file_path: Path to the original document
        total_paragraphs: Total number of paragraphs in document
        total_words: Approximate word count
        total_claims: Number of claims detected
        processing_timestamp: When the document was processed
    """

    file_path: Path
    total_paragraphs: int = 0
    total_words: int = 0
    total_claims: int = 0
    processing_timestamp: Optional[str] = None


@dataclass
class LegalDocument:
    """Represents a legal document with extracted claims.

    Attributes:
        metadata: Document metadata
        paragraphs: All paragraphs from the document
        claims: List of extracted claims
        output_path: Path where output document will be saved
    """

    metadata: DocumentMetadata
    paragraphs: list[str] = field(default_factory=list)
    claims: list[Claim] = field(default_factory=list)
    output_path: Optional[Path] = None

    def add_claim(self, claim: Claim) -> None:
        """Add a claim to the document."""
        self.claims.append(claim)
        self.metadata.total_claims = len(self.claims)

    def get_claims_with_counterarguments(self) -> list[Claim]:
        """Get only claims that have counterarguments generated."""
        return [claim for claim in self.claims if claim.has_counterargument()]

    def get_claims_without_counterarguments(self) -> list[Claim]:
        """Get claims that don't have counterarguments yet."""
        return [claim for claim in self.claims if not claim.has_counterargument()]

    def count_words(self) -> int:
        """Count total words in all paragraphs."""
        return sum(len(p.split()) for p in self.paragraphs)

    def __str__(self) -> str:
        """Return a readable string representation."""
        return (
            f"LegalDocument(file={self.metadata.file_path.name}, "
            f"paragraphs={self.metadata.total_paragraphs}, "
            f"claims={self.metadata.total_claims})"
        )
