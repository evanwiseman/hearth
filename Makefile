.PHONY: install run format lint type security test check clean help

install:  ## Install dependencies
	uv sync

run:  ## Run the application
	uv run hearth

format:  ## Format code with black, isort, and docformatter
	uv run black src tests
	uv run isort src tests
	uv run docformatter --in-place --recursive src tests

lint:  ## Lint with flake8
	uv run flake8 src tests

security:  ## Security scan src with bandit
	uv run bandit -r src

type:  ## Type-check with mypy
	uv run mypy src

test:  ## Run tests with pytest and coverage
	uv run pytest tests

check: format lint type security test  ## Run all checks

clean:  ## Remove caches and build artifacts
	find . -type d -name __pycache__ -not -path './.venv/*' -exec rm -rf {} +
	rm -rf .mypy_cache .pytest_cache .coverage

help:  ## Show available make targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-10s %s\n", $$1, $$2}'