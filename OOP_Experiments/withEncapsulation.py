class BankAccount:
    def __init__(self,owner_name,balance):
        self.owner_name=owner_name #public (accessible everywhere)
        self.__balance=balance #private (cannot be accessible outside the class) | background property : name mangled in python
        self._email=None #protected
        #protected - convention: internal use

    def deposite(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f'Deposited Amount Rs. {amount}')
            
        else:
            print(f'Invalid Amount')

    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
        else :
            print(f'Invalid or Insufficient Balance')

    def get_balance(self): #controlled statement/return value
        return self.__balance
    
account=BankAccount("Raj",56000)
#print(account.__balance)  #error
#Direct Access: Denied
# print('account.__balance', account.__balance) #Attribute Error

#if you want operations on these protected/private members, always use controlled functions

#account.withdraw(-70)

account.withdraw(5000)
print(account.get_balance())










# # by me-
# account=BankAccount("Rajnikant",500000)
# # print(account._BankAccount__balance)  # as balance is private soo but not recommended this beacuse this breaks the purpuse of encapsulation
# # account._BankAccount__balance=25000
# # print(account._BankAccount__balance)  #25000

# account.get_balance() # recommended

# print(account.get_balance())

# #BankAccount ke andar ye ye method define karo agar balance change karna ho to (recommended)
# # def set_balance(self, balance):
# #         self.__balance = balance