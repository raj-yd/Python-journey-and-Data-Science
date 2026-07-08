from mathOperation import pi,addition,multiply,floor_division

print(f"addition(1,2,3,4,5) =  {addition(1,2,3,4,5)}")
print(f"multiply(1,2,3,4)={multiply(1,2,3,4)}")
print(f"Pi = {pi}")
print(f"floor_division(4,3) = {floor_division(4,3)}")

#importing our own package' modules
from school.students import getstudents
from school.faculties import getFacultyLlist
print(f"Students = {getstudents()}")
print(f"Faculties = {getFacultyLlist()}")

#importing our own subpackage' module
import school.staff.salaryCalculation as salary
print(f"Base salary for peons is {salary.base_salary}")