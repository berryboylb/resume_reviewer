# AI-Powered Resume Evaluator

## Project Overview

This project is an AI-powered resume evaluation system designed to analyze candidate resumes against job descriptions. It leverages OpenAI models to assess the relevance of resumes based on job postings, providing structured feedback, strengths, areas for improvement, and ATS (Applicant Tracking System) compatibility scores.

## Features

- **Resume Analysis**: Compares a resume against a job description.
- **Relevance Scoring**: Assigns a score to indicate how well a resume matches the job requirements.
- **Feedback Generation**: Highlights strengths, areas for improvement, and recommendations.
- **Performance Manager Agent**: A secondary AI agent that reviews AI-generated evaluations for bias, profanity, and accuracy.
- **Async Processing**: Utilizes asynchronous functions for efficient handling of multiple resume evaluations.

## Tech Stack

- **Backend**: Python (FastAPI, asyncio)
- **AI Integration**: OpenAI GPT-4o-mini
- **Tools**: WebSearchTool for additional research
- **Storage**: Document-based (e.g., MongoDB, PostgreSQL if needed)
- **Task Queue**: Celery (optional for scaling asynchronous tasks)

## Installation & Setup

### Prerequisites

- Python 3.12+
- `pipenv` (optional, for dependency management)
- OpenAI API Key

### Installation

```sh
# Clone the repository
git clone https://github.com/your-repo/ai-resume-evaluator.git
cd ai-resume-evaluator

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root directory with:

```
OPENAI_API_KEY=your_openai_api_key
```

## Usage

### Running the Resume Evaluator

```sh
python src/main.py
```

### Running Tests

```sh
pytest tests/
```

## Git Ignore Configuration

`.gitignore` should include:

```
# Virtual Environment
.venv/

# IDE & OS Specific Files
.vscode/
__pycache__/
.DS_Store

# Dependency Files
*.pyc
*.pyo

# Environment Variables
.env

# Logs
logs/
*.log
```

## Future Enhancements

- Add a web interface for resume uploads
- Support for multiple job description comparisons
- Improve AI-generated feedback quality
- Integrate an ATS compatibility analyzer

## License

This project is licensed under the MIT License.


