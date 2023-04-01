import streamlit as st
from send_email import send_email

st.header('contact me:')

with st.form(key="email_form"):
    user_email = st.text_input('your email address: ')
    message = st.text_area('your message: ')
    final_email = f'''subject: Portfolio website message from {user_email}

from: {user_email}
message:
{message}'''
    button = st.form_submit_button()
    if button:
        send_email(final_email)
        st.info('your email was sent!')

