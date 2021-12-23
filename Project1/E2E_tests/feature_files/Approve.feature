Feature: Manager can approve a reimbursement if he wants

  Scenario Outline:As an manager user I want to approve an reimbursement
    Given The manager user is on the manager dashboard
    When the manager enter reimbursement id <id> into the reimbursmeent id box
    When the manager enters his comment <comment> into the manager comment box
    When the manager clicks on the new approve button
    Then The manager should be redirected to the manager dashboard

    Examples:
      | id | comment   |
      | 9  | mycomment |




