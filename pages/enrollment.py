import streamlit as st
import snowflake.connector
from datetime import datetime

# Function to hide the sidebar
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
    with st.form(key="enrollment_register"):
        st.title("Create Enrollment Record")
        st.write("Please fill out the enrollment form below:")

        col1, col2 = st.columns(2)

        with col1:
            enrollment_id = st.number_input("Enrollment ID", min_value=1)
            # enrollment_schoolyear = st.number_input("Enrollment School Year", min_value=1)
            enrollment_course = st.text_input("Enrollment Course")
    
            enrollment_created_by = st.text_input("Created By")
            enrollment_is_active = st.checkbox("Is Active")

        with col2:
            student_id = st.number_input("Student ID", min_value=1)
            enrollment_schoolyear = st.number_input("Enrollment School Year", min_value=1)
            # enrollment_updated_by = st.text_input("Updated By")
            enrollment_updated_by = st.date_input("Created at", min_value=datetime.now(), max_value=datetime.now())
            # enrollment_is_active = st.checkbox("Is Active")

        enrollment_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        enrollment_updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # agreement = st.checkbox("I agree to all statements in [Terms and Conditions](http://www.example.com/terms)", value=False, key="agree")

        # Center align the button
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

        submit_button = st.form_submit_button("Submit")
        if submit_button:
            if not all([enrollment_id, enrollment_schoolyear, enrollment_course, enrollment_created_by, student_id, enrollment_updated_by]):
                st.error("Please fill in all fields.")
            elif not agreement:
                st.error("Please agree to the Terms and Conditions.")
            else:
                enrollment_is_active_int = 1 if enrollment_is_active else 0
                sql = """
                INSERT INTO enrollment 
                (enrollment_id, enrollment_schoolyear, enrollment_course, enrollment_is_active, 
                enrollment_created_at, enrollment_created_by, enrollment_updated_at, enrollment_updated_by, student_id) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                val = (enrollment_id, enrollment_schoolyear, enrollment_course, enrollment_is_active_int, 
                       enrollment_created_at, enrollment_created_by, enrollment_updated_at, enrollment_updated_by, student_id)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Enrollment record created successfully.")
                st.experimental_rerun()

        # Center align the link
        # st.markdown("""
        # <div class="center">
        #     <a href="http://www.example.com" style="color: #83A8F5;">Already have a record? Log in here.</a>
        # </div>
        # """, unsafe_allow_html=True)

# Calling the main function
if __name__ == "__main__":
    main()
