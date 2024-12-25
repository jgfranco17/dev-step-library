Feature: Validate Directory Steps
    As a software developer
    I want to have a set of steps to validate directories
    So that I can safely handle directories during tests

    Scenario: Check current directory exists
        Given the directory "./" exists
        Then no error is raised

    Scenario: Check parent directory exists
        Given the directory "../" exists
        Then no error is raised

    Scenario: Check home directory exists
        Given the directory "~" exists
        Then no error is raised
