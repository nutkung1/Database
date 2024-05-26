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
    with st.form(key="transcript_register"):
        st.title("Create Transcript Record")
        st.write("Please fill out the transcript form below:")

        col1, col2 = st.columns(2)

        with col1:
            transcript_id = st.number_input("Transcript ID", min_value=1)
            student_id = st.number_input("Student ID", min_value=1)
            credit = st.number_input("Credit", min_value=0)
            gpax = st.number_input("GPAX", min_value=0.0, format="%.2f")

        with col2:
            student_year = st.number_input("Student Year", min_value=1)
            transcript_path = st.text_input("Transcript Path")

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
            if not all([transcript_id, student_id, credit, gpax, transcript_path]):
                st.error("Please fill in all fields.")
            elif not agreement:
                st.error("Please agree to the Terms and Conditions.")
            else:
                # Inserting data into the transcript table
                sql = "INSERT INTO transcript (transcript_id, student_id, student_year, credit, gpax, transcript_path) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (transcript_id, student_id, student_year, credit, gpax, transcript_path)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Transcript record created successfully.")
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

