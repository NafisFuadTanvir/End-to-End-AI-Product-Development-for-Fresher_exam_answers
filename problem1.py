def withdraw(balance,withdraw_amount):
    if withdraw_amount>balance:
        raise Exception ("insufficient funds")
    return balance-withdraw_amount

print(withdraw(500,100))