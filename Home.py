import streamlit as st

def Home():
    # st.title("Home")
    # st.write("Welcome to the Home Page")
    st.image("image/kmutt-websitelogo-01-scaled.jpg", width=600)

    # News
    st.header("News")     

    # Define image sources
    openhouse_src = 'https://scontent.fbkk22-3.fna.fbcdn.net/v/t39.30808-6/322296094_565819111642809_6127783231039668742_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=5f2048&_nc_ohc=MMyyxuA_gJoQ7kNvgE6v6IA&_nc_ht=scontent.fbkk22-3.fna&oh=00_AfATU6shTCR2a8saS8TMxNJka5O6qxjeB562yzvOTU9Hhw&oe=6642B780'
    university_sport_src = 'https://www.kmutt.ac.th/wp-content/uploads/2024/01/SCM15612-1200x800.jpg'
    Petchre_Pra_Jom_src = 'https://scontent.fbkk22-7.fna.fbcdn.net/v/t39.30808-6/305927187_567352885190048_1863554905914937964_n.png?stp=dst-png_p720x720&_nc_cat=107&ccb=1-7&_nc_sid=5f2048&_nc_ohc=eiykJzl3WgkQ7kNvgFc36pn&_nc_ht=scontent.fbkk22-7.fna&oh=00_AfCx3AkgdHWFCW9_5-O18eMkjwCxT6LYs-yyFr_YwKgtAw&oe=664299A9'
    comcamp_src = 'https://scontent.fbkk22-6.fna.fbcdn.net/v/t39.30808-1/435764432_1101676158081572_6864015543597168996_n.jpg?stp=dst-jpg_p480x480&_nc_cat=102&ccb=1-7&_nc_sid=5f2048&_nc_ohc=WFZ4TCoUp2oQ7kNvgHkJImv&_nc_ht=scontent.fbkk22-6.fna&oh=00_AfCXurSMULaKSZP-50cahjkNbgeFL9BwUh5s3_ml4yF9kw&oe=6642BEB9'
    orientation_src = 'https://media.discordapp.net/attachments/1081112018360221696/1237777829580640277/orientation.jpg?ex=663ce1ef&is=663b906f&hm=0716080b9185b809037fddb341594fd81d6d92ed30fd3b6bfbf0ab51dcf118f9&=&format=webp&width=718&height=478'

    # Construct HTML strings for each image
    openhouse_img = f'<img src="{openhouse_src}" alt="openhouse" width="300" height="250" style="margin-right: 10px;">'
    university_sport_img = f'<img src="{university_sport_src}" alt="university_sport" width="300" height="250" style="margin-right: 10px;">'
    Petchre_Pra_Jom_img = f'<img src="{Petchre_Pra_Jom_src}" alt="Petchre_pra_jom" width="500" height="250" style="margin-right: 10px;">'
    comcamp_img = f'<img src="{comcamp_src}" alt="comcamp" width="300" height="250" style="margin-right: 10px;">'
    orientation_img = f'<img src="{orientation_src}" alt="comcamp" width="300" height="250" style="margin-right: 10px;">'

    # Combine images into a single HTML string with a containing div
    news_pictures = f'<div style="display: flex; overflow-x: auto; white-space: nowrap;">{openhouse_img}{university_sport_img}{Petchre_Pra_Jom_img}{comcamp_img}{orientation_img}</div>'
    st.markdown(news_pictures, unsafe_allow_html=True)

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
            CPE241 <br> Database systems </div>""", unsafe_allow_html=True)
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
            CPE241 <br> Database systems </div>""", unsafe_allow_html=True)
            container = st.container()
            container.markdown("""
            <div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            CPE232 <br> Data models </div>""", unsafe_allow_html=True)

    elif button_wed :
        col1,col2 = st.columns([1,9])
        with col1:
            st.markdown('<div style="font-size: 16px; color: blue;"><br><br>9:30-12:30</div>', unsafe_allow_html=True)
            st.markdown('<div style="font-size: 16px; color: blue;"><br><br><br><br>13:30-16:30</div>', unsafe_allow_html=True)

        with col2:
            container = st.container()
            container.markdown("""<div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            STA302 <br> Statistics for engineering </div>""", unsafe_allow_html=True)
            container = st.container()
            container.markdown("""
            <div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            CPE223 <br> Computer architectures </div>""", unsafe_allow_html=True)

    elif button_thu :
        col1,col2 = st.columns([1,9])
        with col1:
            st.markdown('<div style="font-size: 16px; color: blue;"><br><br>9:30-12:30</div>', unsafe_allow_html=True)
            st.markdown('<div style="font-size: 16px; color: blue;"><br><br><br><br>13:30-16:30</div>', unsafe_allow_html=True)

        with col2:
            container = st.container()
            container.markdown("""<div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            STA302 <br> Statistics for engineering </div>""", unsafe_allow_html=True)
            container = st.container()
            container.markdown("""
            <div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            GEN111 <br> Man and ethics of living </div>""", unsafe_allow_html=True)

    elif button_fri :
        col1,col2 = st.columns([1,9])
        with col1:
            st.markdown('<div style="font-size: 16px; color: blue;"><br><br>9:30-12:30</div>', unsafe_allow_html=True)
            st.markdown('<div style="font-size: 16px; color: blue;"><br><br><br><br>13:30-16:30</div>', unsafe_allow_html=True)

        with col2:
            container = st.container()
            container.markdown("""<div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            - <br> - </div>""", unsafe_allow_html=True)
            container = st.container()
            container.markdown("""
            <div style="border : 1px solid black; padding: 20px; margin: 20px; border-radius: 5px; background-color: #f9f9f9;">
            MIC101 <br> General biology </div>""", unsafe_allow_html=True)
                
    #contact
    st.header("Contact")
    col1,col2 = st.columns([1,25])
    with col1:
        st.image("https://cdn.discordapp.com/attachments/1081112018360221696/1238078545306193971/phone.webp?ex=663df9ff&is=663ca87f&hm=56ce2a9a6cff83553173f7e3addf5ca38d430291aa910e9d76d86b5f817d3f72&", width=30)
        st.image("https://cdn.discordapp.com/attachments/1081112018360221696/1238084839526371358/gmail.png?ex=663dffdc&is=663cae5c&hm=42a416e3544ac0f17421b06dd961a55457c4f89d15819d26e24b9b41db789c01&", width=30)
        st.image("https://cdn.discordapp.com/attachments/1081112018360221696/1238085072800714812/facebook.webp?ex=663e0013&is=663cae93&hm=7b99b8867ac49ba687044b6dbd1e8af9fca7224de832e9dc2d9f00a7fad9786d&", width=30)
        st.image("https://cdn.discordapp.com/attachments/1081112018360221696/1238085202924802169/ig.webp?ex=663e0032&is=663caeb2&hm=5123dce1cd7d74bfd470c61ca508067a52fb66f6f673cf39c3c63b7ec285f09d&", width=30)
    with col2:
        st.write("Tel : xxx-xxxx-xxxx")
        st.write("Gmail : xxxx@gmail.com")
        st.write("Facebook : xxxxxxx")
        st.write("Instagram : xxxxxxx")