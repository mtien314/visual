import streamlit as st
import pandas as pd


df = pd.read_csv("prep_fifa.csv")
club = df['Club'].unique()
club_name = set(club)

st.scatter_chart(df, x="SprintSpeed", y="Stamina")
st.header("SprintSpeed and Stamina")
