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
camera=st.checkbox("it launch the camera ")
if camera:
   img=st.camera_input("")
st.text("feed the photo of the empolyee")
name=st.text_input("NAME")
age=st.number_input("AGE",value=None,max_value=70,step=1)
date=st.date_input("DATE OF BRITH:",None)
con=st.text_input("CONTRACT NUMBER")
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
Fnums=st.text_input("FATHER NUMBER:",value=None)
Mnums=st.text_input("MOTHER NUMBER:",value=None)
uploaded_file = st.file_uploader("Choose a the resume", type=["png", "jpg", "jpeg", "pdf", "txt"])
confirms=st.checkbox("I FEED THE ALL THE INFORMATION ")
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
       st.error("CHECK THE FATHER  !")
    if not mot:
       st.error("CHECK THE MOTHRE NAME !")
    if not sta:
       st.error("ENTER THE STATE !")
    if not Fnums or len(Fnums) != 10:
        st.error("CHECK THE FATHER NUMBER !")
    if not Mnums or len(Mnums) != 10:
        st.error("CHECK THE MOTHER NUMBER !")
    if not uploaded_file:
        st.error("PLEASE UPLOAD THE RESUME !")
    elif st.button("submitt"):
        st.toast("This informational have be send.")
st.button("cancel")
