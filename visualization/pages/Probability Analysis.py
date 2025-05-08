import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

df = pd.read_csv("../profitability_category.csv")

st.title("Profitability by Product Category")
fig3 = plt.figure()
plt.pie(
    df["total_profit"],
    labels=df["category"],
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.75, 
    labeldistance=1.05,   
    wedgeprops=dict(width=0.4) 
)
plt.axis("equal")
st.pyplot(fig3)
