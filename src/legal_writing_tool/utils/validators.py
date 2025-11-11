"""Input validation utilities."""

import os
from pathlib import Path
from typing import Optional


class ValidationError(Exception):
    """Custom exception for validation errors."""

    pass


def validate_input_file(file_path: str) -> Path:
    """Validate that the input file exists and is a .docx file.

    Args:
        file_path: Path to the input file

    Returns:
        Path object for the validated file

    Raises:
        ValidationError: If the file doesn't exist or isn't a .docx file
    """
    path = Path(file_path)

    if not path.exists():
        raise ValidationError(f"Input file does not exist: {file_path}")

    if not path.is_file():
        raise ValidationError(f"Input path is not a file: {file_path}")

    if path.suffix.lower() != ".docx":
        raise ValidationError(
            f"Input file must be a .docx file, got: {path.suffix}. "
            "Note: .doc (older Word format) is not supported."
        )

    # Check if file is readable
    if not os.access(path, os.R_OK):
        raise ValidationError(f"Input file is not readable: {file_path}")

    return path


def validate_output_path(output_path: Optional[str], input_path: Path) -> Path:
    """Validate and generate output file path.

    Args:
        output_path: User-specified output path (optional)
        input_path: Input file path (used to generate default output name)

    Returns:
        Path object for the output file

    Raises:
        ValidationError: If the output path is invalid
    """
    if output_path:
        path = Path(output_path)

        # Check if parent directory exists
        if not path.parent.exists():
            raise ValidationError(
                f"Output directory does not exist: {path.parent}. "
                "Please create the directory first."
            )

        # Check if parent directory is writable
        if not os.access(path.parent, os.W_OK):
            raise ValidationError(f"Output directory is not writable: {path.parent}")

        # Ensure .docx extension
        if path.suffix.lower() != ".docx":
            path = path.with_suffix(".docx")

    else:
        # Generate default output name: input_counterarguments.docx
        stem = input_path.stem
        path = input_path.parent / f"{stem}_counterarguments.docx"

    # Check if file exists and warn (we'll overwrite)
    if path.exists():
        # This is just a check - the caller should handle the warning
        pass

    return path


def validate_api_key(api_key: Optional[str]) -> str:
    """Validate that an API key is provided and looks valid.

    Args:
        api_key: Anthropic API key

    Returns:
        Validated API key

    Raises:
        ValidationError: If the API key is missing or looks invalid
    """
    if not api_key:
        raise ValidationError(
            "Anthropic API key is required. "
            "Set the ANTHROPIC_API_KEY environment variable or provide it via --api-key."
        )

    api_key = api_key.strip()

    if not api_key.startswith("sk-"):
        raise ValidationError(
            "Invalid API key format. Anthropic API keys should start with 'sk-'."
        )

    if len(api_key) < 20:
        raise ValidationError("API key appears to be too short. Please check your key.")

    return api_key


def validate_claim_detection_mode(mode: str) -> str:
    """Validate the claim detection mode.

    Args:
        mode: Claim detection mode

    Returns:
        Validated mode

    Raises:
        ValidationError: If the mode is invalid
    """
    valid_modes = ["simple", "advanced"]

    if mode not in valid_modes:
        raise ValidationError(
            f"Invalid claim detection mode: {mode}. " f"Valid options: {', '.join(valid_modes)}"
        )

    return mode


def validate_model_name(model: str) -> str:
    """Validate the Claude model name.

    Args:
        model: Model name

    Returns:
        Validated model name

    Raises:
        ValidationError: If the model name looks invalid
    """
    # List of known valid models (as of implementation)
    known_models = [
        "claude-3-5-sonnet-20241022",
        "claude-3-5-haiku-20241022",
        "claude-3-opus-20240229",
        "claude-3-sonnet-20240229",
        "claude-3-haiku-20240307",
    ]

    if model not in known_models:
        # Warning but don't fail - new models may be released
        return model

    return model
