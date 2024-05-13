import streamlit as st
import snowflake.connector
import pandas as pd
from streamlit_extras.stylable_container import stylable_container

def hide_sidebar():
    st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

student_id = st.session_state["ID"]
def Detail():
    mydb = snowflake.connector.connect(
        user="suchanat",
        password="NuT0863771558-",
        account="PIPWYPD-LO69630",
        warehouse="COMPUTE_WH",
        database="DATABASE",
        schema="PUBLIC"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM student WHERE student_id = %s", (student_id, ))
    result = mycursor.fetchall()
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
    # Creating a DataFrame
    invoice_df = pd.DataFrame(result, columns=['student_id', 'student_firstname', 'student_lastname', 'student_gender', 'department_name', 'student_year', 'student_semester', 'student_address', 'student_email', 'student_phone', 'student_dateofbirth'])
    invoice_df['student_dateofbirth'] = invoice_df['student_dateofbirth'].astype(str)
    invoice_df['student_role'] = "Student"
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

    temp = ""
    if result[0][5] == 1:
        temp = "Freshman"
    elif result[0][5] == 2:
        temp = "Sophomore"
    elif result[0][5] == 3:  
        temp = "Junior"
    elif result[0][5] == 4:
        temp = "Senior"
    
    col1 = st.columns([1, 2, 5, 5, 1, 1])
    
    student_pic = [
        """

        img {
        border-radius: 100%;
        
        }
        
        """
    ]

    col1 = st.columns([0.5, 1.8, 5, 5, 1, 1])
    with col1[1]:
        with stylable_container(
        key="image", 
        css_styles=student_pic,
    ): st.image("image/360_F_553796090_XHrE6R9jwmBJUMo9HKl41hyHJ5gqt9oz.jpg", width=200)
    with col1[2]:
        st.title(f"{result[0][1]} {result[0][2]}")
        st.markdown(f"<p style='font-size: 20px; padding-bottom: 120px; color: #B3B3B3; font-weight: 500;'>Student ({temp})</p>", unsafe_allow_html=True)    
        with col1[4]:
            edit_css = [
                """
                button {
                    border-color: #83A8F5;
                    color: #83A8F5;
                    radius: 10px;
                    background-color: #FFFFFF;
                }
                """,
            ]
            del_css = [
                """
                button {
                    border-color: #F58383;
                    color: #F58383;
                    radius: 10px;
                    background-color: #FFFFFF;
                }
                """,
            ]

            with stylable_container(
                key="button1", 
                css_styles= edit_css,
            ): Edit = st.button("Edit", key="edit")
            
            with stylable_container(
                key="button2", 
                css_styles= del_css,
            ): Delete = st.button("Delete", key="delete")

            
        if Delete:
            mycursor.execute("DELETE FROM student WHERE student_id = %s", (student_id, ))
            mydb.commit()
            st.success("Delete Success")
            st.stop()
        elif Edit:
            st.session_state["page"] = "EditStudent"
            st.switch_page("pages/Editstudent.py")
            st.stop()

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
        st.dataframe(invoice_df)
    col = st.columns([0.065, 0.4, 0.4])
    with col[1]:
        st.markdown(f"<p style='font-size: 20px; color: #B3B3B3'>Address:</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'>{str(result[0][7])}</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    Detail()