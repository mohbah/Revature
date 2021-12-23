from datetime import datetime

from data_access_layer.Implimentations.employeedaoimpl import EmployeeDaoImpl
from entities.Employee import Employee
from entities.Reimbursement import Reimbursement
from service_layer.abstract_services.employee_service import serviceEmployee


class employeeServiceImpl(serviceEmployee):

    def __init__(self,employeedao):
        self.employeedao: EmployeeDaoImpl = employeedao

    def service_login_employee(self, username: str, password: str) -> Employee:
        return self.employeedao.login_employee(username,password)

    def service_create_new_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        return self.employeedao.create_new_reimbursement(reimbursement)

    def service_get_all_reimbursement_for_an_employee(self, employeeid: int) -> list[Reimbursement]:
        return self.employeedao.get_all_reimbursement_for_an_employee(employeeid)