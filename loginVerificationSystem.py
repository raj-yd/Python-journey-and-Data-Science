username=input("Enter your username : ")
password=input("Enter your password : ")
current_username="admin"
current_password="1234"
if (username==current_username and password==current_password):
    print("Login Successfully")
elif (username!=current_username and password==current_password):
    print("Login Unsuccessfully\nYou entered wrong username")
elif (username==current_username and password!=current_password):
    print("Login Unsuccessfully\nYou entered wrong password")
else :
    print("Login Unsuccessfully\nUsername and password both are wrong")
