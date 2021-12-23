Feature: Login Page should support both Employee and Manager log-in

  Scenario Outline: As an employee user I want to log-in to my dashboard
    Given The employee user is on the log-in page
    When The employee user inputs <value> into the username bar
    When The employee user inputs <value1> into the password bar
    When the employee clicks on the log-in button
    Then The employee should be redirected to the Dashboard page with the title <title>
    Examples:
      | value | value1 | title                                             |
      | moh   | bah    | Expense Reimbursement System - Employee Dashboard |
      | John  | John   | Expense Reimbursement System - Employee Dashboard |




