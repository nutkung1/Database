import streamlit as st
from dotenv import load_dotenv
# import mysql.connector
import datetime
import snowflake.connector
import os
import streamlit_shadcn_ui as ui
import pandas as pd
import streamlit_authenticator as stauth
from st_pages import Page, show_pages
from streamlit_extras.stylable_container import stylable_container
import time
from streamlit_navigation_bar import st_navbar
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

# Mysql
# mydb = snowflake.connector.connect(
#     host=os.getenv("host"),
#     user=os.getenv("user"),
#     password=os.getenv("password"),
#     database=os.getenv("databaseProj"),
#     auth_plugin='mysql_native_password'
# )
# mycursor = mydb.cursor()
# SNOWFLAKE
account = os.getenv('account')
user = os.getenv('user_snow')
password = os.getenv('password')
role = os.getenv('role')
warehouse = os.getenv('warehouse')
database = os.getenv('database')
schema = os.getenv('schema')
mydb = snowflake.connector.connect(
    user="suchanat",
    password="NuT0863771558-",
    account="PIPWYPD-LO69630",
    warehouse="COMPUTE_WH",
    database="DATABASE",
    schema="PUBLIC"
)
mycursor = mydb.cursor()
custom_css = """
<style>
.stForm {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    background-color: rgba(255, 255, 255, 1);
    border-radius: 13px;
}

.stTextInput input[type="text"],
.stTextInput input[type="password"] {
    width: 100%;
    padding: 5px;
    # border: 1px solid #ccc;
    # border-radius: 5px;
}

div.stButton > button:first-child{
    background-color: rgba(131, 168, 245, 1);
    color: rgb(255, 255, 255);
    font-size: 10px;
    height: 3em;
    width: 30em;
    border-radius: 21.5px 21.5px 21.5px 21.5px;
    margin: 0 auto;
    display: block;
}

div.stButton > button:hover {
    background-color: #f5f5f5;
    color: #333333;
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


[data-testid="stForm"] {
    max-height: 10000px;
    background: White;
    padding:50px;
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



mycursor.execute("SELECT * FROM authenticator")
result = mycursor.fetchall()
emails = []
usernames = []
passwords = []
role = []
for user in result:
    emails.append(user[0])  # Assuming email is the first field in the tuple
    usernames.append(user[0])
    passwords.append(user[1])  # Assuming password is the second field in the tuple
    role.append(user[2])  # Assuming role is the third field in the tuple
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

logo_url = "https://static-00.iconduck.com/assets.00/shark-emoji-512x503-7lv5l7l3.png"

login_header = f"""
<div style="text-align: center; background-color: rgba(131, 168, 245, 1); color: #ece5f6; padding: 20px; border-radius: 10px;">
    <div style="display: inline-block; background-color: rgba(131, 168, 245, 1); padding: 10px;">
        <img src="{logo_url}" alt="Logo" width="100">
    </div>
    <div style="margin-top: 20px;">
        <h2 style='text-align: center; color: #ece5f6; padding: 0px;'>Oceanview College</h2>
    </div>
</div>
"""

if not st.session_state['authentication_status']:
    st.markdown(login_header, unsafe_allow_html=True)

email, authenticator_status, username = authenticator.login(
                    fields={'Form name': ':black[Log In]', 'Username': ':blue[Username]', 'Password': ':blue[Password]',
                            'Login': 'Log in'})

if st.session_state["authentication_status"]:
    st.session_state["username"] = username
    st.session_state["role"] = role[usernames.index(username)]
    st.sidebar.image("https://static-00.iconduck.com/assets.00/shark-emoji-512x503-7lv5l7l3.png", width=100)
    st.sidebar.subheader(f"Welcome {username}")
    st.sidebar.subheader(f"Role: {role[usernames.index(username)]}")
    # Role ADMIN
    if st.session_state["authentication_status"] and st.session_state["role"] == "admin":
        page = st_navbar(["Home", "CRUD", "Enroll", "Community", "About"])
        if page == "Home":
            st.title("Home")
            st.write("Welcome to the Home Page")
            st.image("image/kmutt-websitelogo-01-scaled.jpg", width=600)  
        elif page == "CRUD":
            mycursor.execute("SELECT * FROM student")
            data = mycursor.fetchall()
            # Creating a DataFrame
            invoice_df = pd.DataFrame(data, columns=['student_id', 'student_firstname', 'student_lastname', 'student_gender', 'department_name', 'student_year', 'student_semester', 'student_address', 'student_email', 'student_phone', 'student_dateofbirth'])
            invoice_df['student_dateofbirth'] = invoice_df['student_dateofbirth'].astype(str)
            invoice_df['student_role'] = "Student"

            CRUD = st.selectbox("Select an operation", ["Insert", "Update", "Delete"])
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
            if search_query:
                dataset = dataset[dataset[sort_field].str.contains(search_query, case=False)]

            # Table with view details button
            colms = st.columns((1, 1, 1, 1, 1, 1, 1))
            fields = ['ID', 'Firstname', "Lastname", "email", "Department", "Role"]
            for col, field_name in zip(colms, fields):
                # header
                col.write(field_name)

            # Display the data
            if not dataset.empty:
                for x in range(len(dataset)):
                    col1, col2, col3, col4, col5, col6, col7 = st.columns((1, 1, 1, 1, 1, 1, 1))
                    col1.write(dataset['student_id'][x])  # email
                    col2.write(dataset['student_firstname'][x])  # unique ID
                    col3.write(dataset['student_lastname'][x])   # email status
                    col4.write(dataset['student_email'][x])
                    col5.write(dataset['department_name'][x])
                    col6.write(dataset['student_role'][x])
                    button_type = "View Detail"
                    button_phold = col7.empty()  # create a placeholder
                    do_action = button_phold.button(button_type, key=x)
                    if do_action:
                        pass # do some action with a row's data
                        button_phold.empty()  #  remove button
            else:
                st.warning("No data matching the search query.")


            # Display the filtered table
            if CRUD == "Insert":
                with st.form(key="insert_form"):
                    col = st.columns(2)
                    with col[0]:
                        student_firstname = st.text_input("First Name", placeholder="First Name", key="stu_first_name")
                        student_lastname = st.text_input("Last Name", placeholder="Last Name", key="stu_last_name")
                        student_gender = st.selectbox("Select an operations", ["Male", "Female", "Others"], key="stu_gender")
                        student_department = st.text_input("Department", placeholder="Department", key="stu_department")
                        student_year = st.number_input("Year", placeholder="Year", key="stu_year", min_value=1, max_value=4)
                    with col[1]:
                        student_semester = st.number_input("Semester", placeholder="Semester", key="stu_semester", min_value=1, max_value=2)
                        student_address = st.text_input("Address", placeholder="Address", key="stu_address")
                        student_email = st.text_input("Email", placeholder="Email", key="stu_email")
                        student_phone = st.text_input("Phone Number", placeholder="Phone Number", key="stu_phone")
                        student_birth = st.date_input("Date input", min_value=datetime.date(year=1990, month=12, day=31))
                    submit = st.form_submit_button("Submit")
                    if submit:
                        mycursor.execute("SELECT MAX(student_id) FROM student")
                        result = mycursor.fetchone()[0]
                        next_student_id = result + 1 if result is not None else 1
                        sql = "INSERT INTO student (student_id, student_firstname, student_lastname, student_gender, department_name, student_year, student_semester, student_address, student_email, student_phone, student_dateofbirth) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        val = (next_student_id, student_firstname, student_lastname, student_gender, student_department, student_year, student_semester, student_address, student_email, student_phone, student_birth)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        st.rerun()

    #ROLE Student
    elif st.session_state["authentication_status"] and st.session_state["role"] == "student":
        st.write("Welcome to Student Page")
        # student_df = invoice_df.drop(columns=['password'])
        # ui.table(student_df)


    authenticator.logout("Logout", "sidebar")
# else:
#     st.write("Wrong email or password, please try again.")

