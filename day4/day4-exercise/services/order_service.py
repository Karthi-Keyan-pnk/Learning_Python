from models.order import Order
from repository.order_repository import save_order


def calculate_total(items: list[dict])-> float:
    return sum(item["price"] * item["quantity"] for item in items )

def calculate_discount(total: float,discount_percent:float) -> float:
    return total*discount_percent

def calculate_tax(total:float,tax_rate:float)-> float:
    return total*tax_rate

