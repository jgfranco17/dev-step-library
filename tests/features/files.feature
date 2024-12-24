Feature: Validate File Steps

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
        Then an error is raised
