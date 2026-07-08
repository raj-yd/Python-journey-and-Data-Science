atm_pin=4563
for i in range(3):
    entered_pin=int(input("Enter Pin : "))
    if atm_pin==entered_pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN")
else:
    print("Account Temporarily Locked")