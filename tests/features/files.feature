Feature: Validate File Steps

    Scenario: Check temp file exists
        Given I create a temporary file "./temp.txt"
        Then file "./temp.txt" exists
        And no error is raised
