"""
Class or Function?

if i need to perform a single or just need to return a value after some calculation then i will go for function
 but if i need to perform some action on the data or need to store some data then i will go for class.

 for tax calculation i will go for function because it is just a calculation and return the value
"""

def tax_calculation(price:float)->float:

    return price*(18/100)

print(tax_calculation(10000))