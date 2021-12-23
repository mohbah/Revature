Feature: Manager can deny a reimbursement if he wants

  Scenario Outline:As an manager user I want to deny an reimbursement
    Given The managerr  is on the manager dashboard
    When the managerr enters reimbursement id <id> into the reimbursmeent id box
    When the managerr enters his commentt <comment> into the manager comment box
    When the managerr clicks on the new deny button
    Then The managerr should be redirected to the manager dashboard

    Examples:
      | id | comment   |
      | 9  | mycomment |


