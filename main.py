import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("My showcase App")

col1, col2 = st.columns(2)

with col1:
    st.image("images/portrait.jpg", width=300)

with col2:
    st.title("Joe Doe")
    content = """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
    when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries,
    """
    st.write(content)

content2 = """
Below are some apps I created using python, I have also shared the source code.
"""
st.info(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv")

with col3:
    for index, row in df[:2].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[2:].iterrows():
        st.header(row["title"])
