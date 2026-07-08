#smart EMI calculator without interest
product=input("Enter Product Name : ")
price=float(input("Enter price per unit : "))
no_of_months=int(input("Enter no.of months : "))
emi=price/no_of_months
print(f"The total cost of {product}: {price}")
print(f"Equated Monthly Installment without interest: {emi}")

#with interest
interest_rate=float(input("Enter Annual interest rate(in percentage) : "))
monthly_interest_rate=interest_rate/12/100
emi=price*monthly_interest_rate/(1-(1+monthly_interest_rate)**(-no_of_months)) #using formula for EMI =p*r/(1-(1+r)^-n)
print(f"Equated Monthly Installment with interest: {emi}")