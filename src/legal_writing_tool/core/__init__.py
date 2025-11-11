"""Core functionality for legal writing tool."""

from .claim_analyzer import ClaimAnalyzer
from .counterargument_generator import CounterargumentGenerator
from .document_parser import DocumentParseError, DocumentParser
from .document_writer import DocumentWriter

__all__ = [
    "ClaimAnalyzer",
    "CounterargumentGenerator",
    "DocumentParseError",
    "DocumentParser",
    "DocumentWriter",
]
