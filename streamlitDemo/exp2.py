import streamlit as st
import numpy as np
import csv
list=[]
with open("car data.csv","r") as file1:
    dictCSV=csv.DictReader(file1)
    for row in dictCSV:
        if row["Car_Name"] not in list:
            list.append(row["Car_Name"])
print(list)
print(len(list))
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(5 in numbers)
#st.write(f"{np.array(list)}")