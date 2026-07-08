import pandas as pd
data={"Name":["Raj Yadav","Priyanshu Pandey","Aniket Kumar Maurya","Saumya Tripathi","Arun Yadav"],
      "Marks":[89,76,78,77,79],
      "Roll number":[34,56,32,78,43],
      "Age":[20,21,23,24,23],
      "City":["Lucknow","Delhi","Mumbai","Jaipur","Bengaluru"],
      "attendance" : [92, 85, 78, 96, 88]}

df=pd.DataFrame(data)

print(f"Data \n{data}")
print("\n")

print("DataFrame\n\n")
print(df)
print()

#basic properties/functions
print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)
print(df.size)
print(len(df))

print(df["Name"].dtype)
print(df["Age"].dtype)

print(df["Name"].dtype=="str")
print(df["Age"].dtype=="int64")