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
employee.salary = 70000
print(employee.salary)


class Employee:
    def work(self):
        print("Working")


class Developer(Employee):
    def write_code(self):
        print("Writing code")

Employee1 = Developer()
Employee1.work()
Employee1.write_code()


class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()


car = Car()
car.start()
