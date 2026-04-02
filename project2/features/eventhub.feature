Feature: EventHub booking
  As a QA engineer
  I want to validate event booking behavior
  So that a valid user can log in and complete a booking

  Scenario: User can book an event successfully
    Given the user opens the EventHub login page
    When the user logs in with valid EventHub credentials
    And the user selects the configured event
    And the user completes the booking
    Then the booking should be confirmed
