from data_access_layer.Implimentations.managerdaoimpl import managerDaoImpl
from entities.Manager import Manager

dao_manager= managerDaoImpl()
manager = Manager(1, "David", "Beckham")

def test_manager_login_success():
    manager1 = dao_manager.login_manager(manager.manager_user_name, manager.manager_password)
    assert manager1

def test_resolve_reimbursement():
    pass

def test_get_all_pending_reimbursements():
    list = dao_manager.get_all_pending_reimbursements()
    assert len(list)> 0

def test_get_all_approved_reimbursements():
    list = dao_manager.get_all_approved_reimbursements()
    assert len(list)>0

def test_get_all_reimbursements():
    list = dao_manager.get_all_reimbursements()
    assert len(list)> 0