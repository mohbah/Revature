import datetime

class Reimbursement:

    def __init__(self, reimbursement_id: int, reimbursement_type_id: int, reimbursement_amount: int, date_submitted: datetime, date_resolved: datetime, reimbursement_status_id: int , reimbursement_employee_id: int, manager_comment: str ):
        self.reimbursement_id = reimbursement_id
        self.reimbursement_type_id = reimbursement_type_id
        self.reimbursement_amount = reimbursement_amount
        self.date_submitted = date_submitted
        self.date_resolved = date_resolved
        self.reimbursement_status_id = reimbursement_status_id
        self.reimbursement_employee_id = reimbursement_employee_id
        self.manager_comment = manager_comment




    def make_Reimbursement_dictionary(self):
        return {
            "reimbursementId": self.reimbursement_id,
            "reimbursementTypeId": self.reimbursement_type_id,
            "reimbursementAmount": self.reimbursement_amount,
            "dateSubmitted": self.date_submitted,
            "dateResolved": self.date_resolved,
            "reimbursementtatusId": self.reimbursement_status_id,
            "reimbursementEmployeeId": self.reimbursement_employee_id,
            "managerComment": self.manager_comment,


        }

