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



from enum import Enum

class InvoiceStatus(Enum):
    DRAFT = "draft"
    PAID = "paid"
    CANCELLED = "cancelled"

status = InvoiceStatus.DRAFT
print(status.value)


from typing import NamedTuple

class Product(NamedTuple):
    name: str
    price: float

product = Product(name="Laptop", price=1200.00) # we cant assign a new value because NamedTuple is immutable
print(product.name)
# product.price = 1300.121 error : AttributeError: can't set attribute
 

class Invoice:
    def __init__(self,customer):
        self.customer = customer
        
    def __str__(self):
        return f"Invoice for {self.customer}"
    
    def __str__(self):
        return f"Invoice for {self.customer}" # it override the previous __str__ method

invoice = Invoice("John Doe")
print(invoice)

class Invoice:
    def __init__(self, customer: str, amount: float):
        self.customer = customer
        self.amount = amount

    def __repr__(self) -> str:
        return f"Invoice(customer={self.customer!r}, amount={self.amount!r})"

invoice = Invoice("John Doe", 100.0)
print(repr(invoice))



class Invoice:
    def __init__(self, customer, amount):
        self.customer = customer
        self.amount = amount
        
    def __eq__(self, other):
        return self.customer == other.customer and self.amount == other.amount

invoice1 = Invoice("Karthi", 5000)
invoice2 = Invoice("Karthi", 5000)

print(invoice1 == invoice2)  