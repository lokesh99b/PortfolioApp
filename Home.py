import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.JPG")

with col2:
    st.title("Lokesh Bhosale")
    content = """Hi, I am Lokesh! I am a Programmer. I graduated in 2022 with a 
    Bachelor of Engineering Degree in Information Science
    from Acharya Institute of Technology, Bangalore. 
    I am a fresher and looking for opportunities to put my 
    programming skills to use.
    """
    st.info(content)

content2 = """Below You can find some of the apps that I have built in Python."""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:5].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[5:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
