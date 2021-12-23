import datetime
from Util.database_connection import connection
from data_access_layer.abstract_classes.employee_dao import EmployeeDao

from entities.Reimbursement import Reimbursement
from entities.Employee import Employee


class EmployeeDaoImpl(EmployeeDao):

    def login_employee(self, usernam: str, password: str) -> Employee:
        try:
          sql = "select * from employee where employee_user_name = %s and employee_password = %s"
          cursor = connection.cursor()
          cursor.execute(sql, (usernam, password))
          employee_record = cursor.fetchone()
          employee = Employee(*employee_record)
          return employee
        except TypeError as e:
          return str(e)

    def create_new_reimbursement(self, riembursement: Reimbursement ) -> Reimbursement:

       sql = "insert into reimbursement values(default, %s, %s, default, null, default, %s, null ) returning reimbursement_id"
       cursor = connection.cursor()
       cursor.execute(sql, (riembursement.reimbursement_type_id, riembursement.reimbursement_amount,riembursement.reimbursement_employee_id))
       connection.commit()
       id=cursor.fetchone()[0]
       riembursement.reimbursement_id=id
       riembursement.manager_comment= None

       return riembursement


    def get_all_reimbursement_for_an_employee(self, employeeid: int) -> list[Reimbursement]:
      try:
        sql = "select * from reimbursement where  reimbursement_employee_id= %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employeeid])
        Rem_records = cursor.fetchall()
        Rem_list = []
        for rem in Rem_records:
            Rem_list.append(Reimbursement(*rem))
        return Rem_list
      except TypeError as e:
       return str(e)