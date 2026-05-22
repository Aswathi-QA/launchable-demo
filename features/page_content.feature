Feature: Static page content validation

  Scenario: Verify heading text on home page
    Given user is on the home page
    Then the page heading should be displayed