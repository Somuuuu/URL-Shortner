import streamlit as st 
from api import post


st.set_page_config(page_title="URL Shortner", page_icon="✂️", layout="centered")

with st.form("url"):  
    col = st.columns([1,1,1])
    with col[1]:
        st.header("URL Shortner")
    long = st.text_input("Enter Your Url")
    short = ""
    if st.form_submit_button("Shorten", type="primary"):
        short = post(
            long=long       
        )
        st.toast("successfull")
        
if short:
    st.write("Your Shortned URL:")
    col, col1 = st.columns([5,1])
    with col:
        st.write(short)
   
