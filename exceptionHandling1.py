# > ZeroDivisionError: division by zero
try:
    num1=int(input("Enter number : "))
    operation=100/num1
except ZeroDivisionError:
    print("Sorry any number cannot divided by 0 ")
except ValueError:
    print("Sorry you must enter integer number ")
except Exception as e:
    print(f"Something ent wrong - {e}")
else : 
    print(f"Result = {operation}")
finally:
    print("Thankyou!!")