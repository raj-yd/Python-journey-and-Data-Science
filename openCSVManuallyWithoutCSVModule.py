with open("students.csv","r") as file:
    #list
    lines=file.readlines()
    header=lines[0].strip().split(",")
    print(f"Columns : {header}") #list of columns

    for line in lines[1:]:
        data=line.strip().split(",")
        name=data[0]
        age=int(data[1])
        marks=int(data[2])
        city=data[3]
        print(f"{name},{age},{marks},{city}")



print()
#More Attractive
with open("students.csv","r") as file:
    #list
    lines=file.readlines()
    header=lines[0].strip().split(",")
    print(f"{header[0].capitalize()},{header[1].capitalize()},{header[2].capitalize()},{header[3].capitalize()}") 
    print()
    for line in lines[1:]:
        data=line.strip().split(",")
        name=data[0]
        age=int(data[1])
        marks=int(data[2])
        city=data[3]
        print(f"{name},{age},{marks},{city}")