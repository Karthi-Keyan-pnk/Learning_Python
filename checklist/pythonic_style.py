class Employee:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


employees = [
    Employee("Karthi"),
    Employee("Arun"),
    Employee("Rahul")
]

for i in range(len(employees)):
    employee = employees[i]
    print(employee.get_name())


#######################################################

""" converting to pythonic style """

print("Pythonic style")
class Employee1:

    def __init__(self, name: str):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value

employees = Employee1("Karthi")

print(employees.name)

employees.name = "Karthi Kumar"

print(employees.name)