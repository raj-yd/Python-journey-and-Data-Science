import pandas as pd
import numpy as np

df=pd.read_csv('messy_students.csv')
#number of problems ,we will identify
print('null : ',df.isnull().sum())
print('duplicated',df.duplicated().sum())
print('dtype',df.dtypes)
print('max value of maxks',df['Marks'].max())
print(df['City'].unique())

import pandas as pd
import numpy as np

df = pd.read_csv('messy_students.csv')

#number of problems we will identify
print('null: ', df.isnull().sum())
print('duplicated: ', df.duplicated().sum())
print('dtype: ', df.dtypes)
print('max value in Marks: ', df['Marks'].max())
print(df['City'].unique())

print(f'Before: {df.shape}')

#cleaning
#removing duplicates
df=df.drop_duplicates()

#text inconsistancy
df['Name'] = df['Name'].str.strip().str.title()
df['City'] = df['City'].str.strip().str.title()

#fixing data type
df['Attendance'] = (df['Attendance'].str.replace('%','').astype(float))

#fixing invalid numbers
df['Marks'] = df['Marks'].clip(0, 100)

#fixing missing values
df['Name'] = df['Name'].fillna('Unknown')
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

#adding derived class (adding more column)
df['Result'] = df['Marks'].apply(
    lambda x: 'Pass' if x >= 40 else 'Fail'
)
print(f'After: {df.shape}')
print('total nulls: ', df.isnull().sum())

df.to_csv('clean_students.csv', index = False)
print(df)