students = [
    ["Rahul", 1], ["Amit", 2], ["Priya", 3], ["Neha", 4], ["Rohit", 5],
    ["Anjali", 6], ["Vikas", 7], ["Pooja", 8], ["Suresh", 9], ["Kiran", 10],
    ["Arjun", 11], ["Sneha", 12], ["Deepak", 13], ["Riya", 14], ["Manoj", 15],
    ["Kavita", 16], ["Nikhil", 17], ["Simran", 18], ["Raj", 19], ["Meena", 20],
    ["Aakash", 21], ["Divya", 22], ["Sunil", 23], ["Payal", 24], ["Gaurav", 25],
    ["Shreya", 26], ["Vivek", 27], ["Nisha", 28], ["Harsh", 29], ["Tina", 30],
    ["Yash", 31], ["Komal", 32], ["Ravi", 33], ["Alok", 34], ["Swati", 35],
    ["Varun", 36], ["Isha", 37], ["Mohit", 38], ["Rekha", 39], ["Sanjay", 40],
    ["Pankaj", 41], ["Ankit", 42], ["Sonia", 43], ["Tarun", 44], ["Geeta", 45],
    ["Lokesh", 46], ["Preeti", 47], ["Ramesh", 48], ["Jyoti", 49], ["Ajay", 50],
    ["Seema", 51], ["Kunal", 52], ["Bhavna", 53], ["Chirag", 54], ["Lata", 55],
    ["Dhruv", 56], ["Sakshi", 57], ["Umesh", 58], ["Ritu", 59], ["Hemant", 60]
]
print('************** Attendance Register *************')
for name,rollnumber in students:
    print(f"{rollnumber} : {name} , ",end="")
    mark=input("Mark P/A - ")
    if mark=="P" or mark=="p" or mark=="A" or mark=="a":
        students[rollnumber-1].append(mark)
    else :
        print(f"Please mark P/A and {name} is mark for absent now")
        students[rollnumber-1].append("A")
#print(students)
present_students=list(filter(lambda student : student[2]=="p" or student[2]=="P",students))
absent_students=list(filter(lambda student : student[2]=="a" or student[2]=="A",students))

print("Present Students - ")
for name,rollno,attendance in present_students:
    print(rollno,name)

print("Absent Students - ")
for name,rollno,attendance in absent_students:
    print(rollno,name)