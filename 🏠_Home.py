import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)
with open('qoute.txt') as f:
    qoute = f.read()

new_qoute = st.text_area("Qoute",value=qoute,height= len(qoute.splitlines())*40+20, label_visibility='collapsed')
if new_qoute:
    with open('qoute.txt','w') as f:
       f.write(new_qoute)