import streamlit as st
import pandas as pd

# Load CSV
df = pd.read_csv("../ship_performance.csv")

# Show title and data
st.title("Shipping Performance Preview")
st.bar_chart(df, x="ship_mode", y="num_shipped")
