import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="NITwork",
    page_icon="🎓",
    layout="wide"
)

# ---------- CUSTOM CSS ----------

st.markdown("""
<style>

.main {
    background-color: #0F172A;
}

.card {
    background-color: #1E293B;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
}

.big-title {
    text-align:center;
    font-size:50px;
    font-weight:bold;
}

.subtitle {
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------

st.markdown(
    "<div class='big-title'>🎓 NITwork</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>India's Student-Made NIT Network</div>",
    unsafe_allow_html=True
)

# ---------- LOAD DATA ----------

df = pd.read_csv("data/nits.csv")

search = st.text_input("🔍 Search NIT")

if search:
    df = df[
        df["College"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

# ---------- COLLEGE CARDS ----------

for i,row in df.iterrows():

    st.markdown(
        f"""
        <div class='card'>
            <h3>#{row['Rank']} {row['College']}</h3>
            <p>{row['State']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1,col2 = st.columns(2)

    with col1:
        st.link_button(
            "🌐 Website",
            row["Website"]
        )

    with col2:
        st.link_button(
            "💬 WhatsApp",
            row["Whatsapp"]
        )

    st.divider()

# ---------- FOOTER ----------

st.markdown("---")

st.markdown("""
Built by Ayaan Vasishtha

Future Aerospace Engineer 🚀
""")
