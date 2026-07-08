with open("students.csv","w") as file :
    file.write("name,age,marks,city\n")
    file.write("Raj,20,80,Prayagraj\n")
    file.write("Priyanshu,19,75,Ayodhya\n")
    file.write("Saumya,19,78,Varanshi\n")

    print("CSV File CReated Successfully!")