Feature: Validate Directory Steps
    As a developer
    I want to create and manipulate temporary directories during tests
    So that I can validate directory operations safely.

    Scenario: Check current directory exists
        Given the directory "./" exists
        Then no error is raised

    Scenario: Check parent directory exists
        Given the directory "../" exists
        Then no error is raised

    Scenario: Check home directory exists
        Given the directory "~" exists
        Then no error is raised
