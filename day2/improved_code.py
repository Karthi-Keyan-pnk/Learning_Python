def process_order(customer_name:str , items:list[dict], discount_percent:float , save_to_file:bool)-> None:

    if not customer_name:
        print("Customer name is required")
        return None

    if not items:
        print("Items cannot be empty")
        return None

    if not 0 <= discount_percent <= 100:
        print("Discount must be between 0 and 100")
        return None

    total = calculate_total(items)
    
    discounted_price, discount, tax = calculate_discount(discount_percent, total)

    if save_to_file:
        save_order_to_file(customer_name, total, discount, tax, discounted_price)
    print(f"Customer: {customer_name}")
    print(f"Subtotal: {total}")
    print(f"Discount: {discount}")
    print(f"Tax: {tax}")
    print(f"Final total: {discounted_price}")

def save_order_to_file(customer_name:str, total:float, discount:float, tax:float, final_total:float) -> None:
    try:
        with open("order.txt","w") as file:
            file.write(f"Customer: {customer_name}\n")
            file.write(f"Subtotal: {total}\n")
            file.write(f"Discount: {discount}\n")
            file.write(f"Tax: {tax}\n")
            file.write(f"Final total: {final_total}\n")
    except Exception as e:
        print("Error saving order to file."+ str(e))

def calculate_discount(discount_percent:float, total:float)-> tuple[float, float, float]:

    discount = total * discount_percent / 100

    total_after_discount = total - discount

    tax = total_after_discount * 0.18
    final_total = total_after_discount + tax
    return final_total, discount, tax


def calculate_total(items:list[dict])->float:

    try:
        return sum(item["price"] * item["quantity"] for item in items)
    
    except Exception as e:
        print("Error calculating total."+ str(e))
        return 0
    

items = [
    {"name": "Laptop", "price": 50000, "quantity": 1},
    {"name": "Mouse", "price": 1000, "quantity": 2}
]

process_order("Karthi", items, 10, True)