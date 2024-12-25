Feature: Validate File Steps
    As a software developer
    I want to have a set of steps to validate files
    So that I can safely handle files during tests

    Scenario: Check temp file exists
        Given I create a temporary file "./temp.txt"
        Then the file "./temp.txt" exists
        And no error is raised

    Scenario: Check temp file is readable
        Given I create a temporary file "./readable-temp.txt"
        Then the file "./readable-temp.txt" is readable
        And no error is raised

    Scenario: Error raised if file does not exist
        When I try: Given the file "non-existent-file.json" exists
        Then the error message contains: Path 'non-existent-file.json' does not exist
