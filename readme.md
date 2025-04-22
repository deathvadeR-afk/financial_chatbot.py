# Financial Chatbot

A Python-based chatbot that provides financial insights and analysis for Microsoft, Tesla, and Apple from 2022 to 2024. The application offers both a web interface and a command-line interface for user interaction.

## Features

- **Financial Data Analysis**: Access and analyze financial data for major tech companies
  - Total Revenue
  - Net Income
  - Total Assets
  - Total Liabilities
  - Cash Flow from Operating Activities (CFFOA)

- **Growth Metrics**: View year-over-year growth rates for:
  - Revenue Growth
  - Net Income Growth
  - Assets Growth
  - Liabilities Growth
  - CFFOA Growth

- **Multiple Interfaces**:
  - Web Interface (Built with Flask)
  - Command Line Interface (CLI)

- **Key Capabilities**:
  - Get total revenue for specific companies and years
  - Track net income changes
  - Compare revenue growth across companies
  - Access financial health assessments
  - Compare cash flow performance

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd financial_chatbot
```

2. Create and activate a virtual environment:
```bash
python -m venv my_venv
# On Windows:
my_venv\Scripts\activate
# On Unix or MacOS:
source my_venv/bin/activate
```

3. Install required dependencies:
```bash
pip install flask pandas numpy python-dateutil
```

## Usage

### Web Interface

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Use the chat interface to ask questions about financial data.

### Command Line Interface

1. Run the CLI version:
```bash
python cli.py
```

2. Type your questions and press Enter. Type 'exit' or 'quit' to end the session.

## Example Queries

- "What is the total revenue for Microsoft in 2024?"
- "How has Tesla's net income changed over the last year?"
- "Which company had the highest revenue growth in the most recent year?"
- "What is the financial health of Apple?"
- "Compare the cash flow performance of all companies"

## Project Structure

- `app.py` - Flask web application
- `chatbot.py` - Core chatbot logic and query processing
- `cli.py` - Command-line interface
- `financial_data.py` - Financial data and metrics
- `test_chatbot.py` - Test suite for chatbot functionality
- `templates/index.html` - Web interface template

## Testing

Run the test suite:
```bash
python test_chatbot.py
```

## Data Coverage

The chatbot includes financial data for:
- Companies: Microsoft, Tesla, and Apple
- Years: 2022, 2023, and 2024
- Metrics: Revenue, Net Income, Assets, Liabilities, Cash Flow

## Technical Details

- Built with Python 3.12+
- Uses Flask for web framework
- Implements clean separation of concerns:
  - Data layer (`financial_data.py`)
  - Business logic (`chatbot.py`)
  - Presentation layers (`app.py`, `cli.py`)
  - Web interface (`templates/index.html`)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
