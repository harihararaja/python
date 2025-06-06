import streamlit as st
import pandas as pd
df = pd.read_csv("C:\\Users\\Hari Hara Rajan\\Documents\\date.csv.xlsm")
st.dataframe(df)
