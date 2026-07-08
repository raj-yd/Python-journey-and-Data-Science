import pandas as pd
#creating and saving a sample dataset
data = {
    "Name": [
        "Raj Yadav", "Priyanshu Pandey", "Aniket Kumar Maurya",
        "Saumya Tripathi", "Arun Yadav", "Aman Singh",
        "Riya Sharma", "Neha Verma", "Vikas Kumar",
        "Sneha Gupta"
    ],
    "Marks": [89, 76, 78, 77, 79, 91, 84, 73, 68, 95],
    "Maths" : [78, 85, 92, 67, 88, 74, 95, 81, 69, 90],
    "Science" : [82, 76, 91, 73, 87, 79, 94, 84, 71, 89],
    "English" : [75, 88, 80, 69, 92, 77, 85, 83, 74, 90],
    "Roll Number": [34, 56, 32, 78, 43, 25, 19, 67, 45, 88],
    "Age": [20, 21, 23, 24, 23, 22, 20, 21, 22, 23],
    "City": [
        "Lucknow", "Delhi", "Mumbai", "Jaipur", "Bengaluru",
        "Kanpur", "Pune", "Hyderabad", "Chennai", "Kolkata"
    ],
    "Attendance": [92, 85, 78, 96, 88, 94, 81, 76, 90, 98]
}

df=pd.DataFrame(data)
df.to_csv("students.csv",index=False)
print("csv file has created!")