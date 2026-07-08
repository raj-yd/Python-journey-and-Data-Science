import pandas as pd
print("Version")
print(pd.__version__)
marks=pd.Series([2,4,3,1,6])
print(marks)
print(type(marks))
print(marks.dtype)
print('Aniket marks',marks[1]) #access by position

marks=pd.Series([2,4,3,1,6],index=["Raj","Aniket","Priyanshu","Saumya","Arun"])
print(marks)
#access by name
print('Aniket marks',marks["Aniket"]) #selecting index (costumized)

#operations on pandas
print(marks+5)
print(marks[marks > 80]) #filter
print(marks.mean())
print(marks.max())
print(marks.min())
print(marks.sort_values())
print(marks.describe()) #full statisctics

data={"Name":["Raj Yadav","Priyanshu Pandey","Aniket Kumar Maurya","Saumya Tripathi","Arun Yadav"],
      "Age":[89,76,78,77,79],
      "Roll number":[34,56,32,78,43]}

print(pd.DataFrame(data))

#error
# student = {
#     "name": "Raj",
#     "age": 20,
#     "marks": 88,
#     "city": "Lucknow"
# }
# print(pd.DataFrame(student)) #pd.DataFrame() expects the values to be list-like (or another iterable) when you pass a dictionary.
