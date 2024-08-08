import streamlit as st
# Set page configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="📊",
)

col1, col2 = st.columns(2)

with col1:
    st.image("photos/L.png")

with col2:
    st.title("Muiz Naveed")
    content =""" 
Hello my name is Muiz Naveed and I'm a passionate young coder(only 11 years old) who wants to help the community. I started coding when I was six and self taught myself from there using youtube and other platforms. I have started a youtube channel LearnPythonWithMuiz and hope you subscribe. Thank you and goodbye.
"""
    st.info(content)