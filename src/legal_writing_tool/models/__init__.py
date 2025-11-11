"""Data models for legal writing tool."""

from .claim import Claim, CounterargumentResult
from .document import DocumentMetadata, LegalDocument

__all__ = [
    "Claim",
    "CounterargumentResult",
    "DocumentMetadata",
    "LegalDocument",
]
