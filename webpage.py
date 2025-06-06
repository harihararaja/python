import streamlit as st
st.set_page_config(page_title="Styled Form", layout="centered")
st.markdown("""
    <style>
    .stApp {
        background-color:lightblue;
        }
    </style>
    """, unsafe_allow_html=True)
st.title("JOB APPLICATION FORM")
<<<<<<< HEAD
camera=st.checkbox("it launch the camera ")
if camera:
   img=st.camera_input("")
st.text("feed the photo of the empolyee")
=======
>>>>>>> a4c39601c1d8a67402d0e6d6d417c42b4a5d840e
name=st.text_input("NAME")
age=st.number_input("AGE",value=None,max_value=70,step=1)
date=st.date_input("DATE OF BRITH:",None)
con=st.text_input("CONTACT NUMBER")
pos=st.text_input
id=st.text_input("E-MAIL")
gen=st.radio(
    "GENDER:",
    options=["MALE", "FEMALE"],
    horizontal=True,
)
s=st.write(f"YOU SELECTED:{gen}")
add=st.text_input("ADDRESS:")
sta=st.text_input("STATE:")
cou=st.text_input("COUNTRY:")
fat=st.text_input("FATHER NAME")
mot=st.text_input("MOTHER NAME")
occ=st.text_input("OCCUPATION")
Fnums=st.text_input("DEGREE:",value=None)
Mnums=st.text_input("DEPARTMENT:",value=None)
year=st.date_input("PASSOUT YEAR:",None)
uploaded_file = st.file_uploader("upload your resume", type=["png", "jpg", "jpeg", "pdf", "txt"])
uploaded_photo = st.file_uploader("upload your photo", type=["png", "jpg", "jpeg", "pdf", "txt"])
confirms=st.checkbox("THE ABOVE INFORMATION CONTAINED IS CORRECT TO MY KNOWLEDGE ")
if confirms:
    if not camera:
       st.error("PLEASE UPLOAD YOUR CURRENT PHOTO")
    if not name:
         st.error("CHECK THE NAME !")
    if not age:
        st.error("ENTER THE AGE !")
    if not con or len(con) != 10:
        st.error("CONTRACT NUMBER MUST BE EXACTLY 10 DIGITS !")
    if not add:
        st.error("CHECK THE ADDRESS !")
    if not sta:
       st.error("CHECK THE STATE !")
    if not cou:
       st.error("CHECK THE COUNTRY !")
    if not fat:
       st.error("CHECK THE FATHER NAME !")
    if not mot:
       st.error("CHECK THE MOTHRE NAME !")
    if not sta:
       st.error("ENTER THE STATE !")
    if not Fnums :
        st.error("CHECK THE DEGREE !")
    if not Mnums or len(Mnums) != 10:
        st.error("CHECK THE DEPARTMENT !")
    if not year:
        st.error("check the passout year!")
    if not uploaded_file:
        st.error("PLEASE UPLOAD THE RESUME !")
    if not  uploaded_photo:
        st.error("please upload your photo !")
    elif st.button("submitt"):
        st.toast("This information has been sent.")
st.button("cancel")
