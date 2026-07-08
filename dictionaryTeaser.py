#dictionary definition
students={"Name":"Raj Yadav",
          "Roll no":7,
          "Std":8,
          "School":"NRSJPS"
}
print(f"students = {students}")
print(f"type(students) = {type(students)}")
#print(f"students[college] : {students[college]}")  #NameError: name 'college' is not defined
print(f"students['School'] : {students['School']}")  #students['School'] : NRSJPS
print(f"students.get('College') = {students.get('College')}")  #students.get('College') = None
print(f"students.get('username') = {students.get('username')}")
print(f"students.get('name') = {students.get('name')}")

for i in students:
    print(f"students[{i}] : {students[i]}")