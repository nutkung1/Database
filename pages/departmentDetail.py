import streamlit as st
import snowflake.connector


def hide_sidebar():
    st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

hide_sidebar()

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

def main():
    with st.form(key="department_register"):
        st.title("Create Department Record")
        st.write("Please fill out the department form below:")

        col1, col2 = st.columns(2)

        with col1:
            department_name = st.text_input("Department Name")
            program = st.text_input("Program")

        with col2:
            instructor_firstname = st.text_input("Instructor First Name")
            instructor_lastname = st.text_input("Instructor Last Name")

        agreement = st.checkbox("I agree to all statements in [Terms and Conditions](http://www.example.com/terms)", value=False, key="agree")

        # Center align the button
        st.markdown("""
        <style>
        .stButton>button {
            border-radius: 20px;
            background-color: #83A8F5;
            width: 100%;
            text-align: center;
        }
        .center {
            text-align: center;
        }
        a {
            color: #83A8F5;
        }
        </style>
        """, unsafe_allow_html=True)

        submit_button = st.form_submit_button("Create Record")
        if submit_button:
            if not all([department_name, program, instructor_firstname, instructor_lastname]):
                st.error("Please fill in all fields.")
            elif not agreement:
                st.error("Please agree to the Terms and Conditions.")
            else:
                # Inserting data into the department table
                sql = "INSERT INTO department (department_name, program, instructor_firstname, instructor_lastname) VALUES (%s, %s, %s, %s)"
                val = (department_name, program, instructor_firstname, instructor_lastname)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Department record created successfully.")
                st.experimental_rerun()

        # Center align the link
        st.markdown("""
        <div class="center">
            <a href="http://www.example.com" style="color: #83A8F5;">Already have a record? Log in here.</a>
        </div>
        """, unsafe_allow_html=True)

# Calling the main function
if __name__ == "__main__":
    main()
