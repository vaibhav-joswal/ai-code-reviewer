# 🤖 AI Code Reviewer Project

This is a project from my "21-Day Comeback Plan." It is an automated code review assistant.

## Week 1: Local Code Analyzer

This script (`reviewer.py`) is the engine of the reviewer. It automatically analyzes a Python file using `flake8` and generates a clean, human-readable report of any style errors.

### How to Use

1.  Clone this repository.
2.  Create a virtual environment: `python -m venv venv`
3.  Activate it: `source venv/bin/activate` (or `.\venv\Scripts\activate`)
4.  Install dependencies: `pip install -r requirements.txt`
5.  Run the analyzer on a test file: `python reviewer.py`