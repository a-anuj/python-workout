import streamlit as st
import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "emailsfromapp@gmail.com"
    password = "taca tplp imgh quss"
    receiver = "emailsfromapp@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


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
