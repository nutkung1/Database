import streamlit as st
import snowflake.connector
import datetime

# Establish connection to Snowflake
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

# Assuming instructor_id is stored in the session state
instructor_id = 1
# instructor_id = st.session_state["instructor_id"]

# Custom CSS for the button
custom_css = """
<style>
    div.stButton > button:first-child {
        background-color: rgba(131, 168, 245, 1);
        color: rgb(255, 255, 255);
        font-size: 10px;
        height: 3em;
        width: 10em;
        border-radius: 21.5px;
        margin: 0 auto;
        display: block;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

def hide_sidebar():
    st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

with st.form(key="edit_form"):
    st.title("Edit Instructor Detail")
    hide_sidebar()
    col = st.columns(2)
    with col[0]:
        instructor_firstname = st.text_input("First Name", placeholder="First Name", key="ins_first_name")
        instructor_lastname = st.text_input("Last Name", placeholder="Last Name", key="ins_last_name")
        instructor_gender = st.selectbox("Gender", ["Male", "Female", "Others"], key="ins_gender")
    with col[1]:
        instructor_phone = st.text_input("Phone Number", placeholder="Phone Number", key="ins_phone")
        instructor_email = st.text_input("Email", placeholder="Email", key="ins_email")
        instructor_birth = st.date_input("Date of Birth", min_value=datetime.date(year=1950, month=1, day=1), key="ins_birth")
    instructor_address = st.text_area("Address", placeholder="Address", key="ins_address")
    
    submit = st.form_submit_button("Submit")
    if submit:
        sql = """
        UPDATE instructor
        SET 
            Instructor_firstname = %s,
            Instructor_lastname = %s,
            Instructor_gender = %s,
            Instructor_dateofbirth = %s,
            Instructor_phone = %s,
            Instructor_email = %s,
            Instructor_address_1 = %s
        WHERE 
            Instructor_ID = %s
        """
        # Define the values to be updated in the SQL query
        val = (instructor_firstname, instructor_lastname, instructor_gender, instructor_birth, instructor_phone, instructor_email, instructor_address, instructor_id)

        # Execute the SQL query
        mycursor.execute(sql, val)
        
        # Commit the transaction
        mydb.commit()
        st.success("Instructor details updated successfully.")
        st.experimental_rerun()
