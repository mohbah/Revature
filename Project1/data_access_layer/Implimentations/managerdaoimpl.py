from data_access_layer.abstract_classes.manager_dao import managerDao

from entities.Reimbursement import Reimbursement
from entities.Manager import Manager
from Util.database_connection import connection


class managerDaoImpl(managerDao):
    def login_manager(self, username: str, password: str) -> Manager:
        try:
            sql = "select * from manager where manager_user_name = %s and manager_password = %s"
            cursor = connection.cursor()
            cursor.execute(sql, (username, password))
            manager_record = cursor.fetchone()
            manager = Manager(*manager_record)
            return manager
        except TypeError :
            return "Wrong UserName and/or PassWord!"

    def resolve_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = "update reimbursement set date_resolved= default, reimbursement_status_id= %s, manager_comment =%s where reimbursement_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, ( reimbursement.reimbursement_status_id, reimbursement.manager_comment, reimbursement.reimbursement_id))
        connection.commit()
        return reimbursement

    def get_all_pending_reimbursements(self) -> list[Reimbursement]:
        sql = "select * from reimbursement where  reimbursement_status_id= %s"
        cursor = connection.cursor()
        cursor.execute(sql, ['Pending'])
        Rem_records = cursor.fetchall()
        Rem_list = []
        for rem in Rem_records:
            Rem_list.append(Reimbursement(*rem))
        return Rem_list

    def get_all_approved_reimbursements(self) -> list[Reimbursement]:
        sql = "select * from reimbursement where reimbursement_status_id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, ['Approved'])
        Rem_records = cursor.fetchall()
        Rem_list = []
        for rem in Rem_records:
            Rem_list.append(Reimbursement(*rem))
        return Rem_list

    def get_all_reimbursements(self):
        sql = "select * from reimbursement"
        cursor = connection.cursor()
        cursor.execute(sql)
        Rem_records = cursor.fetchall()
        Rem_list = []
        for rem in Rem_records:
            Rem_list.append(Reimbursement(*rem))
        return Rem_list




