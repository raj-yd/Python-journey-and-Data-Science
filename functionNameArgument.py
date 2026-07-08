def information(name,age,gender,location):
    informations={
        "name":name,
        "age":age,
        "gender":gender,
        "location":location
    }
    return informations
    
    
value1 = information("Raj",20,"Male","Prayagraj")

#logical error --> order is not appropriate
value2 = information(20,"Raj","Prayagraj","Male")

print(value1)
print(value2)

#fixing logical error
value2 = information(age=20,name="Raj",location="Prayagraj",gender="Male")
print(value2)

