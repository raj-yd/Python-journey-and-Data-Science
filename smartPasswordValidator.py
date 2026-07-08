while(True):
    password=input("Enter password : ")
    if len(password)>=8:
        print("Password Accepted")
        break
    else :
        print("Invalid Password less than 8 characters")