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
    with st.form(key="course_registration"):
        st.title("Create Course Registration Record")
        st.write("Please fill out the course registration form below:")

        col1, col2 = st.columns(2)

        with col1:
            course_id = st.number_input("Course ID", min_value=1)
            section = st.number_input("Section", min_value=1)
            instructor_firstname = st.text_input("Instructor First Name", max_chars=30)
            instructor_lastname = st.text_input("Instructor Last Name", max_chars=30)
            instructor_id = st.number_input("Instructor ID", min_value=1)
    
        with col2:
            course_schoolyear = st.number_input("Course School Year", min_value=1950)
            enrollment_id = st.number_input("Enrollment ID", min_value=1)
            timetable_id = st.number_input("Timetable ID", min_value=1)
            timetable_slot = st.selectbox("Timetable Slot", options=["Monday 8:00-12:00", "Afternoon", "Evening"])
            coursename = st.selectbox("Course Name", options=["CPE241 Database Systems", "Afternoon", "Evening"])

        # agreement = st.checkbox("I agree to all statements in [Terms and Conditions](http://www.example.com/terms)", value=False, key="agree")

        # Center align the button
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

        submit_button = st.form_submit_button("Submit")
        if submit_button:
            if not all([course_id, section, instructor_firstname, instructor_lastname, instructor_id, course_schoolyear, enrollment_id, timetable_id]):
                st.error("Please fill in all fields.")
            elif not agreement:
                st.error("Please agree to the Terms and Conditions.")
            else:
                sql = """
                INSERT INTO course 
                (course_id, section, Instructor_firstname, Instructor_lastname, Instructor_ID, 
                Course_schoolyear, Enrollment_id, Timetable_id) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                val = (course_id, section, instructor_firstname, instructor_lastname, instructor_id, course_schoolyear, enrollment_id, timetable_id)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Course registration record created successfully.")
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
