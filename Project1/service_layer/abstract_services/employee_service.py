from abc import ABC, abstractmethod
from entities.Reimbursement import Reimbursement
from datetime import datetime, timezone
from entities.Employee import Employee



class serviceEmployee(ABC):

    @abstractmethod
    def service_login_employee(self, username : str, password : str)-> Employee:
        pass

    @abstractmethod
    def service_create_new_reimbursement(self, reimbursement:Reimbursement)-> Reimbursement:
        pass

    @abstractmethod
    def service_get_all_reimbursement_for_an_employee(self, employeeid : int)->list[Reimbursement]:
        pass

