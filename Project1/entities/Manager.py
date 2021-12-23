class Manager:

    def __init__(self, manager_id: int, manager_user_name: str, manager_password: str):
        self.manager_id = manager_id
        self.manager_user_name = manager_user_name
        self.manager_password = manager_password

    def make_Manager_dictionary(self):
        return {
            "managerId": self.manager_id,
            "managerUserName": self.manager_user_name,
            "managerPassword": self.manager_password,
        }

    def __repr__(self):
        return "Manager ID: {}, UserName: {}, ManagerPassword: {}".format(self.manager_id, self.manager_user_name,self.manager_password)