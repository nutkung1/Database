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
# from streamlit_extras.stylable_container import stylable_container
# import hydralit_components as hc
from streamlit_navigation_bar import st_navbar
from Home import Home, login, About, CRUD
from streamlit_extras.stylable_container import stylable_container

# Set Streamlit page configuration
st.set_page_config(
    page_title="Streamlit App",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def hide_sidebar():
    st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data(show_spinner=False)
def split_frame(input_df, rows):
    df = [input_df.loc[i : i + rows - 1, :] for i in range(0, len(input_df), rows)]
    return df

load_dotenv()

# SNOWFLAKE
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

# custom_css = """
# <style>
# .stForm {
#     max-width: 400px;
#     margin: 0 auto;
#     padding: 20px;
#     background-color: rgba(255, 255, 255, 1);
#     border-radius: 13px;
# }

# .stTextInput input[type="text"],
# .stTextInput input[type="password"] {
#     width: 100%;
#     padding: 5px;
#     # border: 1px solid #ccc;
#     # border-radius: 5px;
# }

# div.stButton > button:first-child{
#     background-color: rgba(131, 168, 245, 1);
#     color: rgb(255, 255, 255);
#     font-size: 10px;
#     height: 3em;
#     width: 30em;
#     border-radius: 21.5px 21.5px 21.5px 21.5px;
#     margin: 0 auto;
#     display: block;
# }

# div.stButton > button:hover {
#     background-color: #f5f5f5;
#     color: #333333;
# }

# div[data-baseweb="select"] {
#     background-color: #ffffff;
#     border: 1px solid #ced4da;
#     border-radius: 5px;
# }

# div[data-baseweb="select"] > div {
#     padding: 8px 12px;
#     color: #333333;
# }

# div[data-baseweb="select"] svg {
#     fill: #666666;
# }

# div[data-baseweb="select"]:hover {
#     border-color: #6c757d;
# }


# [data-testid="stForm"] {
#     max-height: 10000px;
#     background: White;
#     padding:50px;
# }

# .custom-sidebar {
#     padding: 15px;
#     margin-bottom: 20px;
#     background-color: #374151;
#     border-radius: 10px;
#     box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
# }

# .custom-sidebar:hover {
#     background-color: #4b5563;
#     transition: background-color 0.3s ease;
# }

# .custom-subheader {
#     font-size: 20px;
#     font-weight: bold;
#     margin-bottom: 10px;
#     color: #d1d5db;
# }

# .custom-sort-select select {
#     width: 100%;
#     padding: 10px;
#     margin-top: 5px;
#     margin-bottom: 5px;
#     border: 1px solid #ccc;
#     border-radius: 5px;
#     background-color: #ffffff;
#     color: #333333;
# }
# </style>
# """

# st.markdown(custom_css, unsafe_allow_html=True)


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
for index in range(len(emails)):
    credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}
authenticator = stauth.Authenticate(credentials, cookie_name='Streamlit', key='nutty', cookie_expiry_days=2)

if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = False

# logo_url = "https://static-00.iconduck.com/assets.00/shark-emoji-512x503-7lv5l7l3.png"

# login_header = f"""
# <div style="text-align: center; background-color: rgba(131, 168, 245, 1); color: #ece5f6; padding: 20px; border-radius: 10px;">
#     <div style="display: inline-block; background-color: rgba(131, 168, 245, 1); padding: 10px;">
#         <img src="{logo_url}" alt="Logo" width="100">
#     </div>
#     <div style="margin-top: 20px;">
#         <h2 style='text-align: center; color: #ece5f6; padding: 0px;'>Oceanview College</h2>
#     </div>
# </div>
# """
st.session_state["student_id"] = None
if not st.session_state['authentication_status'] and st.session_state["student_id"] is None:
    # st.markdown(login_header, unsafe_allow_html=True)
    login()
    custom_css1="""<style>    div.stButton > button:first-child{
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
    </style>"""
    st.markdown(custom_css1, unsafe_allow_html=True)
    # hide_sidebar()

email, authenticator_status, username = authenticator.login(
                    fields={'Form name': ':black[Log In]', 'Username': ':blue[Username]', 'Password': ':blue[Password]',
                            'Login': 'Log in'})
if not st.session_state['authentication_status']:
    col = st.columns([5, 4.2, 2])
    with col[2]:
        st.write("Don't have an account? Click button !!!")
        if st.button("Sign Up"):
            st.switch_page("pages/register.py")
    hide_sidebar()

# custom_css = """
# <style>
#     div.stButton > button:first-child{
#     border-color: #83A8F5;
#     color: #83A8F5;
#     radius: 10px;
# }
# </style>
# """
# st.markdown(custom_css, unsafe_allow_html=True)

if st.session_state["authentication_status"]:
    st.session_state["username"] = username
    st.session_state["role"] = role[usernames.index(username)]
    st.sidebar.image("https://static-00.iconduck.com/assets.00/shark-emoji-512x503-7lv5l7l3.png", width=100)
    st.sidebar.subheader(f"Welcome {username}")
    st.sidebar.subheader(f"Role: {role[usernames.index(username)]}")
    # Role ADMIN
    if st.session_state["authentication_status"] and st.session_state["role"] == "admin":
        styles = {
            "nav": {
                "background-color": "rgb(135, 206, 235)",  # Sky Blue
                "padding": "0.3rem 1rem",  # Adjust padding
                "margin": "0",  # Remove any margin
            },
            "div": {
                "max-width": "42rem",
                "margin": "0",  # Remove any margin
            },
            "span": {
                "border-radius": "5rem",
                "color": "rgb(49, 51, 63)",
                "margin": "5 0.325rem",
                "padding": "0.8rem 0.5rem",  # Adjust padding
            },
            "active": {
                "background-color": "rgba(255, 255, 255, 0.25)",
            },
            "hover": {
                "background-color": "rgba(255, 255, 255, 0.35)",
            },
        }
        

        page = st_navbar(["Home", "Student", "Transcript", "Department", "Enrollment", "Course", "CourseName", "Instructor", "Timetable"], styles=styles)
        if page == "Course":
            mycursor.execute("SELECT course_id, section, Instructor_firstname, Instructor_lastname, Instructor_ID, Course_schoolyear, Enrollment_id, Timetable_id FROM Course")
            data = mycursor.fetchall()

            # Creating a DataFrame
            course_df = pd.DataFrame(data, columns=[
                'course_id', 'section', 'Instructor_firstname', 'Instructor_lastname', 'Instructor_ID', 'Course_schoolyear', 'Enrollment_id', 'Timetable_id'
            ])

            # Custom CSS styles
            css_styles = [
                """
                input {
                    color: #83A8F5;
                }
                """,
            ]

            font_css = """
            <style>
            button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
            font-size: 24px;
            }
            </style>
            """

            # Display the management system interface
            col = st.columns([2, 2, 1.5, 1.3, 0.7])
            with col[0]:
                st.title("Course Management System")
            with col[1]:
                with stylable_container(
                    key="sort_search_by",
                    css_styles=css_styles,
                ):
                    sort_field = st.selectbox("Sort based on...", options=course_df.columns)
            with col[2]:
                search_query = st.text_input("Search", "")
            with col[3]:
                sort_direction = st.radio("Sorting", options=["⬆️", "⬇️"], horizontal=True)
            with col[4]:
                st.write(" ")
                if st.button("Add Course"):
                    st.switch_page("pages/addCourse.py")

            st.write(font_css, unsafe_allow_html=True)

            # Sort the dataset
            dataset = course_df.sort_values(by=sort_field, ascending=sort_direction == "⬆️", ignore_index=True)
            dataset[sort_field] = dataset[sort_field].astype(str)

            # Filter the dataset based on search query
            if search_query:
                dataset = dataset[dataset[sort_field].str.contains(search_query, case=False)]
                temp = dataset.index

            # Define custom CSS style
            with st.container(border=True):
                # Table with view details button
                colms = st.columns((1, 1, 1, 1, 1, 1, 1, 1))
                fields = ['course_id', 'section', 'Instructor_firstname', 'Instructor_lastname', 'Instructor_ID', 'Course_schoolyear', 'Enrollment_id', 'Timetable_id']
                for col, field_name in zip(colms, fields):
                    col.write(f"<span style='font-weight: bold;'>{field_name}</span>", unsafe_allow_html=True)

                # Display the data
                if not dataset.empty:
                    for x in range(len(dataset)):
                        col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns((1, 1, 1, 1, 1, 1, 1, 1, 1))
                        col1.write(dataset['course_id'][x])
                        col2.write(dataset['section'][x])
                        col3.write(dataset['Instructor_firstname'][x])
                        col4.write(dataset['Instructor_lastname'][x])
                        col5.write(dataset['Instructor_ID'][x])
                        col6.write(dataset['Course_schoolyear'][x])
                        col7.write(dataset['Enrollment_id'][x])
                        col8.write(dataset['Timetable_id'][x])
                        button_phold = col9.empty()
                        do_action = button_phold.button("👁️ View Details", key=x)

                        if do_action:
                            st.session_state["course_id"] = dataset['course_id'][x]
                            st.switch_page("pages/courseDetail.py")
                else:
                    st.warning("No data matching the search query.")
        elif page == "Instructor":
            mycursor.execute("SELECT * FROM instructor")
            data = mycursor.fetchall()

            # Creating a DataFrame
            columns = ['Instructor_ID', 'Instructor_firstname', 'Instructor_lastname', 'Instructor_gender', 'Instructor_dateofbirth', 'Instructor_phone', 'Instructor_email', 'Instructor_address_1']
            instructor_df = pd.DataFrame(data, columns=columns)

            # Custom CSS styles
            css_styles = [
                """
                input {
                    color: #83A8F5;
                }
                """
            ]

            font_css = """
            <style>
            button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
                font-size: 24px;
            }
            </style>
            """

            # Layout for the management system
            col = st.columns([2, 2, 1.5, 1.3, 0.7])
            with col[0]:
                st.title("Instructor Management System")
            with col[1]:
                with stylable_container(
                    key="sort_search_by",
                    css_styles=css_styles,
                ): 
                    sort_field = st.selectbox("Sort based on...", options=instructor_df.columns)
            with col[2]:
                search_query = st.text_input("Search", "")
            with col[3]:
                sort_direction = st.radio("Sorting", options=["⬆️", "⬇️"], horizontal=True)
            with col[4]:
                st.write(" ")
                if st.button("Add Instructor"):
                    st.switch_page("pages/addInstructor.py")

            st.write(font_css, unsafe_allow_html=True)

            # Sort the dataset
            dataset = instructor_df.sort_values(by=sort_field, ascending=sort_direction == "⬆️", ignore_index=True)

            # Convert the sort_field column to string
            dataset[sort_field] = dataset[sort_field].astype(str)

            # Filter the dataset based on search query
            if search_query:
                dataset = dataset[dataset[sort_field].str.contains(search_query, case=False)]
                temp = dataset.index

            # Define custom CSS style
            with st.container():
                # Table with view details button
                colms = st.columns((1, 1, 1, 1, 1, 1, 1, 1, 1))
                fields = ['Instructor_ID', 'Instructor_firstname', 'Instructor_lastname', 'Instructor_gender', 'Instructor_dateofbirth', 'Instructor_phone', 'Instructor_email', 'Instructor_address_1']
                for col, field_name in zip(colms, fields):
                    # header with middle-sized font
                    col.write(f"<span style='font-weight: bold;'>{field_name}</span>", unsafe_allow_html=True)
                
                # Display the data
                if not dataset.empty:
                    for x in range(len(dataset)):
                        col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns((1, 1, 1, 1, 1, 1, 1, 1, 1))
                        col1.write(dataset['Instructor_ID'][x])
                        col2.write(dataset['Instructor_firstname'][x])
                        col3.write(dataset['Instructor_lastname'][x])
                        col4.write(dataset['Instructor_gender'][x])
                        col5.write(dataset['Instructor_dateofbirth'][x])
                        col6.write(dataset['Instructor_phone'][x])
                        col7.write(dataset['Instructor_email'][x])
                        col8.write(dataset['Instructor_address_1'][x])
                        button_phold = col9.empty()
                        do_action = button_phold.button("👁️ View Details", key=x)

                        if do_action:
                            st.session_state["Instructor_ID"] = dataset['Instructor_ID'][x]
                            st.switch_page("pages/instructorDetail.py")
                else:
                    st.warning("No data matching the search query.")

        elif page == "Department":
            mycursor.execute("SELECT * FROM department")
            data = mycursor.fetchall()

            # Creating a DataFrame
            invoice_df = pd.DataFrame(data, columns=[
                'Department_name', 'program', 
                'instructor_firstname', 'instructor_lastname'
            ])

            # Custom CSS for input styling
            css_styles = [
                """
                input {
                    color: #83A8F5;
                }
                """,
            ]

            # Custom CSS for font styling
            font_css = """
            <style>
            button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
                font-size: 24px;
            }
            </style>
            """

            col = st.columns([2, 2, 1.5, 1.3, 0.7])
            with col[0]:
                st.title("Management System")
            with col[1]:
                with stylable_container(key="sort_search_by", css_styles=css_styles):
                    sort_field = st.selectbox("Sort based on...", options=invoice_df.columns)
            with col[2]:
                search_query = st.text_input("Search", "")
            with col[3]:
                sort_direction = st.radio("Sorting", options=["⬆️", "⬇️"], horizontal=True)
            with col[4]:
                st.write(" ")
                if st.button("Add Instructor"):
                    st.switch_page("pages/instructor.py")

            st.write(font_css, unsafe_allow_html=True)

            # Sort the dataset
            dataset = invoice_df.sort_values(by=sort_field, ascending=sort_direction == "⬆️", ignore_index=True)
            dataset[sort_field] = dataset[sort_field].astype(str)

            # Filter the dataset based on search query
            if search_query:
                dataset = dataset[dataset[sort_field].str.contains(search_query, case=False)]
                temp = dataset.index

            # Custom CSS style for the container
            st.markdown("""
            <style>
            .stContainer {
                border: 1px solid #83A8F5;
                padding: 20px;
                border-radius: 10px;
            }
            </style>
            """, unsafe_allow_html=True)

            with st.container():
                # Table with view details button
                colms = st.columns((1, 1, 1, 1, 1))
                fields = ['Department_name', 'program', 'instructor_firstname', 'instructor_lastname']
                for col, field_name in zip(colms, fields):
                    col.write(f"<span style='font-weight: bold;'>{field_name}</span>", unsafe_allow_html=True)

                if not dataset.empty:
                    for x in range(len(dataset)):
                        col1, col2, col3, col4, col5 = st.columns((1, 1, 1, 1, 1))
                        col1.write(dataset['Department_name'][x])
                        col2.write(dataset['program'][x])
                        # col3.write(dataset['instructor_id'][x])
                        col3.write(dataset['instructor_firstname'][x])
                        col4.write(dataset['instructor_lastname'][x])
                        button_phold = col5.empty()
                        do_action = button_phold.button("👁️ View Details", key=x)

                        if do_action:
                            st.session_state["ID"] = dataset['instructor_id'][x]
                            st.switch_page("pages/instructorDetail.py")
                else:
                    st.warning("No data matching the search query.")
        elif page == "Enrollment":
            mycursor.execute("SELECT * FROM enrollment")
            data = mycursor.fetchall()

            # Creating a DataFrame
            invoice_df = pd.DataFrame(data, columns=[
                'Enrollment_ID', 'enrollment_schoolyear', 'enrollment_course', 
                'enrollment_is_active', 'enrollment_created_at', 'enrollment_created_by', 
                'enrollment_updated_at', 'enrollment_updated_by', 'student_id'
            ])

            # Custom CSS for input styling
            css_styles = [
                """
                input {
                    color: #83A8F5;
                }
                """,
            ]

            # Custom CSS for font styling
            font_css = """
            <style>
            button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
                font-size: 24px;
            }
            </style>
            """

            col = st.columns([2, 2, 1.5, 1.3, 0.7])
            with col[0]:
                st.title("Management System")
            with col[1]:
                with stylable_container(key="sort_search_by", css_styles=css_styles):
                    sort_field = st.selectbox("Sort based on...", options=invoice_df.columns)
            with col[2]:
                search_query = st.text_input("Search", "")
            with col[3]:
                sort_direction = st.radio("Sorting", options=["⬆️", "⬇️"], horizontal=True)
            with col[4]:
                st.write(" ")
                if st.button("Add Enrollment"):
                    st.switch_page("pages/enrollment.py")

            st.write(font_css, unsafe_allow_html=True)

            # Sort the dataset
            dataset = invoice_df.sort_values(by=sort_field, ascending=sort_direction == "⬆️", ignore_index=True)
            dataset[sort_field] = dataset[sort_field].astype(str)

            # Filter the dataset based on search query
            if search_query:
                dataset = dataset[dataset[sort_field].str.contains(search_query, case=False)]
                temp = dataset.index

            # Custom CSS style for the container
            st.markdown("""
            <style>
            .stContainer {
                border: 1px solid #83A8F5;
                padding: 20px;
                border-radius: 10px;
            }
            </style>
            """, unsafe_allow_html=True)

            with st.container():
                # Table with view details button
                colms = st.columns((1, 1, 1, 1, 1, 1))
                fields = ['Enrollment_ID', 'enrollment_schoolyear', 'enrollment_course', 'enrollment_is_active', 'enrollment_created_at']
                for col, field_name in zip(colms, fields):
                    col.write(f"<span style='font-weight: bold;'>{field_name}</span>", unsafe_allow_html=True)
                
                if not dataset.empty:
                    for x in range(len(dataset)):
                        col1, col2, col3, col4, col5, col6 = st.columns((1, 1, 1, 1, 1, 1))
                        col1.write(dataset['Enrollment_ID'][x])
                        col2.write(dataset['enrollment_schoolyear'][x])
                        col3.write(dataset['enrollment_course'][x])
                        col4.write(dataset['enrollment_is_active'][x])
                        col5.write(dataset['enrollment_created_at'][x])
                        button_phold = col6.empty()
                        do_action = button_phold.button("👁️ View Details", key=x)

                        if do_action:
                            st.session_state["ID"] = dataset['Enrollment_ID'][x]
                            st.switch_page("pages/enrollment.py")
                else:
                    st.warning("No data matching the search query.")
                
        elif page == "Home":
            custom_css1="""<style>    div.stButton > button:first-child{
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
            </style>"""
            st.markdown(custom_css1, unsafe_allow_html=True)
            Home() 
        elif page == "Student":
            mycursor.execute("SELECT * FROM student")
            data = mycursor.fetchall()
            # Creating a DataFrame
            invoice_df = pd.DataFrame(data, columns=['ID', 'First Name', 'Last Name', 'Gender', 'Department', 'Year', 'Semester', 'Address', 'E-mail', 'Phone', 'Date of Birth'])
            invoice_df['Date of Birth'] = invoice_df['Date of Birth'].astype(str)
            invoice_df['Role'] = "Student"

            css_styles = [
                """
                input {
                    
                    color: #83A8F5;
                }
                """,
            ]

            font_css = """
            <style>
            button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
            font-size: 24px;
            }
            </style>
            """

            st.write(font_css, unsafe_allow_html=True)
            st.write(font_css, unsafe_allow_html=True)

            # CRUD = st.selectbox("Select an operation", ["Insert", "Update", "Delete"])
            col = st.columns([2, 2,1.5, 1.3,0.7])
            with col[0]:
                st.title("Management System")
            with col[1]:
                st.write(" ")
            with col[2]:
                with stylable_container(
                key="sort_search_by",
                css_styles=css_styles,
            ): sort_field = st.selectbox("Sort based on...", options=invoice_df.columns)
            with col[3]:
                search_query = st.text_input("Search", "")
            with col[4]:
                sort_direction = st.radio("Sorting", options=["⬆️", "⬇️"], horizontal=True)
            st.write(font_css, unsafe_allow_html=True)
            st.write(font_css, unsafe_allow_html=True)
            # Sort the dataset
            dataset = invoice_df.sort_values(by=sort_field, ascending=sort_direction == "⬆️", ignore_index=True)
            # Convert the sort_field column to string
            dataset[sort_field] = dataset[sort_field].astype(str)

            # Filter the dataset based on search query
            if search_query:
                dataset = dataset[dataset[sort_field].str.contains(search_query, case=False)]
                temp = dataset.index

            # Define custom CSS style
                
            with st.container( border=True):
                # Table with view details button
                colms = st.columns((1, 1, 1, 1, 1, 1, 1))
                fields = ['ID', 'First Name', "Last Name", "E-mail", "Department", "Role"]
                for col, field_name in zip(colms, fields):
                    # header with middle-sized font
                    col.write(f"<span style='font-weight: bold;'>{field_name}</span>", unsafe_allow_html=True)
                st.write(font_css, unsafe_allow_html=True)
                
                
                # Display the data
                if not dataset.empty:
                    for x in range(len(dataset)):
                        col1, col2, col3, col4, col5, col6, col7 = st.columns((1, 1, 1, 1, 1, 1, 1))
                        col1.write(dataset['ID'][x])  # email
                        col2.write(dataset['First Name'][x])  # unique ID
                        col3.write(dataset['Last Name'][x])   # email status
                        col4.write(dataset['E-mail'][x])
                        col5.write(dataset['Department'][x])
                        col6.write(dataset['Role'][x])
                        button_phold = col7.empty()
                        do_action = button_phold.button("👁️ View Details", key=x)
                        
                        if do_action:
                            st.session_state["ID"] = dataset['ID'][x]
                            st.switch_page("pages/studentDetail.py")
                else:
                    st.warning("No data matching the search query.")
        elif page == "Transcript":
            mycursor.execute("SELECT * FROM transcript")
            data = mycursor.fetchall()
            # Creating a DataFrame
            invoice_df = pd.DataFrame(data, columns=['Transcript_ID', 'Student_ID', 'Student_year', 'Credit', 'GPAX', 'Transcript_Path'])
            # invoice
            css_styles = [
                """
                input {
                    
                    color: #83A8F5;
                }
                """,
            ]

            font_css = """
            <style>
            button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
            font-size: 24px;
            }
            </style>
            """
            col = st.columns([2, 2,1.5, 1.3,0.7])
            with col[0]:
                st.title("Management System")
            with col[1]:
                with stylable_container(
                key="sort_search_by",
                css_styles=css_styles,
            ): sort_field = st.selectbox("Sort based on...", options=invoice_df.columns)
            with col[2]:
                search_query = st.text_input("Search", "")
            with col[3]:
                sort_direction = st.radio("Sorting", options=["⬆️", "⬇️"], horizontal=True)
            with col[4]:
                st.write(" ")
                if st.button("Add Transcript"):
                    st.switch_page("pages/Transcript.py")
                
            st.write(font_css, unsafe_allow_html=True)
            st.write(font_css, unsafe_allow_html=True)
            # Sort the dataset
            dataset = invoice_df.sort_values(by=sort_field, ascending=sort_direction == "⬆️", ignore_index=True)
            # Convert the sort_field column to string
            dataset[sort_field] = dataset[sort_field].astype(str)

            # Filter the dataset based on search query
            if search_query:
                dataset = dataset[dataset[sort_field].str.contains(search_query, case=False)]
                temp = dataset.index

            # Define custom CSS style
                
            with st.container( border=True):
                # Table with view details button
                colms = st.columns((1, 1, 1, 1, 1, 1, 1))
                fields = ['Transcript_ID', 'Student_ID', 'Student_year', 'Credit', 'GPAX', 'Transcript_Path']
                for col, field_name in zip(colms, fields):
                    # header with middle-sized font
                    col.write(f"<span style='font-weight: bold;'>{field_name}</span>", unsafe_allow_html=True)
                # st.write(font_css, unsafe_allow_html=True)
                
                
                # Display the data
                if not dataset.empty:
                    for x in range(len(dataset)):
                        col1, col2, col3, col4, col5, col6, col7 = st.columns((1, 1, 1, 1, 1, 1, 1))
                        col1.write(dataset['Transcript_ID'][x])  # email
                        col2.write(dataset['Student_ID'][x])  # unique ID
                        col3.write(dataset['Student_year'][x])   # email status
                        col4.write(dataset['Credit'][x])
                        col5.write(dataset['GPAX'][x])
                        col6.write(dataset['Transcript_Path'][x])
                        button_phold = col7.empty()
                        do_action = button_phold.button("👁️ View Details", key=x)
                        
                        if do_action:
                            st.session_state["ID"] = dataset['ID'][x]
                            st.switch_page("pages/studentDetail.py")
                else:
                    st.warning("No data matching the search query.")



    #ROLE Student
    elif st.session_state["authentication_status"] and st.session_state["role"] == "student":
        styles = {
            "nav": {
                "background-color": "rgb(135, 206, 235)",  # Sky Blue
            },
            "div": {
                "max-width": "32rem",
            },
            "span": {
                "border-radius": "1rem",
                "color": "rgb(49, 51, 63)",
                "margin": "0 0.125rem",
                "padding": "0.4375rem 0.625rem",
            },
            "active": {
                "background-color": "rgba(255, 255, 255, 0.25)",
            },
            "hover": {
                "background-color": "rgba(255, 255, 255, 0.35)",
            },
        }
        page = st_navbar(["Home", "Detail", "Course", "About Us"], styles=styles)
        custom_css1="""<style>    div.stButton > button:first-child{
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
            </style>"""
        st.markdown(custom_css1, unsafe_allow_html=True)
        
        if page == "Home":
            Home() 
        elif page == "Detail":
            mycursor.execute("SELECT student_id FROM student WHERE student_email = %s", (st.session_state["username"], ))
            result = mycursor.fetchall()
            student_id = result[0][0]

            mycursor.execute("SELECT * FROM student WHERE student_id = %s", (student_id, ))
            result = mycursor.fetchall()
            # Creating a DataFrame

            temp = ""
            if result[0][5] == 1:
                temp = "Freshman"
            elif result[0][5] == 2:
                temp = "Sophomore"
            elif result[0][5] == 3:  
                temp = "Junior"
            elif result[0][5] == 4:
                temp = "Senior"

            invoice_df = pd.DataFrame(result, columns=['student_id', 'student_firstname', 'student_lastname', 'student_gender', 'department_name', 'student_year', 'student_semester', 'student_address', 'student_email', 'student_phone', 'student_dateofbirth'])
            invoice_df['student_dateofbirth'] = invoice_df['student_dateofbirth'].astype(str)
            invoice_df['student_role'] = "Student"
            data = {
                'course_id': [101, 102, 103, 104, 105],
                'course_name': ['CSE101', 'MAT202', 'BIO303', 'CHE404', 'PHY505'],
                'section': [1, 2, 1, 3, 2],
                'Instructor_firstname': ['Smith', 'Johnson ', 'Lee', 'Brown', 'Williams'],
                'Instructor_lastname': ['Doe', 'Smith', 'Brown', 'White', 'Black'],
                'Instructor_ID': [101, 102, 103, 104, 105],
                # 'Course_schoolyear': [2021, 2021, 2022, 2022, 2023],
                # 'Enrollment_id': [301, 302, 303, 304, 305],
                # 'Timetable_id': [401, 402, 403, 404, 405]
            }

            # Create DataFrame
            course_df = pd.DataFrame(data)

            css = """
                    <style>
                        .title-container {
                            padding-bottom: 20px; /* Adjust the value as needed */
                            padding-left: 90px;
                        }
                    </style>
                    """

            st.markdown(css, unsafe_allow_html=True)
            st.markdown('<div class="title-container"> <h1>Student Detail</h1>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)


            col1 = st.columns([1, 2, 5, 5, 1, 1])
            student_pic = [
                """

                img {
                border-radius: 100%;
                
                }
                
                """
            ]
            with col1[1]:
                with stylable_container(
                key="image", 
                css_styles=student_pic,
            ): st.image("image/360_F_553796090_XHrE6R9jwmBJUMo9HKl41hyHJ5gqt9oz.jpg", width=200)
            with col1[2]:
                st.title(f"{result[0][1]} {result[0][2]}")
                st.markdown(f"<p style='font-size: 20px; padding-bottom: 120px; color: #B3B3B3; font-weight: 500;'>Student ({temp})</p>", unsafe_allow_html=True)    
            col = st.columns([0.1, 0.2, 0.2, 0.2, 0.6])
            with col[1]:
                st.markdown(f"<p style='font-size: 20px; color: #B3B3B3'>First Name:</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'>{str(result[0][1])}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px; color: #B3B3B3'>Email:</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'>{str(result[0][8])}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px; color: #B3B3B3'>Department:</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'>{str(result[0][4])}</p>", unsafe_allow_html=True)
            with col[2]:
                st.markdown(f"<p style='font-size: 20px; color: #B3B3B3'>Last name:</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'>{str(result[0][2])}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px; color: #B3B3B3'>Gender:</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'>{str(result[0][3])}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px; color: #B3B3B3'>Semester:</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'>{str(result[0][6])}</p>", unsafe_allow_html=True)
            with col[3]:
                st.markdown(f"<p style='font-size: 20px; color: #B3B3B3'>ID:</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'>{str(result[0][0])}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px; color: #B3B3B3'>Birthday:</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'>{str(result[0][10])}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px; color: #B3B3B3'>Phone Number:</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'>{str(result[0][9])}</p>", unsafe_allow_html=True)

            with col[4]:
                st.subheader("Course Detail")
                st.table(course_df)
            col = st.columns([0.065, 0.4, 0.4])
            with col[1]:
                st.markdown(f"<p style='font-size: 20px; color: #B3B3B3'>Address:</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'>{str(result[0][7])}</p>", unsafe_allow_html=True)
        elif page == "Course":
            # Sample course data
            course_data = {
                'Course ID': ['CSE101', 'MAT202', 'BIO303', 'CHE404', 'PHY505', 'ECO606', 'PSY707', 'ENG808', 'HIS909'],
                'Course Name': ['Introduction to Computer Science', 'Linear Algebra', 'Biology Fundamentals',
                                'Chemistry Essentials', 'Physics Principles', 'Economics for Beginners',
                                'Psychology Basics', 'Advanced English Literature', 'History of Civilization'],
                'Instructor': ['Prof. Smith', 'Dr. Johnson', 'Prof. Lee', 'Dr. Brown', 'Prof. Williams',
                            'Dr. Taylor', 'Prof. Martinez', 'Dr. Anderson', 'Prof. Thompson'],
                'Instructor_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109],  # Example Instructor IDs
                'Description': ['A course covering the basics of computer science.',
                                'A course covering fundamental concepts in linear algebra.',
                                'An overview of basic concepts in biology and biochemistry.',
                                'Essential principles of chemistry for beginners for junior.',
                                'Introduction to fundamental principles of physics.',
                                'An introductory course to the basics of economics.',
                                'Understanding the fundamentals of psychology.',
                                'Exploration of advanced English literary works.',
                                'A journey through the history of human civilization.'],
                'Image URL': ['https://images.unsplash.com/photo-1610563166150-b34df4f3bcd6?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y29tcHV0ZXIlMjBzY2llbmNlfGVufDB8fDB8fHww',
                            'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Linear_subspaces_with_shading.svg/1200px-Linear_subspaces_with_shading.svg.png',
                            'https://img.freepik.com/free-vector/science-lab-objects_23-2148488312.jpg?size=338&ext=jpg&ga=GA1.1.1224184972.1715126400&semt=sph',
                            'https://cdn.britannica.com/86/193986-050-7B2DBB6A/ball-and-stick-model-structure-atoms.jpg',
                            'https://media.istockphoto.com/id/936903524/vector/blackboard-inscribed-with-scientific-formulas-and-calculations-in-physics-and-mathematics-can.jpg?s=612x612&w=0&k=20&c=sRLsJbHUVOYvZ_M16hti4fF9NM0RysfjAPUQrCJ8o4U=',
                            'https://www.ntu.edu.sg/images/librariesprovider124/default-album/general-images/sss-webrevamp/sss_econs_coinsb6efd5c0-2a2a-4c0e-aa83-669f44598aea.jpg?Status=Master&sfvrsn=ee6510c_3',
                            'https://www.udc.edu/social-udc/wp-content/uploads/sites/24/2018/03/Importance-of-Psychology_UDC.jpg',
                            'https://heritageinstitute.in/wp-content/uploads/2019/01/Advanced-English.png',
                            'https://dualcreditathome.com/wp-content/uploads/2014/02/history.jpg'],
                'Course_schoolyear': [2023, 2023, 2024, 2024, 2024, 2023, 2023, 2024, 2023],  # Example school years
                'Timetable': ['10.30-12.30', '13.00-15.00', '09.00-11.00', '10.30-12.30',
                            '13.00-15.00', '09.00-11.00', '10.30-12.30', '13.00-15.00', '09.00-11.00']  # Example Timetable
            }
            # Create a DataFrame from the course data
            df_courses = pd.DataFrame(course_data)
            # Define header background image and text
            header_bg_image = 'https://cdn.discordapp.com/attachments/1081112018360221696/1237724333326204928/asasdqweq.JPG?ex=663cb01c&is=663b5e9c&hm=950f617aa089f3d67c5e26c60c3e92c6dccd389fe9c86bbfefbd907a2dd3d4cf&'
            header_text = """ 
            <h1 style="color: white; text-align: center; margin-left: 40px; margin-top: 40px;">Helping You Grow</h1>
            <br>
            <h5 style="color: white; font-weight: 100; text-align: center; margin-left: 40px; margin-top: 10px;">Learning is the compass that guides us through the uncharted territories of knowledge</h5>
            <h5 style="color: white; font-weight: 100; text-align: center; margin-left: 40px; margin-top: 10px;">illuminating our path with the brilliance of understanding.</h5>
            """

            # Page title
            # Display header with background image and text
            st.markdown(
                f"""
                <div style="padding: 0; background-size: cover;">
                    <div style="background-image: url('{header_bg_image}'); filter: blur(2px); position: absolute; top: 0; left: 0; width: 100%; height: 350px; background-size: contain;"></div>
                    <div style="position: relative; z-index: 0; margin-top: 50px; margin-bottom: 150px;">{header_text}</div>
                </div>""",unsafe_allow_html=True
            )

            with st.container(border=True,height=1000):
                st.markdown(f"""<h2 style=" text-align: center; margin-bottom:30px;">Active courses now</h2>""", unsafe_allow_html=True)
                col1, col2, col3= st.columns(3)
                
                for index, course in df_courses.iterrows():
                    with eval(f"col{index % 3+ 1}"):  # Alternate between the four columns
                        col4, col5, col6= st.columns(3)
                        with col5:
                            st.markdown(
                                f"""<div style="height: 133px; width: 200px; overflow: hidden; border-radius: 15px; margin-top:20px;">
                                    <img src="{course['Image URL']}" alt="{course['Course Name']}" style="width: 100%; height: 100%; object-fit: cover;">
                                </div>""",
                                unsafe_allow_html=True
                            )
                        st.markdown(f"""<h4 style=" text-align: center; margin-bottom:10px;">{course['Course Name']}</h4>""", unsafe_allow_html=True)
                        with st.container(border=True,):
                            st.write(f"**Course ID:** {course['Course ID']}")
                            st.write(f"**Instructor:** {course['Instructor']} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Instructor ID:** {course['Instructor_ID']}")
                            st.write(f"**Description:** {course['Description']}")
                            st.write(f"**Course School Year:** {course['Course_schoolyear']}")
                            st.write(f"**Timetable:** {course['Timetable']}")
                            st.button(f"**Enrollment** {course['Course ID']}")
        elif page == "About Us":
            About()


        # student_df = invoice_df.drop(columns=['password'])
        # ui.table(student_df)
    authenticator.logout("Logout", "sidebar")

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

