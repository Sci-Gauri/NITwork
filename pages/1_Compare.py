import streamlit as st
import pandas as pd

st.title("⚖ Compare NITs")

df = pd.read_csv("data/nits.csv")

selected = st.multiselect(
    "Select Colleges",
    df["College"]
)

if selected:

    compare_df = df[
        df["College"].isin(selected)
    ]

    st.dataframe(compare_df)
