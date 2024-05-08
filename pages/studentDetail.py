import streamlit as st
import snowflake.connector
import pandas as pd

student_id = st.session_state["student_id"]
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
    # Creating a DataFrame
    invoice_df = pd.DataFrame(result, columns=['student_id', 'student_firstname', 'student_lastname', 'student_gender', 'department_name', 'student_year', 'student_semester', 'student_address', 'student_email', 'student_phone', 'student_dateofbirth'])
    invoice_df['student_dateofbirth'] = invoice_df['student_dateofbirth'].astype(str)
    invoice_df['student_role'] = "Student"
    st.title("Student Detail")


    col1 = st.columns([0.5, 1.8, 5, 5, 1, 1])
    with col1[1]:
        st.image("image/360_F_553796090_XHrE6R9jwmBJUMo9HKl41hyHJ5gqt9oz.jpg", width=200)
    with col1[2]:
        st.title(f"{result[0][1]} {result[0][2]}")
        st.markdown(f"<p style='font-size: 20px; padding-bottom: 120px'><strong>Year: {result[0][5]}</strong></p>", unsafe_allow_html=True)
    with col1[4]:
        Edit = st.button("Edit", key="edit")
        Delete = st.button("Delete", key="delete")
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
        st.markdown(f"<p style='font-size: 25px;'><strong>First Name:</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'><strong>{str(result[0][1])}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 25px;'><strong>Email:</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'><strong>{str(result[0][8])}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 25px;'><strong>Department:</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'><strong>{str(result[0][4])}</strong></p>", unsafe_allow_html=True)
        # st.write(str(result[0][1]))
    with col[2]:
        st.markdown(f"<p style='font-size: 25px;'><strong>Last name:</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'><strong>{str(result[0][2])}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 25px;'><strong>Gender:</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'><strong>{str(result[0][3])}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 25px;'><strong>Semester:</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'><strong>{str(result[0][6])}</strong></p>", unsafe_allow_html=True)
    with col[3]:
        st.markdown(f"<p style='font-size: 25px;'><strong>ID:</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'><strong>{str(result[0][0])}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 25px;'><strong>Birthday:</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'><strong>{str(result[0][10])}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 25px;'><strong>Phonenumber:</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'><strong>{str(result[0][9])}</strong></p>", unsafe_allow_html=True)
    with col[4]:
        st.subheader("Course Detail")
        st.dataframe(invoice_df)
    col = st.columns([0.065, 0.4, 0.4])
    with col[1]:
        st.markdown(f"<p style='font-size: 25px;'><strong>Address:</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px; padding-bottom: 30px'><strong>{str(result[0][7])}</strong></p>", unsafe_allow_html=True)

if __name__ == "__main__":
    Detail()