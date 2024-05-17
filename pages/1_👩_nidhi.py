import streamlit as st
import pandas as pd
import datetime

st.set_page_config(
    page_title="Nidhi Timetable",
    page_icon="👩",
)
st.title("Nidhi's Timetable",)
today = datetime.date.today()
weekday_number = today.weekday()

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = st.selectbox("Day:",weekdays,index=weekday_number)

df = pd.read_csv(f"TimeTable/NY/{day}.csv")
timetable = st.empty()
timetable.table(df)

uploaded_file = st.file_uploader(f"Upload {day}'s new timetable",type=['csv'])
if st.button("Update"):
    if uploaded_file:
        new_df = pd.read_csv(uploaded_file)
        new_df.to_csv(f"TimeTable/NY/{day}.csv", index=False)
        timetable.table(new_df)