import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title = 'Student Data Explorer',
    page_icon = '[]',
    layout = 'wide'
)

st.title('Student Data Exlorer')
st.write('Interactive streamlit web application that implements csv, pandas, and numpy')

#Loading data
@st.cache_data #it prevents multiple loading
def load_data():
    df = pd.read_csv('students.csv')
    df['Total'] = (df['Maths'] + df['Science'] + df['English'])
    df['Percentage'] = (df['Total']/300 * 100)
    df['Result'] = df['Percentage'].apply(
        lambda x: 'Pass' if x >= 40 else 'Fail'
    )

    return df

df = load_data()
# print(df)

st.sidebar.title('Filter')

cities = ['All'] + list(df['City'].unique())
city_filter = st.sidebar.selectbox('Filter by City', cities)

min_marks = st.sidebar.slider('Minimum Marks', 0, 100, 0)

result_filter = st.sidebar.radio('Result', ['All', 'Pass', 'Fail'])

filtered = df.copy()

if city_filter != 'All':
    filtered = filtered[filtered['City'] == city_filter]

filtered = filtered[filtered['Maths'] >= min_marks]

col1, col2, col3, col4 = st.columns(4)

col1.metric('Total Students', len(filtered))
col2.metric('Avg Maths', f'{filtered['Maths'].mean():.1f}' if len(filtered) > 0 else 'N/A')
col3.metric('Pass count', len(filtered[filtered['Result'] == 'Pass']))
col4.metric('Fail count', len(filtered[filtered['Result'] == 'Fail']))

st.divider()

st.subheader('Student Records')
st.dataframe(filtered, use_container_width = True)

st.divider()

#charts
left, right = st.columns(2)

with left:
    st.subheader('Maths Marks Distribution')
    st.bar_chart(filtered.set_index('Name')['Maths'])

with right:
    st.subheader('Students per City')
    city_counts = filtered['City'].value_counts()
    st.bar_chart(city_counts)

#division for downloading your filtered data
st.divider()

st.subheader('Download your filtered data')
csv = filtered.to_csv(index=False)

st.download_button(
    label = 'Download as CSV',
    data = csv,
    file_name = 'filtered_students.csv',
    mime = 'text/csv'
)