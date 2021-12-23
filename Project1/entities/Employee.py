class Employee:

    def __init__(self, employee_id: int, employee_user_name: str,  employee_password: str):
        self.employee_id = employee_id
        self.employee_user_name = employee_user_name
        self.employee_password = employee_password

    def make_Employee_dictionary(self):
        return {
            "employeeID": self.employee_id,
            "employeeUserName": self.employee_user_name,
            "employeePassword": self.employee_password,
        }

    def __repr__(self):
        return "Employee ID: {}, UserName: {}, EmployeePassword: {}".format(self.employee_id, self.employee_user_name,self.employee_password)