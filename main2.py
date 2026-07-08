import student_utils
try:
    print(f"Average marks = {student_utils.calculate_percentage([int(x) for x in input("Enter marks Seperated by Space : ").split()])}")
except ValueError as e:
    print("Error - ",e)
try:
    print(student_utils.get_grade(int(input("Enter percentage : "))))
except student_utils.PercentageError as e:
    print(e)

# method 2
# try:
#     marks_input = input("Enter marks Seperated by Space : ")
#     marks_list = [int(x) for x in marks_input.split()]
    
#     avg = student_utils.calculate_percentage(marks_list)
#     print(f"Average marks = {avg}")

# except ValueError as e:
#     print("Error - ", e)


# try:
#     percentage = int(input("Enter percentage : "))
#     grade = student_utils.get_grade(percentage)
#     print(grade)

# except student_utils.PercentageError as e:
#     print(e)