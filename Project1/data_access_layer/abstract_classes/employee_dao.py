from abc import ABC, abstractmethod
from entities import Reimbursement
from entities.Employee import Employee
import datetime


class EmployeeDao(ABC):

    @abstractmethod
    def login_employee(self, username : str, password : str)-> Employee:
        pass

    @abstractmethod
    def create_new_reimbursement(self, reimbursement: Reimbursement)-> Employee:
        pass

    @abstractmethod
    def get_all_reimbursement_for_an_employee(self, employeeid : int)->list[Reimbursement]:
        pass


