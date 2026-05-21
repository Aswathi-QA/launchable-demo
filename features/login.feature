Feature: Login functionality

  Scenario: Valid login
    Given user is on login page
    When user enters valid username and password
    Then user should see secure area

  Scenario: Invalid login
    Given user is on login page
    When user enters invalid username and password
    Then user should see error message