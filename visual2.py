import pandas as pd
import streamlit as st
import numpy as np

df = pd.read_csv("prep_fifa.csv")
# club_name = df['Club'].unique()
#
# nation_name = df['Nationality'].unique()
# position = df['Position'].unique()
#
# international_reputation =  df['International Reputation'].unique()
#
# body_type = df['Body Type'].unique()
#
# preferred_foot = df['Preferred Foot'].unique()
#
# # nation_name.append("All")
# # position.append("All")
# # international_reputation.append("All")
# # body_type.append("All")
# # preferred_foot.append("All")
#
#
# option = st.selectbox(
#         "Club_1",
#         club_name)
#
# nationality = st.selectbox(
#         "Nationality",
#         nation_name
#     )
#
# position_option = st.selectbox(
#         "Position",
#         position
#     )
# international_reputation_option = st.selectbox(
#     "International Reputation",
#     international_reputation
# )
# body_type_option = st.selectbox(
#         "Body Type",
#         body_type
#     )
# preferred_foot_option = st.selectbox(
#         "Preferred Foot",
#         preferred_foot
#     )
#
# #df2 = df[df['Club'] == option]
# #players = df2['Name'].to_list()
#
# # option2 = st.selectbox(
# #         "Players_1",
# #         players
# #     )
#
# #eight = df2[df2['Name']==option2]['Height'].iloc[0]
#
# total = len(df[(df['Club']==option) & (df['Nationality']==nationality) & (df['Position']==position_option) &
#                (df['International Reputation']==international_reputation_option) & (df['Body Type']==body_type_option) &
#                (df['Preferred Foot']==preferred_foot_option)])
# # preferred_foot = df2[df2['Name']==option2]['Preferred Foot'].iloc[0]
# #st.header(f"Name: {option2}")
# st.subheader(f"Total Number of Players: {total}")


df['Value'] = df['Value'] * 1000  # Assuming Value is in thousands

# Streamlit UI setup
st.title("FIFA Players Analysis")

# Sidebar filters
nationality = st.sidebar.selectbox("Select Nationality", options=['All'] + df['Nationality'].unique().tolist(), index=0)

# Filter data
if nationality != 'All':
    df = df[df['Nationality'] == nationality]

# KPI cards
top_player = df.loc[df['Overall'].idxmax()]
highest_wage_player = df.loc[df['Wage'].idxmax()]
highest_value_player = df.loc[df['Value'].idxmax()]
highest_potential_player = df.loc[df['Potential'].idxmax()]
oldest_player = df.loc[df['Age'].idxmax()]
highest_composure_player = df.loc[df['Composure'].idxmax()]
highest_standing_tackle_player = df.loc[df['StandingTackle'].idxmax()]

# Display KPIs
st.markdown(f"### Top Players with Highest Overall: {top_player['Name']} ({top_player['Overall']})")
st.markdown(f"### Highest Wage Player Name: {highest_wage_player['Name']} ({highest_wage_player['Wage']})")
st.markdown(f"### Highest Value Player: {highest_value_player['Name']} (${highest_value_player['Value']})")
