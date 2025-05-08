import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Revenue Contribution by Top 10 Customers")
df = pd.read_csv("../top10_customer.csv")

fig = px.treemap(
    df,
    path=['customer_name'],
    values='total_revenue',
    hover_data={'total_revenue': True},
)

fig.update_traces(texttemplate="%{label}<br>$%{value:,.2f}")
st.plotly_chart(fig, use_container_width=True)
