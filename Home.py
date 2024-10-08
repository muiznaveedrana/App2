import streamlit as st
import pandas

# Set page configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="📊",
    layout = "wide"

)

col1, col2 = st.columns(2)

with col1:
    st.image("photos/photo.jpg", caption= "Me and my cousin. :)")
    
with col2:
    st.title("Muiz Naveed")
    content =""" 
Hello my name is Muiz Naveed and I'm a passionate young coder(only 11 years old) who wants to help the community. I started coding when I was six and self taught myself from there using youtube and other platforms. I have started a youtube channel LearnPythonWithMuiz and hope you subscribe. Thank you and goodbye.
"""
    st.info(content)

content2 = """Below you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write(content2)

col3,emptycol, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    df = pandas.read_csv("data.csv", sep=";")
    for index,row in df[:5].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image('photos/' + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index,row in df[5:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image('photos/' + row["image"])
        st.write(f"[Source Code]({row['url']})")
        