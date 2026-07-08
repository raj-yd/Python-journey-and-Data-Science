def information(name,age,gender="Not defined",location="Not defined"):
    informations={
        "name":name,
        "age":age,
        "gender":gender,
        "location":location
    }
    return informations
    
    
value1 = information("Raj",20,"Male","Prayagraj")
value2=information("Raj",20)
print(value1)
print(value2)
value3=information(age=20 ,location="Prayagraj",name="Raj")
print(value3)