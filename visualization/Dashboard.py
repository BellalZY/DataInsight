import streamlit as st
import pandas as pd
from langchain.chat_models import ChatOpenAI
import pandas as pd

dfs = {}
uploaded_files = ["./data/DIM_CUSTOMER.csv","./data/DIM_DATE.csv","./data/DIM_ORDER.csv","./data/DIM_PRODUCT.csv","./data/DIM_RETURN.csv","./data/sales_over_time.csv","./data/sales_profit_subCategory.csv","./data/monthly_sales_trend.csv","./data/profitability_category.csv","./data/top10_customer.csv","./data/ship_performance.csv",]
for file in uploaded_files:
    dfs[file] = pd.read_csv(file)

previews = "\n\n".join(
        f"### {name}\n{df.head(10).to_csv(index=False)}" for name, df in dfs.items()
    )

system_prompt = (
        "You are an AI-powered business analyst. Multiple CSV files have been uploaded. "
        "Each contains different aspects of a dataset (e.g., sales, products, returns). "
        "Use them to answer the user's question with insights, trends, and reasoning.\n\n"
    )


st.title("Check out our AI Helper here to help you made decisions!")
st.write("Our AI-powered assistant, seamlessly integrated with DeepSeek LLM, helps you make faster and smarter business decisions. Whether you're analyzing reports, generating insights, or asking complex questions about your data, the DeepSeek model provides accurate, context-aware answers in real time. Say goodbye to decision fatigue—just ask, and let AI guide your strategy.")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

def generate_response(input_text):
    user_prompt = (
        f"Below are previews of the uploaded datasets:\n{previews}\n\n"
        f"User question:\n{input_text}\n\n"
        f"Based on the data above, provide a clear and concise business analysis."
    )
    messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
    chat = ChatOpenAI(
        openai_api_base="https://api.deepseek.com/v1",
        openai_api_key=openai_api_key,
        model="deepseek-chat",
    )

    response = chat.invoke(messages)
    st.info(response.content)

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)

df1 = pd.read_csv("./data/DIM_CUSTOMER.csv")
df2 = pd.read_csv("./data/DIM_DATE.csv")
df3 = pd.read_csv("./data/DIM_ORDER.csv")
df4 = pd.read_csv("./data/DIM_PRODUCT.csv")
df5 = pd.read_csv("./data/DIM_RETURN.csv")

st.title("CUSTOMER Data Preview")

sample_option = st.radio("How would you like to select your data?", ("Random Sample", "Filter by Region"))

if sample_option == "Random Sample":
    sample_size = st.slider("Number of rows to sample", 5, 100, 20)
    sampled_df = df1.sample(sample_size)

elif sample_option == "Filter by Region":
    selected_region = st.selectbox("Select a region", df4["Region"].dropna().unique())
    sampled_df = df1[df1["Region"] == selected_region]

# Preview
st.subheader("Sampled Data Preview")
st.dataframe(sampled_df)

# Summary
st.subheader("Summary of Sampled Data")

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Customers", sampled_df["Customer ID"].nunique())
    st.metric("Unique Countries", sampled_df["Country"].nunique())
    st.metric("Unique Segments", sampled_df["Segment"].nunique())

with col2:
    st.write("### Segment Distribution")
    st.bar_chart(sampled_df["Segment"].value_counts())
    st.write("### Country Count")
    st.bar_chart(sampled_df["Country"].value_counts())

st.title("DATE Data Preview")

st.subheader("Filter by Year")
year_choice = st.multiselect("Select Years", sorted(df2["year"].unique()), default=df2["year"].unique())
filtered_df = df2[df2["year"].isin(year_choice)]

st.subheader("Filtered Dates")
st.dataframe(filtered_df)

st.subheader("Monthly Distribution (Filtered)")
monthly_counts = filtered_df["month"].value_counts().sort_index()
st.bar_chart(monthly_counts)

st.title("ORDER Data Preview")

st.subheader("Sample or Filter Orders")
sample_size = st.slider("Sample Size", min_value=5, max_value=len(df3), value=10)
sample_df = df3.sample(sample_size, random_state=42)

st.subheader("Random Sample of {sample_size} Orders")
st.dataframe(sample_df)

st.subheader("Order Priority Distribution")
priority_counts = df3["Order Priority"].value_counts()
st.bar_chart(priority_counts)

st.subheader("Orders Over Time (Yearly)")
df3["Order Date"] = pd.to_datetime(df3["Order Date"], errors='coerce')
df3["Order Year"] = df3["Order Date"].dt.year
yearly_counts = df3["Order Year"].value_counts().sort_index()
st.line_chart(yearly_counts)

st.title("PRODUCT Data Preview")

st.subheader("Product Category Overview")

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Products", len(df4))
    st.metric("Categories", df4["Category"].nunique())
    st.metric("Sub-Categories", df4["Sub-Category"].nunique())

with col2:
    st.write("### Category Distribution")
    st.bar_chart(df4["Category"].value_counts())

    st.write("### Top Sub-Categories")
    st.bar_chart(df4["Sub-Category"].value_counts().head(10))

st.subheader("Filter by Category")
selected_cat = st.multiselect("Choose Category", df4["Category"].unique(), default=df4["Category"].unique())
filtered_df = df4[df4["Category"].isin(selected_cat)]

st.subheader("Filtered Products")
st.dataframe(filtered_df)

st.title("RETURN Data Preview")
st.dataframe(df5)

st.subheader("Return Summary by Region")

return_counts = df5.groupby("region").size().sort_values(ascending=False)

st.bar_chart(return_counts)

top_n = st.slider("Top N Regions", min_value=3, max_value=10, value=5)
st.subheader(f"Top {top_n} Regions by Return Volume")
st.dataframe(return_counts.head(top_n).reset_index(name="Return Count"))

