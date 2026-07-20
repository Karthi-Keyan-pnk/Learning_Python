import logging

balance = 100

# try:
#     amount = float(input("Enter amount to withdraw: "))
#     if amount > balance:
#         raise InsufficientFundsError("Insufficient funds for this transaction.")
# except InsufficientFundsError as e:
#     print(e)

# a=input("Enter a number: ")
# print(type(a))


try:
    x = 10 / 0

except Exception as e:
    print(f"An error occurred: {e}")


logging.basicConfig(filename="app.log", level=logging.ERROR)
logging.info("This is an info message")
