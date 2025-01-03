# List out available commands
_default:
	@just --list --unsorted

# Execute installation
setup:
	@echo "Setting up project..."
	poetry install
	poetry shell
	@echo "Project setup complete!"

# Run linters
lint:
    poetry run black .
    poetry run flake8 .
    poetry run isort .
    echo "Project workspace linted!"

# Run feature tests
behave *ARGS:
    poetry run behave tests/ {{ ARGS}}

# Clean unused files
clean:
	-@find ./ -name '*.pyc' -exec rm -f {} \;
	-@find ./ -name '__pycache__' -exec rm -rf {} \;
	-@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	-@find ./ -name '*~' -exec rm -f {} \;
	-@rm -rf .pytest_cache
	-@rm -rf .cache
	-@rm -rf .mypy_cache
	-@rm -rf build
	-@rm -rf dist
	-@rm -rf *.egg-info
	-@rm -rf htmlcov
	-@rm -rf .tox/
	-@rm -rf docs/_build
	-@rm -rf .venv
	@echo "Cleaned out unused files and directories."
