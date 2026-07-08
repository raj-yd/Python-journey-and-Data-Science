import pandas as pd
#loading data(csv)
df=pd.read_csv('students.csv')
print(df)

#iloc() and loc()
print()
#iloc()
print(df.iloc[0]) #first row
print(df.iloc[2])
print(df.iloc[-1]) #last Row
print(df.iloc[2:5]) #rows : 2,3,4
print(df.iloc[2,4]) # row 2 , col 4
print()
#loc
#label name
print(df.loc[0,"Name"]) # 0 row , and name columnn
print(df.loc[3]) 

#test all the properties/functions on this data
