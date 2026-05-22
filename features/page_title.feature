Feature: Page title validation

  Scenario: Verify login page title
    Given user is on login page
    Then the page title should be displayed
