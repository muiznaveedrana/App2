import streamlit as st

st.header("Contact Me")

with st.form(key = "form"):
    user_email = st.text_input("Your Email Adress")
    user_message = st.text_area("Your Message")
    button = st.form_submit_button()
    if button:
        print("hi")