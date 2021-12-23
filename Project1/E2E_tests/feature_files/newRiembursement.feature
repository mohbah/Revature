Feature: Employee Dashboard should support riembursement option

  Scenario Outline:As an employee user I want to creatt new reimbursement
    Given The employee user is on the new riembursement page
    When the employee entered the reimbursement amount <amount>
    When the employee have chosed the reimbursement type <type>
    When the employee clicks on the submmit new riembursement button
    Then The employee should recieve an Alert
    Examples:
      | amount | type |
      | 123    | Gas  |





