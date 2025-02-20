"""
Question="A banking application allows users to withdraw money. The function withdraw (balance,
amount) should check if the withdrawal amount is greater than the balance. If yes, it should
raise an exception "Insufficient funds", otherwise return the new balance."
"""

def withdraw(balance,withdraw_amount):
    if withdraw_amount>balance:
        raise Exception ("insufficient funds")
    return balance-withdraw_amount

print(withdraw(500,1000))