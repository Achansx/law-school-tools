"""Command-line interface for legal writing tool."""

import argparse
import sys
from pathlib import Path

from .config import Config
from .core import (
    ClaimAnalyzer,
    CounterargumentGenerator,
    DocumentParser,
    DocumentWriter,
)
from .utils import (
    ValidationError,
    get_logger,
    setup_logger,
    validate_api_key,
    validate_input_file,
    validate_output_path,
)
from .utils.api_client import ClaudeAPIClient


def create_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser.

    Returns:
        Configured ArgumentParser
    """
    parser = argparse.ArgumentParser(
        prog="legal-writing-tool",
        description="Generate counterarguments for legal research papers using Claude AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage
  legal-writing-tool --input my_paper.docx

  # Specify output file
  legal-writing-tool --input my_paper.docx --output analysis.docx

  # Use advanced claim detection
  legal-writing-tool --input my_paper.docx --claim-detection advanced

  # Dry run to see detected claims without calling API
  legal-writing-tool --input my_paper.docx --dry-run

  # Estimate cost before processing
  legal-writing-tool --input my_paper.docx --estimate-cost

Environment Variables:
  ANTHROPIC_API_KEY    Your Anthropic API key (required)
  CLAUDE_MODEL         Model to use (default: claude-3-5-sonnet-20241022)
  LOG_LEVEL            Logging level (default: INFO)

For more information, visit: https://github.com/your-repo/legal-writing-tool
        """,
    )

    # Required arguments
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        help="Path to input .docx file",
        metavar="FILE",
    )

    # Optional arguments
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Path to output .docx file (default: INPUT_counterarguments.docx)",
        metavar="FILE",
    )

    parser.add_argument(
        "--api-key",
        type=str,
        help="Anthropic API key (overrides ANTHROPIC_API_KEY env variable)",
        metavar="KEY",
    )

    parser.add_argument(
        "--model",
        type=str,
        default="claude-3-5-sonnet-20241022",
        help="Claude model to use (default: claude-3-5-sonnet-20241022)",
        metavar="MODEL",
    )

    parser.add_argument(
        "--claim-detection",
        type=str,
        choices=["simple", "advanced"],
        default="simple",
        help="Claim detection mode (default: simple)",
        metavar="MODE",
    )

    parser.add_argument(
        "--context-paragraphs",
        type=int,
        default=1,
        help="Number of paragraphs to include as context (default: 1)",
        metavar="N",
    )

    parser.add_argument(
        "--format",
        type=str,
        choices=["table", "sequential"],
        default="table",
        help="Output format (default: table)",
        metavar="FORMAT",
    )

    # Dry run and estimation
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show detected claims without generating counterarguments",
    )

    parser.add_argument(
        "--estimate-cost",
        action="store_true",
        help="Estimate API cost before processing",
    )

    # Logging
    parser.add_argument(
        "--log-level",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Logging level (default: INFO)",
        metavar="LEVEL",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output (equivalent to --log-level DEBUG)",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0",
    )

    return parser


def main() -> int:
    """Main entry point for CLI.

    Returns:
        Exit code (0 for success, 1 for error)
    """
    parser = create_parser()
    args = parser.parse_args()

    # Set up logging
    log_level = "DEBUG" if args.verbose else args.log_level
    logger = setup_logger(level=log_level)

    logger.info("Legal Writing Tool v0.1.0")
    logger.info("=" * 60)

    try:
        # Load configuration
        config = Config.from_env()

        # Update config from command-line arguments
        config.update_from_args(
            api_key=args.api_key or config.api_key,
            model=args.model,
            log_level=log_level,
            claim_detection_mode=args.claim_detection,
            context_paragraphs=args.context_paragraphs,
        )

        # Validate input file
        logger.info("Validating input file...")
        input_path = validate_input_file(args.input)
        logger.info(f"Input file: {input_path}")

        # Validate output path
        output_path = validate_output_path(args.output, input_path)
        logger.info(f"Output file: {output_path}")

        # Validate API key
        logger.info("Validating API key...")
        config.api_key = validate_api_key(config.api_key)

        # Validate configuration
        config_errors = config.validate()
        if config_errors:
            logger.error("Configuration errors:")
            for error in config_errors:
                logger.error(f"  - {error}")
            return 1

        logger.debug(f"Configuration: {config}")

        # Step 1: Parse document
        logger.info("=" * 60)
        logger.info("Step 1: Parsing document...")
        parser_obj = DocumentParser()
        document = parser_obj.parse(input_path)
        logger.info(f"✓ Parsed {document.metadata.total_paragraphs} paragraphs")

        # Step 2: Analyze claims
        logger.info("=" * 60)
        logger.info("Step 2: Analyzing claims...")
        analyzer = ClaimAnalyzer(context_paragraphs=config.context_paragraphs)
        document = analyzer.analyze(document, mode=config.claim_detection_mode)
        logger.info(f"✓ Found {len(document.claims)} claims")

        if not document.claims:
            logger.warning("No claims found in document. Try using --claim-detection advanced")
            return 1

        # Show detected claims
        logger.info("\nDetected claims:")
        for idx, claim in enumerate(document.claims, 1):
            logger.info(
                f"  {idx}. [{claim.claim_type}, confidence={claim.confidence:.1%}] "
                f"{claim.text[:80]}..."
            )

        # Dry run: stop here
        if args.dry_run:
            logger.info("=" * 60)
            logger.info("Dry run complete. Use without --dry-run to generate counterarguments.")
            return 0

        # Cost estimation
        if args.estimate_cost or log_level == "DEBUG":
            logger.info("=" * 60)
            logger.info("Estimating API cost...")

            # Create temporary API client for estimation
            temp_client = ClaudeAPIClient(
                api_key=config.api_key,
                model=config.model,
            )
            temp_generator = CounterargumentGenerator(temp_client)
            cost_estimate = temp_generator.estimate_cost_for_document(document)

            logger.info(f"  Number of claims: {cost_estimate['num_claims']}")
            logger.info(
                f"  Estimated input tokens: {cost_estimate['estimated_input_tokens']:,}"
            )
            logger.info(
                f"  Estimated output tokens: {cost_estimate['estimated_output_tokens']:,}"
            )
            logger.info(
                f"  Estimated total tokens: {cost_estimate['estimated_total_tokens']:,}"
            )
            logger.info(f"  Estimated cost: ${cost_estimate['estimated_cost_usd']:.4f}")

            if args.estimate_cost:
                logger.info("=" * 60)
                logger.info("Cost estimation complete. Use without --estimate-cost to proceed.")
                return 0

        # Step 3: Generate counterarguments
        logger.info("=" * 60)
        logger.info("Step 3: Generating counterarguments...")

        api_client = ClaudeAPIClient(
            api_key=config.api_key,
            model=config.model,
            max_retries=config.max_retries,
            retry_delay=config.retry_delay,
        )

        generator = CounterargumentGenerator(
            api_client=api_client,
            api_delay=config.api_delay,
            include_context=True,
        )

        document, results = generator.generate_for_document(document, show_progress=True)

        # Report results
        successful = sum(1 for r in results if r.success)
        failed = len(results) - successful

        logger.info(f"✓ Generated {successful} counterarguments")
        if failed > 0:
            logger.warning(f"⚠ {failed} failed")

        # Step 4: Write output
        logger.info("=" * 60)
        logger.info("Step 4: Writing output document...")

        writer = DocumentWriter()
        if args.format == "table":
            writer.write_table_format(document, output_path)
        else:
            writer.write_sequential_format(document, output_path)

        logger.info(f"✓ Output written to: {output_path}")

        # Summary
        logger.info("=" * 60)
        logger.info("✓ Processing complete!")
        logger.info(f"  Input:  {input_path}")
        logger.info(f"  Output: {output_path}")
        logger.info(f"  Claims processed: {successful}/{len(results)}")

        return 0

    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        return 1

    except KeyboardInterrupt:
        logger.warning("\nOperation cancelled by user")
        return 1

    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
