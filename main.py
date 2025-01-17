import streamlit as st

pg = st.navigation([st.Page("visual.py"), st.Page("visual2.py"), st.Page("visual3.py")])
pg.run()