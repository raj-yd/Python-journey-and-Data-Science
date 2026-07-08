#student_percentage_calculator
marks=input("Enter marks of five subject using separation Space : ").split()
totalmarks=float(marks[0])+float(marks[1])+float(marks[2])+float(marks[3])+float(marks[4])
percent=(totalmarks/500)*100
print(f"Percentage : {percent}")