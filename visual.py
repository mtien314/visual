import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("prep_fifa.csv")
club = df['Club'].unique()
club_name = set(club)

option = st.selectbox(
    "Club",
    club_name
)


col1, col2, col3, col4  = st.columns(4)

df = pd.read_csv("prep_fifa.csv")
# print(df.head())
# print(df.columns)
# print(df['Club'])
# print(df['ShortPassing'])
attributes = ['ShortPassing','BallControl','Dribbling','HeadingAccuracy','Crossing',
              'LongPassing','Curve','Finishing','FKAccuracy','Volleys']
values = [np.mean(df[df['Club']==option][attribute])for attribute in attributes]

with col1:
    st.header("ATK Stats")
    chart_data = pd.DataFrame({"values":values,"attributes":attributes})
    #radar chart

    # categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
    # values = [4, 3, 2, 5, 4]
    num_vars = len(attributes)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()


    values += values[:1]
    angles += angles[:1]


    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    ax.fill(angles, values, color='green', alpha=0.25)
    ax.plot(angles, values, color='green', linewidth=2)

    # Thêm nhãn cho mỗi trục
    ax.set_yticks([1, 2, 3, 4, 5])  # Định dạng các bậc giá trị
    ax.set_yticklabels(['1', '2', '3', '4', '5'], color="grey", size=10)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes, size=12)

    ax.set_title("ATK Stats", size=16, color='blue', y=1.1)
    ax.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    st.pyplot(fig)
    st.bar_chart(chart_data, x="attributes", y="values",color="#00FF00")

with col2:
    st.header("DEF Stats")
    attributes_2 = ['Composure','Aggression','Vision','Positioning','Interceptions',
                  'StandingTackle','Penalties','Marking','SlidingTackle']
    values_2 = [np.mean(df[df['Club'] == option][attribute])for attribute in attributes_2]
    chart_data = pd.DataFrame({"values": values_2, "attributes": attributes_2})
    num_vars = len(attributes_2)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    values_2 += values_2[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    ax.fill(angles, values_2, color='green', alpha=0.25)
    ax.plot(angles, values_2, color='green', linewidth=2)

    # Thêm nhãn cho mỗi trục
    ax.set_yticks([1, 2, 3, 4, 5])  # Định dạng các bậc giá trị
    ax.set_yticklabels(['1', '2', '3', '4', '5'], color="grey", size=10)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes_2, size=12)

    ax.set_title("DEF Stats", size=16, color='blue', y=1.1)
    ax.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    st.pyplot(fig)
    st.bar_chart(chart_data, x="attributes", y="values",color="#00FF00")

with col3:
    st.header("Stamina Stats")
    attributes_3 = ['Strength', 'SprintSpeed', 'Agility', 'Acceleration', 'Jumping',
                  'Stamina', 'Reactions', 'Balance', 'ShotPower', 'LongShots']

    values_3 = [np.mean(df[df['Club'] == option][attribute]) for attribute in attributes_3]
    chart_data = pd.DataFrame({"values": values_3, "attributes": attributes_3})
    num_vars = len(attributes_3)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()


    values_3 += values_3[:1]
    angles += angles[:1]


    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    ax.fill(angles, values_3, color='green', alpha=0.25)
    ax.plot(angles, values_3, color='green', linewidth=2)

    # Thêm nhãn cho mỗi trục
    ax.set_yticks([1, 2, 3, 4, 5])  # Định dạng các bậc giá trị
    ax.set_yticklabels(['1', '2', '3', '4', '5'], color="grey", size=10)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes_3, size=12)

    ax.set_title("Stamina Stats", size=16, color='blue', y=1.1)
    ax.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    st.pyplot(fig)
    st.bar_chart(chart_data, x="attributes", y="values",color="#00FF00")

with col4:
    st.header("GK Stats")
    attributes_4 = ['GKDiving','GKPositioning','GKHandling','GKReflexes','GKPositioning','GKHandling']

    values_4 = [np.mean(df[df['Club'] == option][attribute]) for attribute in attributes_4]
    chart_data = pd.DataFrame({"values": values_4, "attributes": attributes_4})
    num_vars = len(attributes_4)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    values_4 += values_4[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    ax.fill(angles, values_4, color='green', alpha=0.25)
    ax.plot(angles, values_4, color='green', linewidth=2)

    # Thêm nhãn cho mỗi trục
    ax.set_yticks([1, 2, 3, 4, 5])  # Định dạng các bậc giá trị
    ax.set_yticklabels(['1', '2', '3', '4', '5'], color="grey", size=10)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes_4, size=12)

    ax.set_title("GK Stats", size=16, color='blue', y=1.1)
    ax.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    st.pyplot(fig)
    st.bar_chart(chart_data, x="attributes", y="values",color="#00FF00")
