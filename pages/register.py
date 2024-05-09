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

def registration_form():
    mydb = snowflake.connector.connect(
        user="suchanat",
        password="NuT0863771558-",
        account="PIPWYPD-LO69630",
        warehouse="COMPUTE_WH",
        database="DATABASE",
        schema="PUBLIC"
    )
    mycursor = mydb.cursor()
    with st.form(key="register"):
        st.title("Sign Up !!!")
        st.write("Please fill out the registration form below:")

        col1, col2 = st.columns(2)

        with col1:
            first_name = st.text_input("First Name")
            email = st.text_input("Email")
            birthday = st.date_input("Birthday")
            # student_year = st.number_input("Year", placeholder="Year", key="stu_year", min_value=1, max_value=4)
            address = st.text_input("Address")
            faculty = st.text_input("Department")
            password = st.text_input("Password", type="password")

        with col2:
            last_name = st.text_input("Last Name")
            id_number = st.text_input("ID Number")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            # student_semester = st.number_input("Semester", placeholder="Semester", key="stu_semester", min_value=1, max_value=2)
            phone_number = st.text_input("Phone Number")
            role = st.selectbox("You are...", ["Student", "Teacher"])
            confirm_password = st.text_input("Confirm Password", type="password")

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
        hide_sidebar()

        submit_button = st.form_submit_button("Register")
        if submit_button:
            if not all([first_name, email, birthday, address, faculty, password, last_name, id_number, phone_number]):
                st.error("Please fill in all fields.")
            elif not agreement:
                st.error("Please agree to the Terms and Conditions.")
            elif password != confirm_password:
                st.error("Passwords do not match. Please try again.")
            else:
                if role == "Student":
                    student_year = st.number_input("Year", placeholder="Year", key="stu_year", min_value=1, max_value=4)
                    student_semester = st.number_input("Semester", placeholder="Semester", key="stu_semester", min_value=1, max_value=2)
                    mycursor.execute("SELECT MAX(student_id) FROM student")
                    result = mycursor.fetchone()[0]
                    next_student_id = result + 1 if result is not None else 1
                    sql = "INSERT INTO student (student_id, student_firstname, student_lastname, student_gender, department_name, student_year, student_semester, student_address, student_email, student_phone, student_dateofbirth) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    val = (next_student_id, first_name, last_name, gender, faculty, student_year, student_semester, address, email, phone_number, birthday)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.rerun()
                elif role == "Teacher":
                    pass
        
        # Center align the link
        st.markdown("""
        <div class="center">
            <a href="http://www.example.com" style="color: #83A8F5;">Already registered? Log in here.</a>
        </div>
        """, unsafe_allow_html=True)
        # st.switch_page("app.py")
        st.title(" ")

registration_form()
