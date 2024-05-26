import streamlit as st
import pandas as pd
import snowflake.connector
import os

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

# Connect to Snowflake
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
# Sample data for the DataFrame
data = {
    'Transcript_ID': [1, 2, 3],
    'Student_ID': [101, 102, 103],
    'Student_year': [2020, 2021, 2022],
    'Credit': [15, 16, 17],
    'GPAX': [3.5, 3.6, 3.7],
    'Transcript_Path': ['path1', 'path2', 'path3']
}
invoice_df = pd.DataFrame(data)

def main():
    # st.write("Select a transcript to edit from the dropdown below:")

    # Dropdown to select a transcript by Transcript_ID
    # transcript_id = st.selectbox("Select Transcript ID", invoice_df['Transcript_ID'])

    # # Fetch the selected transcript details
    # transcript = invoice_df[invoice_df['Transcript_ID'] == transcript_id].iloc[0]

    with st.form(key="edit_transcript_form", border=True):
        st.title("Edit Transcript Details")
        st.write("Select a transcript to edit from the dropdown below:")
        transcript_id = st.selectbox("Select Transcript ID", invoice_df['Transcript_ID'])

    # Fetch the selected transcript details
        transcript = invoice_df[invoice_df['Transcript_ID'] == transcript_id].iloc[0]
        col1, col2 = st.columns(2)

        with col1:
            student_id = st.number_input("Student ID")
            student_year = st.number_input("Student Year")
            credit = st.number_input("Credit")
        
        with col2:
            gpax = st.number_input("GPAX", value=transcript['GPAX'], min_value=0.0, max_value=4.0, step=0.01)
            transcript_path = st.text_input("Transcript Path", value=transcript['Transcript_Path'])

        submit_button = st.form_submit_button("Submit")
        if submit_button:
            if not all([transcript_id, student_id, student_year, credit, gpax, transcript_path]):
                st.error("Please fill in all fields.")
            else:
                sql = """
                UPDATE transcripts
                SET 
                    Student_ID = %s,
                    Student_year = %s,
                    Credit = %s,
                    GPAX = %s,
                    Transcript_Path = %s
                WHERE 
                    Transcript_ID = %s
                """
                val = (student_id, student_year, credit, gpax, transcript_path, transcript_id)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Transcript details updated successfully.")
                st.experimental_rerun()

# Calling the main function
if __name__ == "__main__":
    main()
