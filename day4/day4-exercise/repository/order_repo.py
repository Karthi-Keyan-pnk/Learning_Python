def save_order(
    customer_name: str,
    subtotal :float,
    discount:float,
    tax: float,
    final_total :float
) -> None:

    with open("order.txt", "w") as file:

        file.write(f"Customer:{customer_name}\n")
        file.write(f"Subtotal:{subtotal}\n")
        file.write(f"Discount: {discount}\n")
        file.write(f"Tax:{tax}\n")
        file.write(f"Final Total: {final_total}\n")