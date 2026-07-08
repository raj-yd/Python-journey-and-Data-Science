#sorting list of tuples by its marks (second key)
students=[
    ("Priyanshu",80),
    ("Arun",75),
    ("Aniket",85),
    ("Saumya",78),
    ("Raj",90)
]
# list.sort() #it modifies the current list
# sorted() #it creates new modified list

students_sorted=sorted(students,key = lambda student:student[1])
print(f"students_sorted = {students_sorted}")

#filtering (marks > 80)
marks = [45, 92, 42, 91, 92, 55, 99, 33]
marks_greater_than80=list(filter(lambda mark : mark>80,marks))   #filter() ek filter object return karta hai (iterator) Ye directly list nahi deta
print(f"marks_greater_than80 = {marks_greater_than80}")