import streamlit as st
import pandas as pd


# Load CSV
df = pd.read_csv("visualization/data/sales_profit_subCategory.csv")

# Show title and data
st.title("sales profit by sub category Preview")
st.bar_chart(df, x="sub_category", y="total_sales")