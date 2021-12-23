from data_access_layer.Implimentations.employeedaoimpl import EmployeeDaoImpl
from entities.Employee import Employee
from entities.Reimbursement import Reimbursement

dao_employee = EmployeeDaoImpl()

employee= Employee(1, "moh", "bah")
Reim = Reimbursement(None, 1, 650, None, None, None, 1, None)

def test_employee_login_success():
    employee1 = dao_employee.login_employee(employee.employee_user_name, employee.employee_password)
    assert employee1.employee_id == 1

def test_create_new_reimbursement():
    Reim1= dao_employee.create_new_reimbursement(Reim)
    assert Reim1.reimbursement_id !=0

def test_get_all_reimbursements_for_employee():
    list= dao_employee.get_all_reimbursement_for_an_employee(1)
    assert len(list)>0


