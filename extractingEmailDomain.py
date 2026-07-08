email=input("Enter your email : ")
if "@" in email:
    at_position=email.index("@")
    username=email[:at_position]
    domain=email[at_position+1:]
    print(f"username - {username}")
    print(f'Domain - {domain}')
else :
    print("You entered invalid email")