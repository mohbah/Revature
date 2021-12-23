Feature: Login Page should support both Employee and Manager log-in

  Scenario Outline: As an manager user I want to log-in to my dashboard
    Given The manager user is on the log-in page
    When The manager user inputs <value> into the username bar
    When The manager user inputs <value1> into the password bar
    When the manager clicks on the log-in button
    Then The manager should be redirected to the Dashboard page with the title <title>
    Examples:
      | value | value1  | title                                             |
      | David | Beckham | Manager Reimbursement Dashboard |



