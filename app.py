import streamlit as st
from dotenv import load_dotenv
import mysql.connector
import os
import streamlit_shadcn_ui as ui
import pandas as pd
import streamlit_authenticator as stauth
from st_pages import Page, show_pages
# Set Streamlit page configuration
st.set_page_config(
    page_title="Streamlit App",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

@st.cache_data(show_spinner=False)
def split_frame(input_df, rows):
    df = [input_df.loc[i : i + rows - 1, :] for i in range(0, len(input_df), rows)]
    return df

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("host"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    database=os.getenv("databaseProj"),
    auth_plugin='mysql_native_password'
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Test")
data= mycursor.fetchall()
# Creating a DataFrame
invoice_df = pd.DataFrame(data, columns=['ID', 'Name', 'password', 'role'])
custom_css = """
<style>
/* Custom CSS styles */
.stForm {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f5f5f5;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.stTextInput input[type="text"],
.stTextInput input[type="password"] {
    width: 100%;
    padding: 10px;
    margin-top: 5px;
    margin-bottom: 5px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

div.stButton > button:first-child {
    background-color: #f5f5f5;
    color: #333333;
    font-size: 10px;
    height: 3em;
    width: 30em;
    border-radius: 10px 10px 10px 10px;
}

.stFormSubmitButton button {
    background-color: #f5f5f5;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

div[data-baseweb="select"] {
    background-color: #ffffff;
    border: 1px solid #ced4da;
    border-radius: 5px;
}

div[data-baseweb="select"] > div {
    padding: 8px 12px;
    color: #333333;
}

div[data-baseweb="select"] svg {
    fill: #666666;
}

div[data-baseweb="select"]:hover {
    border-color: #6c757d;
}

.stFormSubmitButton button:hover {
    background-color: #f5f5f5;
}

[data-testid="stForm"] {
    background: LightBlue;
}

.custom-sidebar {
    padding: 15px;
    margin-bottom: 20px;
    background-color: #374151;
    border-radius: 10px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.custom-sidebar:hover {
    background-color: #4b5563;
    transition: background-color 0.3s ease;
}

.custom-subheader {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
    color: #d1d5db;
}

/* Custom select box style for sorting */
.custom-sort-select select {
    width: 100%;
    padding: 10px;
    margin-top: 5px;
    margin-bottom: 5px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #ffffff;
    color: #333333;
}
</style>

"""


st.markdown(custom_css, unsafe_allow_html=True)


mycursor.execute("SELECT * FROM Test")
result = mycursor.fetchall()
emails = []
usernames = []
passwords = []
role = []
for user in result:
    emails.append(user[1])  # Assuming email is the first field in the tuple
    usernames.append(user[1])
    passwords.append(user[2])  # Assuming password is the second field in the tuple
    role.append(user[3])  # Assuming role is the third field in the tuple
credentials = {'usernames': {}}  # Fix the key here
# st.write(emails)
# st.write(usernames)
# st.write(passwords)
for index in range(len(emails)):
    credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}
authenticator = stauth.Authenticate(credentials, cookie_name='Streamlit', key='nutty', cookie_expiry_days=2)

if 'authentication_status' not in st.session_state:
    # If it doesn't exist, initialize it to False
    st.session_state['authentication_status'] = False

if not st.session_state['authentication_status']:
    st.markdown("<h1 style='text-align: center; background-color: #1565c0; color: #ece5f6'>Login</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; background-color: #1565c0; color: #ece5f6'>KMUTT University</h4>", unsafe_allow_html=True)

email, authenticator_status, username = authenticator.login(
                    fields={'Form name': ':green[Login]', 'Username': ':blue[Username]', 'Password': ':blue[Password]',
                            'Login': 'Login'})

if st.session_state["authentication_status"]:
    st.session_state["username"] = username
    st.session_state["role"] = role[usernames.index(username)]
    st.sidebar.image("https://static-00.iconduck.com/assets.00/shark-emoji-512x503-7lv5l7l3.png", width=100)
    st.sidebar.subheader(f"Welcome {username}")
    st.sidebar.subheader(f"Role: {role[usernames.index(username)]}")
    if st.session_state["authentication_status"] and st.session_state["role"] == "admin":
        st.selectbox("Select an operations", ["Create", "Update", "Delete"])
        col = st.columns([2, 1.5, 0.5])
        with col[0]:
            sort_field = st.selectbox("Sort and Search By", options=invoice_df.columns)
        with col[1]:
            search_query = st.text_input("Search", "")
        with col[2]:
            sort_direction = st.radio("Sorting", options=["⬆️", "⬇️"], horizontal=True)

        # Sort the dataset
        dataset = invoice_df.sort_values(by=sort_field, ascending=sort_direction == "⬆️", ignore_index=True)

        # Convert the sort_field column to string
        dataset[sort_field] = dataset[sort_field].astype(str)

        # Filter the dataset based on search query
        dataset = dataset[dataset[sort_field].str.contains(search_query, case=False)]



        # Display the filtered table
        ui.table(dataset)

    
    elif st.session_state["authentication_status"] and st.session_state["role"] == "student":
        student_df = invoice_df.drop(columns=['password'])
        ui.table(student_df)


    authenticator.logout("Logout", "sidebar")


