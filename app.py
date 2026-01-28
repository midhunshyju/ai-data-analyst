import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Data Analyst", layout="wide")

st.title("📊 AI Data Analyst Chatbot")
st.write("Upload a CSV file and ask questions about your data.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Ask a question")
    question = st.text_input("Example: What are the top 5 rows?")
