import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
from io import BytesIO
st.title("Form Application")
selected = option_menu(
    menu_title=None,
    options=["Home","menu", "Project", "Contract","help"],  
    icons=["house","menu-button-fill","book","envelope","info-square-fill"],
    default_index=0,
    orientation="horizontal"
)
name=st.text_input("NAME:")
date=st.date_input("DATE OF BRITH:",None)
age=st.number_input("AGE", value=None, min_value=0, max_value=70)
con=st.text_input("CONTRACT NUMBER")
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


if st.checkbox(F"I HAVE FULL THE INFORMATION"):
    if st.button("SUBMIT"):
        errors =False
    if not name:
        st.error("ENTER THE NAME ?")
    elif not date:
        st.error("ENTER THE DATE ?")
    if age<18 or age>70 :
        st.error("CHECK THE AGE OR 18-70 ?")
if not con.isdigit or len(con) != 10:
        st.error("CONTRACT NUMBER MUST BE EXACTLY 10 DIGITS.")
if not add:
     st.error("CHECK THE ADDRESS")
if not sta:
     st.error("CHECK THE STATE")
if not cou:
     st.error("CHECK THE COUNTRY")
if not fat:
     st.error("CHECK THE FATHER NAME")
if not mot:
     st.error("CHECK THE MOTHRE NAME")
if not sta:
     st.error("ENTER THE STATE")
if not Fnums.isdigit or len(Fnums) != 10:
        st.error("CHECK THE FATHER NUMBER .")
if not Mnums.isdigit or len(Mnums) != 10:
        st.error("CHECK THE MOTHER NUMBER.")

st.button("CANCEL")