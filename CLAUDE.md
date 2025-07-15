# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Development Guidelines

This document contains critical information about working with this codebase.
Follow these guidelines precisely.

## Rules

1. Package Management
   - ONLY use uv, NEVER pip
   - Installation: `uv add package`
   - Upgrading: `uv add --dev package --upgrade-package package`
   - FORBIDDEN: `uv pip install`, `@latest` syntax

2. Code Quality
   - Type hints required for all code
   - Follow existing patterns exactly
   - Use Google style for docstring

3. Testing Requirements
   - Framework: `uv run --frozen pytest`
   - Coverage: test edge cases and errors
   - New features require tests
   - Bug fixes require regression tests

4. Git
   - Follow the Conventional Commits style on commit messages.(more detail: [@.cursorrules](.cursorrules))

## Code Formatting and Linting

1. Ruff
   - Format: `uv run --frozen ruff format .`
   - Check: `uv run --frozen ruff check .`
   - Fix: `uv run --frozen ruff check . --fix`
2. Pre-commit
   - Config: `.pre-commit-config.yaml`
   - Runs: on git commit
   - Tools: Ruff (Python)

## Development Setup Commands

```bash
# Initial setup
uv sync
uv run pre-commit install

# Run the main application
python main.py
uv run python main.py

# Run semantic search module
python src/semantic_search/main.py
uv run python src/semantic_search/main.py

# Testing
uv run --frozen pytest                    # Run all tests
uv run --frozen pytest tests/test_*.py    # Run specific test file
uv run --frozen pytest -v                 # Verbose output
```

## Docker Development

This project includes comprehensive Docker support for containerized development:

```bash
# Docker development workflow
uv sync                     # Generate uv.lock before building
./docker/build.sh          # Build development image
./docker/run.sh            # Run container interactively
./docker/run.sh python main.py  # Run specific command

# Docker Compose (simpler alternative)
docker compose build
docker compose up
```

## Project Architecture

This is a LangChain-based semantic search application with the following structure:

### Core Components
- **Main Package**: `src/semantic_search/` - Core semantic search functionality
- **Entry Points**: 
  - `src/semantic_search/main.py` - Semantic search demo using PyPDFLoader
- **Dependencies**: LangChain Community (PyPDFLoader), LangSmith, PyPDF

### Key Files
- `src/semantic_search/main.py:4` - PDF loading with PyPDFLoader
- `src/semantic_search/example_data/nke-10k-2023.pdf` - Sample Nike 10-K document for testing
- `compose.yml:15` - Docker Compose runs `python main.py` by default

### Development Environment
- Python 3.12+ required (pyproject.toml:7)
- Ruff linting with 100 character line length (pyproject.toml:25)
- Pre-commit hooks with uv-lock and ruff checks
- Docker support with multi-stage builds for development and production
