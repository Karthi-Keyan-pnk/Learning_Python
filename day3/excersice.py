from dataclasses import dataclass

@dataclass
class InvoiceData:
    invoice_number:int
    customer:str
    amount:float
    status:str

invoice = InvoiceData(12, "John Doe", 100.0, "paid")
print(invoice)


class Invoice:
    def __init__(self, customer:str, amount:float):
        self.customer = customer
        self.amount = amount
    
    def validate(self)-> None:
        if self.amount<=0:
            raise ValueError("Amount must be greater than zero")
        if not self.customer:
            raise ValueError("Customer name cannot be empty")
    