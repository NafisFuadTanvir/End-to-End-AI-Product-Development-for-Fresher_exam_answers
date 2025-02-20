
"""
Question = "You are building a calculator app. Write a Python function calculate ( ) that takes two
numbers and an operator (+,
*, /) as input and returns the result."

"""


def calculate(number_one,number_two,operator):
    
    if operator=="+":
        return number_one+number_two
    elif operator=="-":
        return number_one-number_two
    elif operator=="*":
        return number_one*number_two
    elif operator=="/":
        if number_two==0:
            raise Exception("division by 0 is not possible")
        return number_one / number_two
    else:
        raise Exception("invalid operator")


print(calculate(500,0,"~"))    