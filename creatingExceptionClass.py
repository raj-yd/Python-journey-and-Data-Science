#subclass: InsufficientBalanceError
#superclass: Exception
#relation: superclass is a parent of subclass
class InsufficientBalanceError(Exception):
    pass
def withdraw(balance,amount):
    if amount>balance:
        raise InsufficientBalanceError("Balance is not Enough")
    print("Transaction Successfully ")
    return f"Balance Left : {balance-amount}"
try:
    print(withdraw(int(input("Enter Balance : ")),int(input("Enter Amount : "))))
except InsufficientBalanceError as e:
    print(e)
else :
    print("Every thing is okay")