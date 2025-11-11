"""Legal Writing Tool - Generate counterarguments for legal research papers using Claude AI.

This package provides a command-line tool for law students to analyze their research
papers and generate thoughtful counterarguments using Claude AI.
"""

__version__ = "0.1.0"
__author__ = "Law School Tools"

from .config import Config
from .core import (
    ClaimAnalyzer,
    CounterargumentGenerator,
    DocumentParser,
    DocumentWriter,
)
from .models import Claim, CounterargumentResult, LegalDocument

__all__ = [
    "Config",
    "ClaimAnalyzer",
    "CounterargumentGenerator",
    "DocumentParser",
    "DocumentWriter",
    "Claim",
    "CounterargumentResult",
    "LegalDocument",
]
