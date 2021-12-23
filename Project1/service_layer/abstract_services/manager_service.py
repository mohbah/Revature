from abc import ABC, abstractmethod
from entities.Reimbursement import Reimbursement
from entities.Manager import Manager


class serviceManager(ABC):

    @abstractmethod
    def service_login_manager(self, username : str, password : str)-> Manager:
        pass

    @abstractmethod
    def service_resolve_reimbursement(self, reimbursement: Reimbursement)-> Reimbursement:
        pass

    @abstractmethod
    def service_get_all_pending_reimbursements(self)->list[Reimbursement]:
        pass

    @abstractmethod
    def service_get_all_approved_reimbursements(self)->list[Reimbursement]:
        pass

    @abstractmethod
    def service_get_all_reimbursements(self) -> list[Reimbursement]:
        pass
