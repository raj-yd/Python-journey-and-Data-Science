username=input("Enter your username : ")
password=input("Enter your password : ")
current_username="admin"
current_password="1234"
if (username==current_username):
    if (password==current_password):
        print("Login Successfully")
    else :
        print("wrong Passwrod")
else : 
    print("Wrong Username")