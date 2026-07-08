age=int(input("Enter your age : "))
movie_type=input("Enter Movie type (U,U/A,A)").upper()
if movie_type=="U":
    print("You are allowed to watch movie")
elif movie_type=="U/A":
    if age>=12:
        print("You are allowed to watch movie")
    else :
        print("You are not allowed to watch movie")
elif movie_type=="A":
    if age>=18:
        print("You are allowed to watch movie")
    else :
        print("You are not allowed to watch movie")
else : 
    print("Please enter valid movie type")