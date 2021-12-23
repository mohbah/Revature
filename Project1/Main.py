from flask import Flask, jsonify, request

import custom_exception
from data_access_layer.Implimentations.employeedaoimpl import EmployeeDaoImpl
from data_access_layer.Implimentations.managerdaoimpl import managerDaoImpl
from entities.Reimbursement import Reimbursement
from service_layer.implimentation_services.employee_service_impl import employeeServiceImpl
from service_layer.implimentation_services.manager_service_impl import managerServiceImpl
from flask_cors import CORS



app: Flask = Flask(__name__)
CORS(app)

employee_dao = EmployeeDaoImpl()
employee_service = employeeServiceImpl(employee_dao)

manager_dao = managerDaoImpl()
manager_service = managerServiceImpl(manager_dao)


@app.post("/employee")
def login_emloyee():
   try:
    data = request.get_json(force=True)
    username = data["username"],
    password = data["password"],
    employee_to_return =employee_service.service_login_employee(username, password)
    employee_as_dictionary = employee_to_return.make_Employee_dictionary()
    employee_as_json = jsonify(employee_as_dictionary)
    return employee_as_json
   except AttributeError:
       exception_dictionary = {"message": "Invalid usernam or password!"}
       exception_json = jsonify(exception_dictionary)
       return exception_json


@app.post("/manager")
def login_manager():
   try:
    data = request.get_json(force=True)
    username = data["username"],
    password = data["password"],
    manager_to_return = manager_service.service_login_manager(username, password)
    manager_as_dictionary = manager_to_return.make_Manager_dictionary()
    manager_as_json = jsonify(manager_as_dictionary)
    return manager_as_json
   except AttributeError :
       exception_dictionary = {"message": "Invalid usernam or password!"}
       exception_json = jsonify(exception_dictionary)
       return exception_json


@app.post("/reimbursement")
def create_new_reimbursment():

    reimbursement_data = request.get_json(force=True)
    new_reimbursement = Reimbursement(
        None,
        reimbursement_data["reimbursementTypeId"],
        reimbursement_data["reimbursementAmount"],
        None,
        None,
        reimbursement_data["reimbursementtatusId"],
        reimbursement_data["reimbursementEmployeeId"],
        None,
    )
    R_to_return = employee_service.service_create_new_reimbursement(new_reimbursement)
    R_as_dictionary= R_to_return.make_Reimbursement_dictionary()
    R_as_json = jsonify(R_as_dictionary)
    return R_as_json

@app.get("/employee/<id>")
def get_all_reimbursement_for_an_employee(id : str):
    try:

        reims_as_reims= employee_service.service_get_all_reimbursement_for_an_employee(int(id))
        reims_as_dictionary = []
        for reim in reims_as_reims:
            dictionary_reim= reim.make_Reimbursement_dictionary()
            reims_as_dictionary.append(dictionary_reim)
        return jsonify(reims_as_dictionary)
    except AttributeError:
        return "Wrong ID!"


@app.get("/allreim")
def get_all_reimbursements():
    try:
        reims_as_reims= manager_service.service_get_all_reimbursements()
        reims_as_dictionary = []
        for reim in reims_as_reims:
            dictionary_reim= reim.make_Reimbursement_dictionary()
            reims_as_dictionary.append(dictionary_reim)
        return jsonify(reims_as_dictionary)
    except AttributeError:
        return "Somethin wrong!"

@app.patch("/reimbursement")
def resolve_reimbursement():
    reimbursement_data = request.get_json(force=True)
    new_reimbursement = Reimbursement(
        reimbursement_data["reimbursementId"],
        None,
        None,
        None,
        None,
        reimbursement_data["reimbursementtatusId"],
        None,
        reimbursement_data["managerComment"],
    )
    R_to_return = manager_service.service_resolve_reimbursement(new_reimbursement)
    R_as_dictionary = R_to_return.make_Reimbursement_dictionary()
    R_as_json = jsonify(R_as_dictionary)
    return R_as_json


@app.get("/reimbursement/pending")
def get_all_pendings():
    reims_as_reims = manager_service.service_get_all_pending_reimbursements()
    reims_as_dictionary= []
    for reim in reims_as_reims:
        dictionary_reimbursement = reim.make_Reimbursement_dictionary()
        reims_as_dictionary.append(dictionary_reimbursement)
    return jsonify(reims_as_dictionary)


@app.get("/reimbursement/approved")
def get_all_approved():
    reims_as_reims = manager_service.service_get_all_approved_reimbursements()
    reims_as_dictionary = []
    for reim in reims_as_reims:
        dictionary_reimbursement = reim.make_Reimbursement_dictionary()
        reims_as_dictionary.append(dictionary_reimbursement)
    return jsonify(reims_as_dictionary)




app.run()