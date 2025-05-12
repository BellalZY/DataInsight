import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("visualization/data/return_rate_region.csv")

fig = px.bar(
    df,
    x="region",
    y="return_rate_percent",
    text="return_rate_percent",
    labels={"region": "Region", "return_rate_percent": "Return Rate (%)"},
    title="Return Rate by Region"
)

fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
fig.update_layout(yaxis_title="Return Rate (%)", xaxis_title="Region")

st.plotly_chart(fig)
