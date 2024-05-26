import streamlit as st
import snowflake.connector
import datetime

import os

account = os.getenv('account')
user = os.getenv('user_snow')
password = os.getenv('password')
role = os.getenv('role')
warehouse = os.getenv('warehouse')
database = os.getenv('database')
schema = os.getenv('schema')

mydb = snowflake.connector.connect(
    user=user,
    password=password,
    account=account,
    warehouse=warehouse,
    database=database,
    schema=schema
)
mycursor = mydb.cursor()
student_id = 3
custom_css = """
<style>
    div.stButton > button:first-child{
    background-color: rgba(131, 168, 245, 1);
    color: rgb(255, 255, 255);
    font-size: 10px;
    height: 3em;
    width: 10em;
    border-radius: 21.5px 21.5px 21.5px 21.5px;
    margin: 0 auto;
    display: block;
    }</style>"""
st.markdown(custom_css, unsafe_allow_html=True)
# st.markdown(
#     """
#     <div style="background-color:#f63366;padding:10px;border-radius:10px;">
#         <h2 style="color:white;text-align:center;">Edit Student Detail</h2>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
def hide_sidebar():
    st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

with st.form(key="edit_form"):
    st.title("Edit Student Detail")
    hide_sidebar()
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
        # next_student_id = result + 1 if result is not None else 1
        sql = "UPDATE student SET student_firstname = %s, student_lastname = %s, student_gender = %s, department_name = %s, student_year = %s, student_semester = %s, student_address = %s, student_email = %s, student_phone = %s, student_dateofbirth = %s WHERE student_id = %s"
        # Define the values to be updated in the SQL query
        val = (student_firstname, student_lastname, student_gender, student_department, student_year, student_semester, student_address, student_email, student_phone, student_birth, student_id)

        # Execute the SQL query
        mycursor.execute(sql, val)
        
        # Commit the transaction
        mydb.commit()
        st.rerun()