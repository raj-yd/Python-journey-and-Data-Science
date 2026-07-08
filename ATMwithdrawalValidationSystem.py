account_balance=25000
withdrawal_amount=int(input("Enter Amount to Withdraw : "))
if withdrawal_amount>=100:
    if withdrawal_amount<=25000:
        print("Transaction Successful")
    else:
        print("Insufficient balance")
elif withdrawal_amount>=0 : 
    print(f"Minimum withdrawal amount is {withdrawal_amount}")
else: 
    print("Invalid amount")