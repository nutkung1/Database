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
    with st.form(key="register"):
        st.title("Sign Up !!!")
        st.write("Please fill out the registration form below:")

        col1, col2 = st.columns(2)

        with col1:
            first_name = st.text_input("First Name")
            email = st.text_input("Email")
            birthday = st.date_input("Birthday")
            # student_year = st.number_input("Year", placeholder="Year", key="stu_year", min_value=1, max_value=4)
            faculty = st.text_input("Department")
            role = st.selectbox("You are...", ["Student", "Teacher"])
            password = st.text_input("Password", type="password")
            if role == "Student":
                student_semester = st.number_input("Semester", placeholder="Semester", key="stu_semester", min_value=1, max_value=2)

        with col2:
            last_name = st.text_input("Last Name")
            id_number = st.text_input("ID Number")
            address = st.text_input("Address")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            # student_semester = st.number_input("Semester", placeholder="Semester", key="stu_semester", min_value=1, max_value=2)
            phone_number = st.text_input("Phone Number")
            confirm_password = st.text_input("Confirm Password", type="password")
            if role == "Student":
                student_year = st.number_input("Year", placeholder="Year", key="stu_year", min_value=1, max_value=4)

        agreement = st.checkbox("I agree to all statements in [Terms and Conditions](http://www.example.com/terms)", value=False, key="agree")

        # Center align the button
        # st.markdown("""
        # <style>
        # .stButton>button {
        #     border-radius: 20px;
        #     background-color: #83A8F5;
        #     width: 100%;
        #     text-align: center;
        # }
        # .center {
        #     text-align: center;
        # }
        # a {
        #     color: #83A8F5;
        # }
        # </style>
        # """, unsafe_allow_html=True)
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
                    mycursor.execute("SELECT MAX(student_id) FROM student")
                    result = mycursor.fetchone()[0]
                    next_student_id = result + 1 if result is not None else 1
                    sql = "INSERT INTO student (student_id, student_firstname, student_lastname, student_gender, department_name, student_year, student_semester, student_address, student_email, student_phone, student_dateofbirth) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    val = (next_student_id, first_name, last_name, gender, faculty, student_year, student_semester, address, email, phone_number, birthday)
                    mycursor.execute(sql, val)
                    mydb.commit()   
                    sql = "INSERT INTO authenticator (email, password, role) VALUES (%s, %s, %s)"
                    val = (email, password, role)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.rerun()
                elif role == "Teacher":
                    pass
        
        # Center align the link
        col = st.columns(3)
        with col[1]:
            st.markdown("""
            <div class="center">
                <a href="http://www.example.com" style="color: #83A8F5;">Already registered? Log in here.</a>
            </div>
            """, unsafe_allow_html=True)
        # st.switch_page("app.py")
        st.title(" ")

registration_form()
