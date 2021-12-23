from data_access_layer.Implimentations.managerdaoimpl import managerDaoImpl
from entities.Manager import Manager
from entities.Reimbursement import Reimbursement
from service_layer.abstract_services.manager_service import serviceManager


class managerServiceImpl(serviceManager):

    def __init__(self, managerdao):
            self.managerdao: managerDaoImpl = managerdao

    def service_login_manager(self, username: str, password: str) -> Manager:
        return self.managerdao.login_manager(username, password)

    def service_resolve_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        return self.managerdao.resolve_reimbursement(reimbursement)

    def service_get_all_pending_reimbursements(self) -> list[Reimbursement]:
        return self.managerdao.get_all_pending_reimbursements()

    def service_get_all_approved_reimbursements(self) -> list[Reimbursement]:
        return self.managerdao.get_all_approved_reimbursements()

    def service_get_all_reimbursements(self) -> list[Reimbursement]:
        return self.managerdao.get_all_reimbursements()

