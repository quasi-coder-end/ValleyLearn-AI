# ValleyLearn-AI

Valley Learn AI is a syllabus-focused learning assistant designed for JKBOSE students, starting with Class 10 Physics.

The project aims to provide accurate, exam-oriented answers strictly based on the JKBOSE curriculum, avoiding irrelevant or out-of-syllabus content.

## Features

- Interactive Q&A system for Class 10 Physics (multiple chapters)
- Keyword-based question matching with scoring system
- Answers formatted for easy reading
- Automatically loads all available JSON data files
- Strictly adheres to JKBOSE syllabus

## Project Structure

```
ValleyLearn-AI/
├── README.md
├── tutor.py                 # Main application script
└── data/
    └── class_10_light.json/  # Data directory
        └── data/
            └── class10_light.json  # JSON data file with Q&A pairs
```

## How It Works

### Data Loading
The application automatically scans the `data/class_10_light.json/data/` directory (and subdirectories) for all `.json` files and loads their Q&A data. This allows it to answer questions from multiple chapters without code changes.

### Question Matching Algorithm
1. **Preprocessing**: The user's question is converted to lowercase.
2. **Keyword Scoring**: For each Q&A pair, the system counts how many keywords appear as substrings in the question (allowing partial matches).
3. **Match Selection**: All answers with the highest keyword match count are collected.
4. **User Interaction**:
   - If one match: Display the answer directly.
   - If multiple matches: Show a numbered list of options (based on keywords) and let the user choose.
   - If no matches: Inform that the question is not covered.
5. **Answer Formatting**: Answers are displayed in a readable format, handling both simple strings and structured dictionaries.

### Example
- Question: "current"
- Keywords in data: ["electric", "current"] and ["si", "unit", "current"]
- Score: 1 each (keyword "current" appears in question)
- Result: Multiple options presented for user to choose

## Installation and Setup

1. Ensure Python 3.x is installed
2. Clone or download the repository
3. Navigate to the project directory
4. Run the application: `python tutor.py`

## Usage

1. Start the program: `python tutor.py`
2. Enter your question when prompted
3. The system will provide the most relevant answer(s) based on keyword matching:
   - If one answer matches best, it's shown directly
   - If multiple answers have equal relevance, you'll be asked to choose from a list
4. Type 'exit' to quit

## Data Format

Each JSON data file follows this structure:

```json
{
  "class": 10,
  "subject": "Physics",
  "chapter": "Chapter Name",
  "board": "JKBOSE",
  "qa": [
    {
      "keywords": ["keyword1", "keyword2"],
      "answer": {
        "definition": "Answer text..."
      }
    }
  ]
}
```

The system automatically combines Q&A data from all JSON files in the data directory.

## Contributing

Contributions are welcome! Please ensure that:
- All answers are based on the official JKBOSE syllabus
- Code changes maintain the keyword-based matching system
- New features are tested thoroughly

## License

This project is open-source. Please check the license file for details.