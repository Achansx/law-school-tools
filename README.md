# Legal Writing Tool

A Python command-line tool that uses Claude AI to generate counterarguments for legal research papers. Designed specifically for law students to strengthen their legal arguments by anticipating opposing viewpoints.

## Features

- **Intelligent Claim Detection**: Automatically identifies legal claims and arguments in Word documents
- **AI-Powered Counterarguments**: Uses Claude 3.5 Sonnet to generate thoughtful, well-reasoned counterarguments
- **Citation Support**: Includes relevant case citations and legal principles
- **Educational Focus**: Tailored for law students with detailed, analytical responses
- **Flexible Output**: Side-by-side table format for easy comparison
- **Cost Estimation**: Preview API costs before processing
- **Dry Run Mode**: Review detected claims without generating counterarguments
- **Robust Error Handling**: Automatic retry logic for API failures

## Installation

### Prerequisites

- Python 3.10 or higher
- Anthropic API key ([Get one here](https://console.anthropic.com/))

### Install Dependencies

```bash
# Clone the repository (if not already cloned)
git clone https://github.com/your-username/law-school-tools.git
cd law-school-tools

# Install required packages
pip install -r requirements.txt

# Or install in development mode
pip install -e .
```

### Set Up API Key

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your Anthropic API key:

```
ANTHROPIC_API_KEY=sk-your-key-here
```

## Quick Start

### Basic Usage

```bash
# Analyze a legal research paper
python -m legal_writing_tool --input my_paper.docx

# This will create: my_paper_counterarguments.docx
```

### Specify Output File

```bash
python -m legal_writing_tool --input my_paper.docx --output analysis.docx
```

### Advanced Claim Detection

```bash
# Use more aggressive claim detection
python -m legal_writing_tool --input my_paper.docx --claim-detection advanced
```

### Dry Run (Preview Claims)

```bash
# See what claims will be detected without calling the API
python -m legal_writing_tool --input my_paper.docx --dry-run
```

### Cost Estimation

```bash
# Estimate API cost before processing
python -m legal_writing_tool --input my_paper.docx --estimate-cost
```

## Command-Line Options

```
Required Arguments:
  -i, --input FILE           Path to input .docx file

Optional Arguments:
  -o, --output FILE          Path to output .docx file
  --api-key KEY              Anthropic API key (overrides env variable)
  --model MODEL              Claude model to use (default: claude-3-5-sonnet-20241022)
  --claim-detection MODE     Claim detection mode: simple, advanced (default: simple)
  --context-paragraphs N     Number of context paragraphs to include (default: 1)
  --format FORMAT            Output format: table, sequential (default: table)
  --dry-run                  Show detected claims without generating counterarguments
  --estimate-cost            Estimate API cost before processing
  --log-level LEVEL          Logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL
  -v, --verbose              Enable verbose output (DEBUG level)
  --version                  Show version and exit
```

## How It Works

1. **Document Parsing**: Reads your .docx file and extracts all paragraphs
2. **Claim Detection**: Identifies legal claims using pattern matching
   - Looks for assertion markers ("I argue that...", "The claim is...")
   - Detects legal reasoning patterns ("Therefore...", "It follows that...")
   - Identifies numbered arguments
3. **Counterargument Generation**: Sends each claim to Claude AI with:
   - The claim text
   - Surrounding context for better understanding
   - Instructions to generate substantive counterarguments with citations
4. **Document Creation**: Generates a new .docx file with:
   - Original claims in the left column
   - Generated counterarguments in the right column
   - Clean, professional formatting

## Configuration

### Environment Variables

Create a `.env` file or set these in your environment:

```bash
# Required
ANTHROPIC_API_KEY=sk-your-key-here

# Optional
CLAUDE_MODEL=claude-3-5-sonnet-20241022
MAX_RETRIES=3
RETRY_DELAY=2
LOG_LEVEL=INFO
API_DELAY=0.5
```

### Claim Detection Modes

**Simple Mode** (default):
- Pattern-based detection
- High precision, may miss some claims
- Faster processing

**Advanced Mode**:
- More aggressive detection
- Includes inferred claims based on legal terminology
- Higher recall, may have false positives

## Examples

### Example 1: Basic Analysis

```bash
python -m legal_writing_tool --input contract_law_paper.docx
```

Output: `contract_law_paper_counterarguments.docx`

### Example 2: Advanced Detection with Verbose Output

```bash
python -m legal_writing_tool \
  --input constitutional_analysis.docx \
  --claim-detection advanced \
  --verbose
```

### Example 3: Cost-Conscious Processing

```bash
# First, estimate the cost
python -m legal_writing_tool --input long_paper.docx --estimate-cost

# If acceptable, proceed
python -m legal_writing_tool --input long_paper.docx
```

### Example 4: Custom Model and Context

```bash
python -m legal_writing_tool \
  --input appellate_brief.docx \
  --model claude-3-5-haiku-20241022 \
  --context-paragraphs 2
```

## Output Format

The tool generates a Word document with:

- **Header**: Document metadata (source file, claims found, processing date)
- **Claim Tables**: Each claim in a separate table with:
  - Left column: Original claim text with type and confidence score
  - Right column: Generated counterarguments with citations
- **Footer**: Generation timestamp

Example output structure:

```
┌────────────────────────────────────────────────────────────┐
│              Legal Argument Analysis - Counterarguments     │
└────────────────────────────────────────────────────────────┘

Source Document: my_paper.docx
Total Claims Found: 5
Claims with Counterarguments: 5

Claim 1
┌──────────────────────┬──────────────────────────────────┐
│ Original Claim       │ Counterarguments                  │
├──────────────────────┼──────────────────────────────────┤
│ The defendant's...   │ 1. This argument overlooks...     │
│                      │ [See Smith v. Jones...]           │
│ [Type: assertion]    │                                   │
│ [Confidence: 85%]    │ 2. Courts have rejected...        │
└──────────────────────┴──────────────────────────────────┘
```

## Cost Considerations

The tool uses Claude 3.5 Sonnet by default, which provides high-quality counterarguments but has associated costs:

- **Claude 3.5 Sonnet**: ~$3 per 1M input tokens, ~$15 per 1M output tokens
- **Typical research paper**: 5-10 claims
- **Estimated cost per paper**: $0.10 - $0.50

**Tips to minimize costs:**
- Use `--dry-run` to verify claims before processing
- Use `--estimate-cost` to preview costs
- For longer papers, consider using `claude-3-5-haiku-20241022` (faster and cheaper)
- Use `simple` claim detection mode to avoid over-detection

## Troubleshooting

### "No claims found in document"

Try:
- Use `--claim-detection advanced` for more aggressive detection
- Ensure your document contains clear legal arguments
- Check that your .docx file is not corrupted

### "API key is required"

Ensure:
- You've created a `.env` file with your API key
- Or set `ANTHROPIC_API_KEY` environment variable
- Or pass `--api-key` on the command line

### "Input file must be a .docx file"

The tool only supports modern Word format (.docx). If you have an older .doc file:
- Open it in Word and save as .docx
- Or use online converters

### Rate Limit Errors

The tool includes automatic retry logic. If you consistently hit rate limits:
- Increase `--api-delay` (default: 0.5 seconds)
- Set `API_DELAY` in your `.env` file

## Development

### Project Structure

```
law-school-tools/
├── src/legal_writing_tool/
│   ├── core/              # Core functionality
│   │   ├── document_parser.py
│   │   ├── claim_analyzer.py
│   │   ├── counterargument_generator.py
│   │   └── document_writer.py
│   ├── models/            # Data models
│   │   ├── claim.py
│   │   └── document.py
│   ├── utils/             # Utilities
│   │   ├── logger.py
│   │   ├── validators.py
│   │   └── api_client.py
│   ├── cli.py             # CLI interface
│   ├── config.py          # Configuration
│   └── __main__.py        # Entry point
├── tests/                 # Test suite
├── requirements.txt
└── pyproject.toml
```

### Running Tests

```bash
# Install dev dependencies
pip install -r requirements.txt

# Run tests
pytest tests/

# With coverage
pytest --cov=legal_writing_tool tests/
```

### Code Quality

```bash
# Format code
black src/

# Lint
ruff check src/
```

## Limitations

- Only supports .docx files (not .doc)
- Requires internet connection for API calls
- Counterarguments are AI-generated and should be reviewed
- May not detect all claims, especially implicit ones
- Does not parse tables, footnotes, or complex formatting

## Future Enhancements

- [ ] Support for .pdf files
- [ ] Batch processing of multiple documents
- [ ] Custom prompt templates
- [ ] Jurisdiction-specific analysis
- [ ] Integration with case law databases
- [ ] Export to other formats (PDF, HTML)
- [ ] Web interface

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the documentation

## Acknowledgments

- Built with [Anthropic's Claude API](https://www.anthropic.com/claude)
- Uses [python-docx](https://python-docx.readthedocs.io/) for Word document handling
- Designed for law students and legal researchers

---

**Note**: This tool generates AI-powered counterarguments for educational purposes. Always critically evaluate the suggestions and conduct your own legal research. The tool is not a substitute for professional legal advice.
