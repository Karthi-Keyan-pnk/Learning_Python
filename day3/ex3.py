class Employee:
    def __init__(self, name, salary):
        self.name =name
        self._salary = salary
    
    @property
    def salary(self)->float:
        return self._salary
    
    @salary.setter
    def salary(self, new_salary: float):
        if(new_salary < 0):
            raise ValueError("Salary cannot be negative")
        self._salary = new_salary

employee = Employee("John", 50000)
employee.salary = -70000
print(employee.salary)
