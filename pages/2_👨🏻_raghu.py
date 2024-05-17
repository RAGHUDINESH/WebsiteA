import streamlit as st
import pandas as pd
import datetime

st.set_page_config(
    page_title="Raghu Timetable",
    page_icon="👩",
)

st.title("Raghu's Timetable",)
days = ["WFH - Native Place", "Weekend OR Holiday"]
day = st.selectbox("Day:",days)

df = pd.read_csv(f"TimeTable/Raghu/{day}.csv")
timetable = st.empty()
timetable.table(df)

uploaded_file = st.file_uploader(f"Upload {day}'s new timetable",type=['csv'])
if st.button("Update"):
    if uploaded_file:
        new_df = pd.read_csv(uploaded_file)
        new_df.to_csv(f"TimeTable/Raghu/{day}.csv", index=False)
        timetable.table(new_df)