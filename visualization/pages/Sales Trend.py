import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("visualization/data/monthly_sales_trend.csv")

years = sorted(df['year'].unique())
for y in years:
    year_df = df[df['year'] == y].sort_values('month')[['month', 'monthly_sales']].set_index('month')
    st.subheader(f"Monthly Sales - {y}")
    st.line_chart(year_df)

fig_total, ax_total = plt.subplots()
for y in years:
    year_df = df[df['year'] == y].sort_values('month')
    ax_total.plot(year_df['month'], year_df['monthly_sales'], marker='o', label=f"{y}")

pivot_df = df.pivot(index='month', columns='year', values='monthly_sales').sort_index()

st.subheader("Monthly Sales Trend - All Years")
st.line_chart(pivot_df)