import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("clean_students.csv")
fig ,ax = plt.subplots(figsize=(8,5))

ax.bar(
    df["Name"],df["Marks"],color ='steelblue',edgecolor='white'

)

ax.set_title("Students Marks",fontsize=14,fontweight="bold")
ax.set_xlabel('Students')
ax.set_ylabel('Marks')
ax.axhline(y=40,color='red',linestyle='--',label="Passing marks")
ax.legend()
ax.tick_params(axis='x',rotation=45)
plt.tight_layout()
plt.show()