import streamlit as st
import snowflake.connector
from streamlit_extras.stylable_container import stylable_container

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

def login():
    logo_url = "https://static-00.iconduck.com/assets.00/shark-emoji-512x503-7lv5l7l3.png"

    login_header = f"""
    <div style="text-align: center; background-color: rgba(131, 168, 245, 1); color: #ece5f6; padding: 20px; border-radius: 10px;">
        <div style="display: inline-block; background-color: rgba(131, 168, 245, 1); padding: 10px;">
            <img src="{logo_url}" alt="Logo" width="100">
        </div>
        <div style="margin-top: 20px;">
            <h2 style='text-align: center; color: #ece5f6; padding: 0px;'>Oceanview College</h2>
        </div>
    </div>
    """
    st.markdown(login_header, unsafe_allow_html=True)
def Home():
    # st.title("Home")
    # st.write("Welcome to the Home Page")
    image_url = 'https://www.troy.edu/_assets/about-us/_images/wide-quad-new.jpg'

    # Define the text to overlay on the image
    overlay_text = "Overlay Text"

    # Define CSS for centering and blurring the image
    css = """
        <style>
            .blur {
                filter: blur(1px); /* Adjust the blur intensity as needed */
                border-radius: 20px;
                
            }
            .centered {
                position: absolute;
                top: 60%;
                left: 35%;
                transform: translate(-50%, -50%);
                color: white; /* Color of the overlay text */
                font-size: 24px; /* Adjust the font size as needed */
                font-weight: bold;
            }
            #rectangle{
                width:30%;
                height:600px;
                border-radius: 20px 0px 0px 20px;
                position: absolute;
                top: 50%;
                left: 15%;
                transform: translate(-50%, -50%);
                
                opacity: 0.8;
            }
            .head {
                color:white;
                width:30%;
            }
            .headsub {
                color:white;
                width:40%;
                font-weight: 20px;
                
            }
        </style>
    """
    logo_url = "https://static-00.iconduck.com/assets.00/shark-emoji-512x503-7lv5l7l3.png"
    # Display the image with CSS styling
    st.markdown(
        f"""
        {css}
        <div style='position:relative;'>
            <img src='{image_url}' class='blur' width='100%' height='600px'/>
            <div id="rectangle"></div>
            <div class='centered'>
                <h1 class="head">We've Been Expecting You </h1>
                <p class="headsub">Welcome to Oceanview, your gateway to an extraordinary educational journey! Step into our vibrant community where every corner is infused with opportunities for growth, discovery, and connection.
                    Picture yourself immersed in our dynamic classrooms, where innovative teaching methods ignite your curiosity and transform your perspective. Engage in captivating discussions with passionate professors who are not just educators but mentors, guiding you towards unlocking your full potential.
                    But it doesn't stop there. Oceanview isn't just about academics; it's a place where lifelong friendships are forged over late-night study sessions and spontaneous adventures. 
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f"""<br></br>""",unsafe_allow_html=True)
    # News
    st.header("News")     

    # Define image sources
    openhouse_src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpIVvi08-eN-zixhDrJUT1TQMFPV6UJ2s29_oO8eAj_g&s'
    university_sport_src = 'https://www.kmutt.ac.th/wp-content/uploads/2024/01/SCM15612-1200x800.jpg'
    Petchre_Pra_Jom_src = 'https://admission.kmutt.ac.th/stocks/discover_banner/c690x390/oa/ej/fr2xoaej6t/kmutt.png'
    comcamp_src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2sEAtlMynbPAEqDQm_vAKMDIhuFZYbT9FPWDczlzZJQ&s'
    orientation_src = 'https://cdn.zipeventapp.com/images/events/3F5C62F5-821F-4D6F-9B5E-AE7D31D85BCC/FD3A1F59-AE42-4D1E-94DE-79D024260744.jpg'
    # Construct HTML strings for each image
    openhouse_img = f'<img src="{openhouse_src}" alt="openhouse" width="300" height="250" style="margin-right: 10px;">'
    university_sport_img = f'<img src="{university_sport_src}" alt="university_sport" width="300" height="250" style="margin-right: 10px;">'
    Petchre_Pra_Jom_img = f'<img src="{Petchre_Pra_Jom_src}" alt="Petchre_pra_jom" width="500" height="250" style="margin-right: 10px;">'
    comcamp_img = f'<img src="{comcamp_src}" alt="comcamp" width="300" height="250" style="margin-right: 10px;">'
    orientation_img = f'<img src="{orientation_src}" alt="comcamp" width="300" height="250" style="margin-right: 10px;">'

    # Combine images into a single HTML string with a containing div
    news_pictures = f'<div style="display: flex; overflow-x: auto; white-space: nowrap;">{openhouse_img}{university_sport_img}{Petchre_Pra_Jom_img}{comcamp_img}{orientation_img}</div>'
    st.markdown(news_pictures, unsafe_allow_html=True)
    st.markdown(f"""<br></br>""",unsafe_allow_html=True)
    # Teaching schedule
    st.header("Teaching Schedule")

    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        button_mon = st.button("Monday")
    with col2:
        button_tue = st.button("Tuesday")
    with col3:
        button_wed = st.button("Wednesday")
    with col4:
        button_thu = st.button("Thursday")
    with col5:
        button_fri = st.button("Friday")

    if button_mon :
        col1,col2 = st.columns([1,9])
        with col1:
            st.markdown('<div style="font-size: 16px; color: blue;"><br><br>9:30-12:30</div>', unsafe_allow_html=True)
            st.markdown('<div style="font-size: 16px; color: blue;"><br><br><br><br>13:30-16:30</div>', unsafe_allow_html=True)
        with col2:
            container = st.container()
            container.markdown("""<div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            CPE241 <br> Linear Algebra </div>""", unsafe_allow_html=True)
            container = st.container()
            container.markdown("""<div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            - <br> - </div>""", unsafe_allow_html=True)

    elif button_tue :
        col1,col2 = st.columns([1,9])
        with col1:
            st.markdown('<div style="font-size: 16px; color: blue;"><br><br>9:30-12:30</div>', unsafe_allow_html=True)
            st.markdown('<div style="font-size: 16px; color: blue;"><br><br><br><br>13:30-16:30</div>', unsafe_allow_html=True)

        with col2:
            container = st.container()
            container.markdown("""<div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            CPE241 <br> Introduction to Computer Science </div>""", unsafe_allow_html=True)
            container = st.container()
            container.markdown("""
            <div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            CPE232 <br> Linear Algebra </div>""", unsafe_allow_html=True)

    elif button_wed :
        col1,col2 = st.columns([1,9])
        with col1:
            st.markdown('<div style="font-size: 16px; color: blue;"><br><br>9:30-12:30</div>', unsafe_allow_html=True)
            st.markdown('<div style="font-size: 16px; color: blue;"><br><br><br><br>13:30-16:30</div>', unsafe_allow_html=True)

        with col2:
            container = st.container()
            container.markdown("""<div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            STA302 <br> Biology Fundamentals </div>""", unsafe_allow_html=True)
            container = st.container()
            container.markdown("""
            <div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            CPE223 <br> Chemistry Essentials </div>""", unsafe_allow_html=True)

    elif button_thu :
        col1,col2 = st.columns([1,9])
        with col1:
            st.markdown('<div style="font-size: 16px; color: blue;"><br><br>9:30-12:30</div>', unsafe_allow_html=True)
            st.markdown('<div style="font-size: 16px; color: blue;"><br><br><br><br>13:30-16:30</div>', unsafe_allow_html=True)

        with col2:
            container = st.container()
            container.markdown("""<div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            STA302 <br> Physics Principles </div>""", unsafe_allow_html=True)
            container = st.container()
            container.markdown("""
            <div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            GEN111 <br> Introduction to Computer Science </div>""", unsafe_allow_html=True)

    elif button_fri :
        col1,col2 = st.columns([1,9])
        with col1:
            st.markdown('<div style="font-size: 16px; color: blue;"><br><br>9:30-12:30</div>', unsafe_allow_html=True)
            st.markdown('<div style="font-size: 16px; color: blue;"><br><br><br><br>13:30-16:30</div>', unsafe_allow_html=True)

        with col2:
            container = st.container()
            container.markdown("""<div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            STA302 <br> Biology Fundamentals </div>""", unsafe_allow_html=True)
            container = st.container()
            container.markdown("""
            <div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            GEN111 <br> Introduction to Computer Science </div>""", unsafe_allow_html=True)

def CRUD():
    custom_css = """
    <style>
        div.stButton > button:first-child{
        border-color: #83A8F5;
        color: #83A8F5;
        radius: 10px;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
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
                
                button_type = "👁️ View Details"
                button_phold = col7.empty()  # create a placeholder
                do_action = button_phold.button(button_type, key=x)
                
                if do_action:
                    # st.empty()
                    # st.experimental_set_query_params(detail="pages/student_detail", student_id=dataset['student_id'][x])
                    st.session_state["ID"] = dataset['ID'][x]
                    st.switch_page("pages/studentDetail.py")
        else:
            st.warning("No data matching the search query.")

# def Home():
#     # st.title("Home")
#     # st.write("Welcome to the Home Page")
#     # st.image("image/kmutt-websitelogo-01-scaled.jpg", width=600)

#     # News
#     st.title("News")     

#     # Define image sources
#     openhouse_src = 'https://scontent.fbkk22-3.fna.fbcdn.net/v/t39.30808-6/322296094_565819111642809_6127783231039668742_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=5f2048&_nc_ohc=MMyyxuA_gJoQ7kNvgE6v6IA&_nc_ht=scontent.fbkk22-3.fna&oh=00_AfATU6shTCR2a8saS8TMxNJka5O6qxjeB562yzvOTU9Hhw&oe=6642B780'
#     university_sport_src = 'https://www.kmutt.ac.th/wp-content/uploads/2024/01/SCM15612-1200x800.jpg'
#     Petchre_Pra_Jom_src = 'https://scontent.fbkk22-7.fna.fbcdn.net/v/t39.30808-6/305927187_567352885190048_1863554905914937964_n.png?stp=dst-png_p720x720&_nc_cat=107&ccb=1-7&_nc_sid=5f2048&_nc_ohc=eiykJzl3WgkQ7kNvgFc36pn&_nc_ht=scontent.fbkk22-7.fna&oh=00_AfCx3AkgdHWFCW9_5-O18eMkjwCxT6LYs-yyFr_YwKgtAw&oe=664299A9'
#     comcamp_src = 'https://scontent.fbkk22-6.fna.fbcdn.net/v/t39.30808-1/435764432_1101676158081572_6864015543597168996_n.jpg?stp=dst-jpg_p480x480&_nc_cat=102&ccb=1-7&_nc_sid=5f2048&_nc_ohc=WFZ4TCoUp2oQ7kNvgHkJImv&_nc_ht=scontent.fbkk22-6.fna&oh=00_AfCXurSMULaKSZP-50cahjkNbgeFL9BwUh5s3_ml4yF9kw&oe=6642BEB9'
#     orientation_src = 'https://media.discordapp.net/attachments/1081112018360221696/1237777829580640277/orientation.jpg?ex=663ce1ef&is=663b906f&hm=0716080b9185b809037fddb341594fd81d6d92ed30fd3b6bfbf0ab51dcf118f9&=&format=webp&width=718&height=478'

#     # Construct HTML strings for each image
#     openhouse_img = f'<img src="{openhouse_src}" alt="openhouse" width="300" height="250" style="margin-right: 10px;">'
#     university_sport_img = f'<img src="{university_sport_src}" alt="university_sport" width="300" height="250" style="margin-right: 10px;">'
#     Petchre_Pra_Jom_img = f'<img src="{Petchre_Pra_Jom_src}" alt="Petchre_pra_jom" width="500" height="250" style="margin-right: 10px;">'
#     comcamp_img = f'<img src="{comcamp_src}" alt="comcamp" width="300" height="250" style="margin-right: 10px;">'
#     orientation_img = f'<img src="{orientation_src}" alt="comcamp" width="300" height="250" style="margin-right: 10px;">'

#     # Combine images into a single HTML string with a containing div
#     news_pictures = f'<div style="display: flex; overflow-x: auto; white-space: nowrap;">{openhouse_img}{university_sport_img}{Petchre_Pra_Jom_img}{comcamp_img}{orientation_img}</div>'
#     st.markdown(news_pictures, unsafe_allow_html=True)

#     # Teaching schedule
#     st.header("Teaching Schedule")

#     col1,col2,col3,col4,col5 = st.columns(5)
#     with col1:
#         button_mon = st.button("Monday")
#     with col2:
#         button_tue = st.button("Tuesday")
#     with col3:
#         button_wed = st.button("Wednesday")
#     with col4:
#         button_thu = st.button("Thursday")
#     with col5:
#         button_fri = st.button("Friday")

#     if button_mon :
#         col1,col2 = st.columns([1,9])
#         with col1:
#             st.markdown('<div style="font-size: 16px; color: blue;"><br><br>9:30-12:30</div>', unsafe_allow_html=True)
#             st.markdown('<div style="font-size: 16px; color: blue;"><br><br><br><br>13:30-16:30</div>', unsafe_allow_html=True)
#         with col2:
#             container = st.container()
#             container.markdown("""<div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
#             CPE241 <br> Database systems </div>""", unsafe_allow_html=True)
#             container = st.container()
#             container.markdown("""<div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
#             - <br> - </div>""", unsafe_allow_html=True)

#     elif button_tue :
#         col1,col2 = st.columns([1,9])
#         with col1:
#             st.markdown('<div style="font-size: 16px; color: blue;"><br><br>9:30-12:30</div>', unsafe_allow_html=True)
#             st.markdown('<div style="font-size: 16px; color: blue;"><br><br><br><br>13:30-16:30</div>', unsafe_allow_html=True)

#         with col2:
#             container = st.container()
#             container.markdown("""<div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
#             CPE241 <br> Database systems </div>""", unsafe_allow_html=True)
#             container = st.container()
#             container.markdown("""
#             <div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
#             CPE232 <br> Data models </div>""", unsafe_allow_html=True)

#     elif button_wed :
#         col1,col2 = st.columns([1,9])
#         with col1:
#             st.markdown('<div style="font-size: 16px; color: blue;"><br><br>9:30-12:30</div>', unsafe_allow_html=True)
#             st.markdown('<div style="font-size: 16px; color: blue;"><br><br><br><br>13:30-16:30</div>', unsafe_allow_html=True)

#         with col2:
#             container = st.container()
#             container.markdown("""<div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
#             STA302 <br> Statistics for engineering </div>""", unsafe_allow_html=True)
#             container = st.container()
#             container.markdown("""
#             <div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
#             CPE223 <br> Computer architectures </div>""", unsafe_allow_html=True)

#     elif button_thu :
#         col1,col2 = st.columns([1,9])
#         with col1:
#             st.markdown('<div style="font-size: 16px; color: blue;"><br><br>9:30-12:30</div>', unsafe_allow_html=True)
#             st.markdown('<div style="font-size: 16px; color: blue;"><br><br><br><br>13:30-16:30</div>', unsafe_allow_html=True)

#         with col2:
#             container = st.container()
#             container.markdown("""<div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
#             STA302 <br> Statistics for engineering </div>""", unsafe_allow_html=True)
#             container = st.container()
#             container.markdown("""
#             <div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
#             GEN111 <br> Man and ethics of living </div>""", unsafe_allow_html=True)

#     elif button_fri :
#         col1,col2 = st.columns([1,9])
#         with col1:
#             st.markdown('<div style="font-size: 16px; color: blue;"><br><br>9:30-12:30</div>', unsafe_allow_html=True)
#             st.markdown('<div style="font-size: 16px; color: blue;"><br><br><br><br>13:30-16:30</div>', unsafe_allow_html=True)

#         with col2:
#             container = st.container()
#             container.markdown("""<div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
#             - <br> - </div>""", unsafe_allow_html=True)
#             container = st.container()
#             container.markdown("""
#             <div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
#             MIC101 <br> General biology </div>""", unsafe_allow_html=True)
                
#     #contact
#     st.header("Contact")
#     col1,col2 = st.columns([1,25])
#     with col1:
#         st.image("https://cdn.discordapp.com/attachments/1081112018360221696/1238078545306193971/phone.webp?ex=663df9ff&is=663ca87f&hm=56ce2a9a6cff83553173f7e3addf5ca38d430291aa910e9d76d86b5f817d3f72&", width=30)
#         st.image("https://cdn.discordapp.com/attachments/1081112018360221696/1238084839526371358/gmail.png?ex=663dffdc&is=663cae5c&hm=42a416e3544ac0f17421b06dd961a55457c4f89d15819d26e24b9b41db789c01&", width=30)
#         st.image("https://cdn.discordapp.com/attachments/1081112018360221696/1238085072800714812/facebook.webp?ex=663e0013&is=663cae93&hm=7b99b8867ac49ba687044b6dbd1e8af9fca7224de832e9dc2d9f00a7fad9786d&", width=30)
#         st.image("https://cdn.discordapp.com/attachments/1081112018360221696/1238085202924802169/ig.webp?ex=663e0032&is=663caeb2&hm=5123dce1cd7d74bfd470c61ca508067a52fb66f6f673cf39c3c63b7ec285f09d&", width=30)
#     with col2:
#         st.write("Tel : xxx-xxxx-xxxx")
#         st.write("Gmail : xxxx@gmail.com")
#         st.write("Facebook : xxxxxxx")
#         st.write("Instagram : xxxxxxx")

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
import hydralit_components as hc
from streamlit_navigation_bar import st_navbar
from Home import Home, login
import streamlit as st
import hydralit_components as hc
import datetime

#make it look nice from the start
def About():
    col1 = st.columns([0.6,0.4])

    with col1[0]:
        st.markdown(f"""
        <div>
        <h1 >About Us</h1>
        <p style="font-weight: 600;">At Oceanview University, we strive to cultivate an environment where students can embark on transformative educational journeys that empower them to make a positive impact in the world.</p>
        <p style="font-weight: 600;">Nestled along the picturesque coastline, our university provides not only a stunning backdrop for learning but also a dynamic academic community dedicated to excellence, innovation, and inclusivity.</p>
        <p style="font-weight: 600;">Our mission at Oceanview University is to foster intellectual curiosity, critical thinking, and ethical leadership in our students. Through rigorous academic programs, experiential learning opportunities, and a commitment to interdisciplinary collaboration, we aim to equip graduates with the knowledge, skills, and values needed to address the complex challenges of today's society and to contribute meaningfully to their communities.</p>
        <p style="font-weight: 600;">We invite you to explore all that Oceanview University has to offer a vibrant hub of learning and innovation.</p>
        <h3 style="font-weight: bold; font-size:35px;">Student Service and Support</h3>
        <ol style="font-weight: 600;">
            <li>Academic Advising: Personalized guidance for academic planning and goal setting.</li>
            <li>Tutoring Services: Peer and professional tutoring to support student learning.</li>
            <li>Career Counseling: Assistance with career exploration, job search strategies, and resume building.</li>
            <li>Wellness Resources: Access to mental health support, counseling services, and wellness programs.</li>
            <li>Financial Aid Assistance: Guidance on scholarships, grants, loans, and financial literacy.</li>
            <li>Accessibility Services: Accommodations and support for students with disabilities.</li>
            <li>Library Services: Research assistance, access to resources, and study spaces.</li>
            <li>Housing Assistance: Support with finding on-campus or off-campus housing options.</li>
            <li>Student Organizations: Opportunities for involvement in clubs, societies, and student-led initiatives.</li>
            <li>Technology Support: Assistance with campus technology, software, and online learning platforms.</li>
        </ol>
        <h3 style="font-weight: bold; font-size:35px;">Student-Centered Support</h3>
        <p style="font-weight: 600;">We understand that each student's journey is unique, which is why we offer a range of support services to help students thrive academically, personally, and professionally. From academic advising and tutoring to career counseling and wellness resources, we are here to support students every step of the way on their path to success.</p>
    </div>""",unsafe_allow_html=True)
    with col1[1]:
        st.markdown(f"""
        <div style="margin-top:30px;"><br></br>
        <h3 style="font-weight: bold; font-size:35px;">University Address</h3>
        <p style="font-weight: 600;">Oceanview University<br>123 Coastal Avenue<br>Seaside, CA 98765<br>United States<br>Oceanviewuniversity.com<br>Reg no: 556703-7485</p>
        <h3 style="font-weight: bold; font-size:35px;">University around the world</h3>
        <p style="font-weight: 600; float: left; margin-right:150px;">
            Oceanview Beachtown<br>
            789 Oceanfront Drive<br>
            Beachtown, CA 54321<br>
            United States<br>
            <span style="text-decoration: none; color: inherit;">Beachtownuniversity.com</span><br>
            Reg no: <span style="text-decoration: none; color: inherit;">123456-7890</span>
        </p>
        <p style="font-weight: 600;">
            Oceanview Shoreline<br>
            456 Shoreline Avenue<br>
            Oceanside, CA 12345<br>
            United States<br>
            <span style="text-decoration: none; color: inherit;">Shorelinecollege.com</span><br>
            Reg no: <span style="text-decoration: none; color: inherit;">246801-3579</span>
        </p>
    </div>""",unsafe_allow_html=True)