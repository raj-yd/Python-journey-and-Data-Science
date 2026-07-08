import csv
employees = [
    ["Rahul Sharma", "Software Engineer", 1001],
    ["Priya Verma", "Data Analyst", 1002],
    ["Amit Kumar", "Project Manager", 1003],
    ["Sneha Gupta", "UI/UX Designer", 1004],
    ["Rohit Singh", "QA Engineer", 1005],
    ["Anjali Yadav", "HR Manager", 1006],
    ["Vikas Patel", "DevOps Engineer", 1007],
    ["Neha Mishra", "Business Analyst", 1008],
    ["Arjun Tiwari", "Backend Developer", 1009],
    ["Pooja Sharma", "Frontend Developer", 1010]
] #data(list of list)
with open("employeesData.csv","w",newline="") as file:  #newline=""  extra newline avoid karega
    writer=csv.writer(file)
    writer.writerows(employees)  #if we cannot write newline="" in with open("employeesData.csv","w") then two newline is add one is by csv and another is added by operating system
print("CSV written successfully")
#Assignment: Make every file of file handling with Exception Handling