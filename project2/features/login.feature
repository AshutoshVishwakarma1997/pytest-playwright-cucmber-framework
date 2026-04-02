Feature: Login
  As a QA engineer
  I want to validate login behavior
  So that valid users can sign in and invalid attempts are rejected

  Scenario Outline: Validate login outcomes for different credential combinations
    Given the user opens the login page
    When the user attempts login for "<scenario>"
    Then the login result for "<scenario>" should be correct

    Examples:
      | scenario            |
      | happy_flow          |
      | invalid_credentials |
      | empty_username      |
      | empty_password      |
