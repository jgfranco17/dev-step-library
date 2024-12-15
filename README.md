# Developer Test Step Library

## Overview

This project is a Python package that leverages **Behavior-Driven Development (BDD)** principles
to ensure robust testing and clear specification of behaviors. The package provides various
utilities and tools, including reusable test steps. It encourages best practices in testing,
making it easier to maintain high-quality, well-tested code.

## Why BDD

### What is BDD?

Behavior-Driven Development (BDD) is an agile software development practice that emphasizes
collaboration between developers, testers, and business stakeholders. It helps ensure that the
software meets business goals and user expectations by writing tests in natural language.

### How BDD benefits this project

- **Clear Specifications**: BDD encourages writing tests in a format that clearly describes the
  behavior of the system. Using **Gherkin syntax**, we define `Given`/`When`/`Then` scenarios,
  making it easy for all stakeholders to understand how the system should behave.

- **Collaboration**: The natural language format allows testers, developers, and product owners
  to work together to ensure the software meets its requirements.
- **Automated Testing**: Tests are automated and can be run at any time to validate that the code
  still behaves as expected.

In this project, we use **Behave**, a Python BDD testing framework, to create reusable test steps
for various testing scenarios. These test steps are designed to be flexible and can be easily
extended or customized for specific use cases.

## Setting up the development environment

### Prerequisites

- Python 3.10+
- Poetry (for dependency management and packaging)

### Steps to set up

Clone the repository.

```shell
git clone https://github.com/your-username/dev-step-library.git
cd dev-step-library
```

Install Poetry (if you haven't already). There are multiple ways to do this, depending on your
system.

```shell
# Curl the install script
curl -sSL https://install.python-poetry.org | python3 -

# Homebrew
brew install poetry

# Global pip
pip install poetry
```

Install project dependencies and activate virtual environment

```shell
poetry install --with dev
poetry shell
```

### Testing

This project uses Behave for BDD-style testing. The tests are defined in Gherkin syntax using
the Given-When-Then structure.

#### Running tests

To run the tests, use Behave to run the feature tests suite.

```shell
# To run all Gherkin tests
poetry run behave tests/

# To run a specific testcase
poetry run behave path/to/your/feature/file.feature
```

Tests will automatically execute when a push or pull request is made to the repository.

#### Writing tests

To write your own tests, create new .feature files in the tests/features/ directory. Define your
scenarios in Gherkin format (Given, When, Then). While it is not required, it is recommended
to include the user story in the feature file if applicable.

Here is an example:

```gherkin
Feature: Validate Directory Steps
    As a developer
    I want to check that files exist
    So that I can run file-related tests safely

    Scenario: Check current directory exists
        Given directory "./sample.txt" exists
        Then no error is raised
```

## License

This project is licensed under the [BSD3 License](LICENSE).
