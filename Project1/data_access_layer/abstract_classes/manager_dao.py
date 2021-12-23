from abc import ABC, abstractmethod
from entities.Reimbursement import Reimbursement
from entities.Manager import Manager



class managerDao(ABC):

    @abstractmethod
    def login_manager(self, username : str, password : str)-> Manager:
        pass

    @abstractmethod
    def resolve_reimbursement(reimbursement: Reimbursement)-> Reimbursement:
        pass

    @abstractmethod
    def get_all_pending_reimbursements(self)->list[Reimbursement]:
        pass

    @abstractmethod
    def get_all_approved_reimbursements(self)->list[Reimbursement]:
        pass

    @abstractmethod
    def get_all_reimbursements(self):
        pass



