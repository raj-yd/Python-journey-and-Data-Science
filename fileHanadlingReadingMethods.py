#First Way: read(), reads entire content
with open('Welcome.txt','r') as file:
    content=file.read()
    print(content)

    #readline()
    lineOne=file.readline()
    print(f"LineOne - {lineOne}")  # output blank because cursor is at end of file because of read()

#Second Way: readline(), reads single line content from the cursor location
with open("Welcome.txt","r") as file :
    lineOne=file.readline()
    lineTwo=file.readline()
    print(f"LineOne - {lineOne}")
    print(f"LineTwo - {lineTwo}")

#Third Way: readlines(), reads line by line contents from the cursor location
with open("Welcome.txt","r") as file :
    contents=file.readlines()
    for i in contents:
        print(i) 
    for i in contents:
        print(i.strip()) #newline ko strip kar raha hai