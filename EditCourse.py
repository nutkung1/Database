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

# Assuming admin_id is stored in the session state
admin_id = 1  # Replace with st.session_state["admin_id"] if needed

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

hide_sidebar()

# Fetch admin details
def get_admin_details(admin_id):
    sql = "SELECT Admin_firstname, Admin_lastname, Admin_gender, Admin_dateofbirth, Admin_phone, Admin_email, Admin_address FROM Admin WHERE Admin_ID = %s"
    mycursor.execute(sql, (admin_id,))
    return mycursor.fetchone()

admin_details = get_admin_details(admin_id)

if admin_details:
    admin_firstname, admin_lastname, admin_gender, admin_dateofbirth, admin_phone, admin_email, admin_address = admin_details

    with st.form(key="edit_admin_form"):
        st.title("Edit Admin Details")
        col1, col2 = st.columns(2)

        with col1:
            admin_firstname = st.text_input("First Name", value=admin_firstname)
            admin_lastname = st.text_input("Last Name", value=admin_lastname)
            admin_gender = st.selectbox("Gender", ["Male", "Female", "Others"], index=["Male", "Female", "Others"].index(admin_gender))
            admin_dateofbirth = st.date_input("Date of Birth", value=admin_dateofbirth)

        with col2:
            admin_phone = st.text_input("Phone Number", value=admin_phone)
            admin_email = st.text_input("Email", value=admin_email)
            admin_address = st.text_area("Address", value=admin_address)

        submit_button = st.form_submit_button("Update Admin")

        if submit_button:
            if not all([admin_firstname, admin_lastname, admin_gender, admin_dateofbirth, admin_phone, admin_email, admin_address]):
                st.error("Please fill in all fields.")
            else:
                sql = """
                UPDATE Admin
                SET 
                    Admin_firstname = %s,
                    Admin_lastname = %s,
                    Admin_gender = %s,
                    Admin_dateofbirth = %s,
                    Admin_phone = %s,
                    Admin_email = %s,
                    Admin_address = %s
                WHERE 
                    Admin_ID = %s
                """
                val = (admin_firstname, admin_lastname, admin_gender, admin_dateofbirth, admin_phone, admin_email, admin_address, admin_id)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Admin details updated successfully.")
                st.experimental_rerun()
else:
    st.error("Admin details not found.")
