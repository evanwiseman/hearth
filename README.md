# Hearth

## Requirements

- Python 3.12
- UV

## Quick Start

```bash
git clone https://github.com/evanwiseman/hearth
cd hearth
make install
pre-commit install
```

## Usage

```bash
make run
```

## Development

| Command         | Description                        |
|-----------------|------------------------------------|
| `make install`  | Install dependencies               |
| `make run`      | Run the application                |
| `make format`   | Format code                        |
| `make lint`     | Lint with flake8                   |
| `make type`     | Type-check with mypy               |
| `make security` | Security scan with bandit          |
| `make test`     | Run tests with coverage            |
| `make check`    | Run all checks                     |
| `make clean`    | Remove caches and build artifacts  |