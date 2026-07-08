import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.set_page_config(page_title = 'Data Dashboard', page_icon = '[]', layout = 'wide')

st.title('Student Data Dashboard')

@st.cache_data
def load_clean_data():
    df = pd.read_csv("clean_students.csv")
    #if not cleaned, follow the process of cleaning mechanism
    return df

df = load_clean_data()

col1, col2, col3, col4 = st.columns(4)

# Metrics row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Students", len(df))
col2.metric("Average Marks",
            f"{df['Marks'].mean():.1f}")
col3.metric("Passed",
            len(df[df["Result"]=="Pass"]))
col4.metric("Pass %",
            f"{len(df[df['Result']=='Pass'])/len(df)*100:.0f}%")


st.divider()

#Data Table
st.subheader('Clean data')
st.dataframe(df, use_container_width = True)

st.divider()

#Three charts one by one
st.subheader('Visual Analysis')
column_1, column_2, column_3 = st.columns(3)

with column_1:
    fig, ax = plt.subplots(figsize=(5, 4))

    ax.bar(
        df['Name'], df['Marks'], color = 'steelblue', edgecolor = 'white'
    )

    ax.set_title('Students Marks', fontsize = 14, fontweight = 'bold')
    ax.set_xlabel('Student')
    ax.set_ylabel('Marks')
    ax.axhline(y=40, color = 'red', linestyle = '--', label = 'Passing Mark')
    ax.legend()
    ax.tick_params(axis = 'x', rotation = 45)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

with column_2:
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.hist(df['Marks'], bins = 5, color= 'coral', edgecolor='white')
    ax.axvline(df['Marks'].mean(), color = 'blue', linestyle = '--')
    ax.set_title('Marks Distribution', fontweight = 'bold')

    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

with column_3:
    fig, ax = plt.subplots(figsize=(5, 4))
    rc = df['Result'].value_counts()
    ax.pie(rc, labels = rc.index, autopct = '%1.1f%%', colors = ['green', 'red'])
    ax.set_title('Pass vs Fail', fontweight = 'bold')

    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

st.divider()

#filter section
st.subheader('Filter by City')

city = st.selectbox('Select City', ['All'] + list(df['City'].unique()))

if city != 'All':
    filtered = df[df['City'] == city]
else:
    filtered = df

st.dataframe(filtered[['Name', 'Marks', 'City', 'Result']], use_container_width = True)

#Downloading button
csv = df.to_csv(index = False)
st.download_button('Download Clean Data', csv, 'clean_data.csv', 'txt/csv')