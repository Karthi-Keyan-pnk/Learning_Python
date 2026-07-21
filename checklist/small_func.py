def area_of_rectangle(length:float, width: float)-> float:

    """
    Function to calculate the area of a rectangle.
    """

    return length * width

def eligible_to_vote(age:int)-> bool:

    """
    Function to check if a person is eligible to vote based on age.
    """
    
    return age >= 18

def gst_calculator(price:float)-> float:

    """
    Function to calculate the GST amount based on price and GST rate.
    """

    return price*(18/100)



print(area_of_rectangle(5, 10))
print(eligible_to_vote(20))
print(gst_calculator(1000))