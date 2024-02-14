import streamlit as st

st.title("Contact us")

with st.form(key="contact_form"):
    user_email = st.text_input("Enter Email:")
    message = st.text_area("Enter message:")
    submit_btn = st.form_submit_button("Submit")
    if submit_btn:
        st.write("Hello")
