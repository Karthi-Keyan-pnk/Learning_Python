# import tomllib

# with open("config.toml", "rb") as f:
#     tomldata: dict = tomllib.load(f)

# print(tomldata)

# # try:
# #     print(int(input("Enter a number: ")))
# # except ValueError:
# #     print("Invalid input. Please enter a valid number.")

# # print("Hello, World!")

# square = lambda x: x * x

# print(square(5))

# number =[1,2,3,4,5]

# mapper= map(lambda x:x*2,number)

# print(list(mapper))

def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("Apple"))

print(add_item("Banana"))

def add_item1(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items

print(add_item1("Apple"))
print(add_item1("Banana"))