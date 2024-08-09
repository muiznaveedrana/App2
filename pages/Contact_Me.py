import streamlit as st
import send_email
st.header("Contact Me")

with st.form(key = "form"):
    user_email = st.text_input("Your Email Adress")
    user_message = st.text_area("Your Message")
    user_message =  f"Subject: New Email From {user_email} \n From: {user_email} \n" + user_message + "\n" + user_email
    button = st.form_submit_button()
    if button:
        send_email.send_email(user_message)
        st.info("Email Succesfully Sent.")