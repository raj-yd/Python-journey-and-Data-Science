#The problem: without encapuslation
class BankAccount:
    def __init__(self,owner_name,balance):
        self.owner_name=owner_name
        self.balance=balance

account=BankAccount("Rajnikant",500000)
print(account.balance)

account.balance=25000
print(account.balance)

#problem is here:
#your balance is directly accessible
#and, anyone can access and modifies your value