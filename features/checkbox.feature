Feature: Checkbox selection

  Scenario: Select first checkbox
    Given user is on checkbox page
    When user selects checkbox one
    Then checkbox one should be selected
  
  Scenario: Checkbox page shows two checkboxes
    Given user is on checkbox page
    Then two checkboxes should be visible
