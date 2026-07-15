
def function(price : int)-> int:
    return price*2;

print(type(function(10)));




def func(*arg):
    return [n*n for n in arg ]

print(func(1,2,3,4,5,6))




def function(item : str , intems: list[str]|None = None):
    if intems is None:
         intems = []
    intems.append(item)
    return intems

function("apple")
function("banana", ["orange"])
function("grape", ["kiwi", "mango"])

print(function("pear"))



def func2(list1:list[int])-> list[int]:
    return [n*2 for n in list1]

print(func2([1,2,3,4,5]))

def func3(value: int | str )-> None:
    print(f"Value is: {value}")

func3(10)
func3("Hello")



def add(a:int,b:int)->int:
    return a+b;

def calculate(val1:int ,val2:int,operation:[[int,int],int])->int:
    return operation(val1,val2)

print(f"value{calculate(10,20,add)}")


def my_decorator(function):
    def wrapper():
        print("Before the function is called.")
        function()
        print("After the function is called.")
    return wrapper


@my_decorator  # greet = my_decorator(greet)
def greet() ->None:
    print("Hello, World!")


greet()

print("#################################################")


def process_order(customer_name, items, discount_percent, save_to_file):
    if customer_name:
        if items:
            total = 0

            for item in items:
                if item["price"] > 0 and item["quantity"] > 0:
                    total += item["price"] * item["quantity"]
                else:
                    print("Invalid item found")
                    return None

            if discount_percent >= 0:
                if discount_percent <= 100:
                    discount = total * discount_percent / 100
                    final_total = total - discount

                    tax = final_total * 0.18
                    final_total = final_total + tax

                    print(f"Customer: {customer_name}")
                    print(f"Subtotal: {total}")
                    print(f"Discount: {discount}")
                    print(f"Tax: {tax}")
                    print(f"Final total: {final_total}")

                    if save_to_file:
                        file = open("order.txt", "w")
                        file.write(f"Customer: {customer_name}\n")
                        file.write(f"Subtotal: {total}\n")
                        file.write(f"Discount: {discount}\n")
                        file.write(f"Tax: {tax}\n")
                        file.write(f"Final total: {final_total}\n")
                        file.close()

                    return final_total
                else:
                    print("Discount cannot be greater than 100")
                    return None
            else:
                print("Discount cannot be negative")
                return None
        else:
            print("Items cannot be empty")
            return None
    else:
        print("Customer name is required")
        return None


items = [
    {"name": "Laptop", "price": 50000, "quantity": 1},
    {"name": "Mouse", "price": 1000, "quantity": 2},
]

process_order("Karthi", items, 10, True)


