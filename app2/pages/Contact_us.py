import streamlit as st
from app2.send_email import send_email

with st.form(key="forms"):
    st.title("Contact me ")
    email = st.text_input("Your Email ")
    raw_message = st.text_area("Message ")
    message = f"""\
Subject : Email from {email}

From : {email}
Message : {raw_message}
"""
    submit = st.form_submit_button("Submit")
    if submit:
        send_email(message)
        st.info("Submitted Successfully !")
