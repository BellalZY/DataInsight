import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("return_rate_region.csv")

pivot_df = df.pivot(index="REGION", columns="CATEGORY", values="RETURN_RATE")

fig = px.imshow(
    pivot_df,
    text_auto=True,
    labels=dict(x="Product Category", y="Region", color="Return Rate (%)"),
    title="Return Rate Heatmap by Region and Product Category"
)

st.plotly_chart(fig)
