import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
st.set_page_config(page_title = 'Car Price Analyzer', page_icon = 'carpic.png', layout='wide')
if "logged_in" not in st.session_state:
    st.session_state.logged_in=False

st.markdown("""
<style>
.stApp {
    background-color: #ECF4E5;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style="
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: #1f2a44;
">
    CAR PRICE ANALYZER
</h1>
""", unsafe_allow_html=True)
st.text("\n\n")

def login():
    st.markdown("""
                <h1 style="
                text-align: center;
                font-size: 30px;
                font-weight: 650;
                color: #1E3A8A;
                ">
                🔐 LOGIN
                </h1>
                """, unsafe_allow_html=True)
    with open("loginData.csv","a+",newline="") as file1:
        file1.seek(0)
        dictCSV=csv.DictReader(file1)
        name=st.text_input("Name")
        password=st.text_input("Password",type="password")
        if st.button("Login"):
            if name and password:
                flag=False
                for data in dictCSV:
                    if data["username"]==name and  data["password"]==password:
                        flag=True
                        break
                if flag==True:
                    st.success("Login Successfully!!")
                    st.session_state.logged_in=True
                    st.rerun()
                else :
                    st.error("Invalid Username Or Password!!")

            else :
                st.warning("Please enter both username and password.")

    
def signup():
    st.markdown("""
                <h1 style="
                text-align: center;
                font-size: 30px;
                font-weight: 650;
                color: #1E3A8A;
                ">
                👤 Sign Up
                </h1>
                """, unsafe_allow_html=True)
    with open("loginData.csv","a+",newline="") as file1:
        file1.seek(0)
        data=csv.reader(file1)
        users= [row[0] for row in data]
        name=st.text_input("Name")
        password=st.text_input("Password",type="password")
        writer=csv.writer(file1)
        if st.button("Sign Up"):
            if name and password:
                if name in users:
                    st.error("Username not available! Please take another username")
                else:
                    writer.writerow([name,password])
                    st.success("Sign Up Successfully..")
                    st.session_state.logged_in=True
                    st.rerun()
            else:
                st.warning("Please enter both username and password.")
        


if not st.session_state.logged_in:
#if not True:
    option=st.radio("How would you like to continue?",["Login","Sign Up"],horizontal=True)
    if option=="Login":
        login()
    else :
        signup()
else:
    st.success("Welcome to Car Price Analyzer..")
    st.image("carpic.png",caption="Car Price Analyzer",width="stretch")
    st.divider()
    st.sidebar.title("Setting")
    uploaded_file = st.sidebar.file_uploader('DATASET - Upload CSV File',type=["csv"])
    data_source = uploaded_file if uploaded_file else "CAR DETAILS FROM CAR DEKHO.csv"
    df=pd.read_csv(data_source)

    headercolumn=list(df.columns)
    filtered_df = df.drop_duplicates()
    for hd in headercolumn:
        #options = ["All"] + list(df[hd].unique())
        # df[hd] = df[hd].fillna('Unknown')
        options = ["All"] + sorted(df[hd].dropna().unique())
        selected = st.sidebar.selectbox(f"Filter by {hd.capitalize()}",options)

        if selected != "All":
            filtered_df = filtered_df[filtered_df[hd] == selected]

    
    st.header("Car Details")
    col1,col2,col3,=st.columns(3)
    col1.metric("Total Cars",len(filtered_df))
    col2.metric("Car Brands",filtered_df[headercolumn[0]].nunique())
    col3.metric("Currently Unavailable",(filtered_df.isnull().any(axis=1)).sum())
    st.divider()
    st.subheader("Dublicate Data Found")
    st.write("Extra Dublicate Pieces(Removed) - ",df.duplicated().sum())
    
    
    for hd in headercolumn:
        if filtered_df[hd].dtype=="str":
            filtered_df[hd] = filtered_df[hd].fillna('Unknown')
        else:
            filtered_df[hd] = filtered_df[hd].fillna(round(filtered_df[hd].mean(), 2))

    st.divider()
    st.subheader("Records")
    st.dataframe(filtered_df, hide_index=True)
    
    st.divider()
    
    try:
        for col in filtered_df.columns:
            #if filtered_df[col].nunique() <= 20:   # maximum 20 unique values
            st.subheader(col.capitalize())
            count = filtered_df[col].value_counts()
            left,right=st.columns(2)
            total = count.sum()
            labels = [label if (value / total * 100) >= 2 else "" for label, value in zip(count.index, count.values)]

            with left:
                st.write(f"{col.capitalize()} Distribution Bar Chart")
                st.bar_chart(count)
                
            with right:
                st.write(f"{col.capitalize()} Distribution pie Chart")
                fig, ax = plt.subplots(figsize=(5, 5))
                ax.pie(
                count.values,
                labels=labels,
                autopct=lambda pct: f"{pct:.1f}%" if pct>=2 else "",
                startangle=90)
                #ax.set_title(f"{col.capitalize()} Distribution")
                ax.axis("equal")  # Pie ko circle banata hai
                st.pyplot(fig)
                #-----
                    
                
            st.divider()
    
    except ValueError as e:
        st.warning("No data available for the selected filters. Please change your filter selection.")


    st.header("📊 Statistics")
    st.write(filtered_df.describe())
    st.divider()
    st.sidebar.divider()
    st.write("Download Cleaned And Filtered Data")
    csvfile = filtered_df.to_csv(index = False)
    st.download_button(label='Download',data=csvfile,file_name='clean_filtered_data.csv',mime='text/csv')
    st.divider()
    st.info("You've reached the end of the analysis!")
    
    st.write('Thanks for exploring your dataset with Car Price Analyzer. Keep analyzing, keep learning! 🚀')
    #st.divider()
    # st.sidebar.link_button("My GitHUB","https://github.com/raj-yd")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in=False
        st.rerun()
