import streamlit as st
from PIL import Image

st.set_page_config(page_title='Learn Genetics', page_icon="📖", layout="wide")

#A banner, could be ads or logo
ad_banner = Image.open("assets\DNAban.jpg")
st.image(ad_banner)

#tab for navigation
tab1, tab2, tab3, tab4 = st.tabs(["Home", "Our Courses", "Help", "Contact us"])

#Body
#Home
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        video_preview = Image.open("assets\preview.png")
        st.image(video_preview)
    with col2:
        st.header("Genetics for Biologist: Learn Genetics the easy way!")
        st.write("Learn Genetics in 1 hour with 25+ simple-to-use rules and guidelines — tons of amazing genetic resources included!")
        st.markdown("`Free Course` (122 ratings) 26 students 🎥 2 hours of on-demand video")
        st.write("🌐 language: English, Nepali")
        st.button("Enroll Now")


#tabs
tabx, taby, tabz = st.tabs(["What you'll learn", "Course content", "Instructions"])

#what you'll learn tabx
with tabx:
    st.write("""
    ✔️The 25+ guidelines of amazing web design: simple rules and guidelines that go straight to the point \n
    ✔️Immediate FREE access to the course e-book "Best Resources for Web Design and Development with HTML5 & CSS3" \n
    ✔️How to make text look professionally designed \n
    ✔️How to correctly use the power of colors \n
    ✔️How to get and use amazing images, fonts and icons to make your website shine — all for FREE. \n
    ✔️How to create a layout using whitespace and visual hierarchy \n
    ✔️How to keep yourself inspired to learn more and more about web design \n
    ✔️How to make your websites convert better using 8 simple-to-use techniques
    """)


#Course content
with taby:
    st.subheader("Requirements")
    st.write("""
    ⁍ Experienced in Biology \n
    ⁍ A working computer \n
    ⁍ Internet connection
    """)

    st.subheader("Description")
    st.write("IMPORTANT NOTE: The material of this course is also covered in my other course about web design and development with Stat. Scroll to the bottom of this page to check out that course, too! If you're already taking my other course, you already have all it takes to start designing beautiful websites today! Best web design course on Udemy: If you're interested in web design, but want more than just a how to use WordPress course, I highly recommend this one.")
    st.write("Did you know that beautiful websites convert better than ones that don't stand out at all? This means more sales, more signups, and ultimately more money for you. Do you want to learn how to do exactly that?")
    st.markdown("*If you wonder how you can make your next website really good-looking, then you've come to the right place!*")
    st.markdown("**In this course, I will show you 25+ guidelines of amazing web design in less than 1 hour.**")
    st.write("""
    •How to make text look professionally designed\n

    • How to correctly use the power of colors\n

    • How to get and use amazing images, fonts, and icons to make your website shine — all for FREE.\n

    • How to create a layout using whitespace and visual hierarchy\n

    • How to keep yourself inspired to learn more and more about web design\n

    • How to make your websites convert better using 8 simple-to-use techniques
    """)

    with st.expander("Course Syllabus"):
        st.write("""
        Introduction To Web Design                                03:47 \n 
        Beautiful Typography                                      08:54 \n 
        Using Colors Like A Pro                                   06:45 \n 
        The Meaning Of Colors In Web Design                       01:09 \n 
        Working With Images                                       04:54 \n 
        Use CSS To Work With Images                               02:31 \n 
        Web Design Quiz 1 5 questions Working With Icons          03:29 \n 
        Spacing And Layout                                        03:42 \n 
        Introduction To User Experience                           02:50 \n 
        The Secret Ingredient For Stunning Web Design             02:25 
        """)





#sub footer
st.markdown("---")
colx, coly = st.columns(2)
with colx:
    st.subheader("Top students choose us to built their carrier.")
    st.write("📚 There's no end to education.")
    st.write("📖 Learning never exhausts the mind.")

with coly:
    banner = Image.open("assets\dvert.jpg","r")
    st.image(banner)
    

st.markdown("---")

#footer
st.header("Learn more with us!")

cola, colb, colc, cold, cole = st.columns(5)

with cola:
    st.markdown("[Home](https://www.bing.com)")

with colb:
    st.markdown("[Other courses](https://www.bing.com)")

with colc:
    st.markdown("[Help](https://www.bing.com)")

with cold:
    st.markdown("[Contact us](https://www.bing.com)")

with cole:
    st.markdown("[Report abuse](https://www.bing.com)")

