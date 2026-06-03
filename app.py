import streamlit as st
import pandas as pd

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="NITwork",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.stApp {
    background-color: #020617;
    color: white;
}

.hero-title{
    text-align:center;
    font-size:70px;
    font-weight:800;
    margin-bottom:0px;
}

.hero-subtitle{
    text-align:center;
    font-size:22px;
    color:#94A3B8;
    margin-bottom:30px;
}

.metric-card{
    background:#0F172A;
    padding:20px;
    border-radius:15px;
    text-align:center;
    border:1px solid #1E293B;
}

.nit-card{
    background:#0F172A;
    padding:25px;
    border-radius:20px;
    border:1px solid #1E293B;
    margin-bottom:20px;
}

.footer{
    text-align:center;
    color:#94A3B8;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO
# -----------------------------

st.markdown(
"""
<div class='hero-title'>
🎓 NITwork
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='hero-subtitle'>
Find your NIT. Join your community. Choose with confidence.
</div>
""",
unsafe_allow_html=True
)

# -----------------------------
# STATS
# -----------------------------

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div class='metric-card'>
        <h2>31</h2>
        <p>NITs</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class='metric-card'>
        <h2>2030</h2>
        <p>Batch Focus</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class='metric-card'>
        <h2>1</h2>
        <p>Platform</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv("data/nits.csv")

# -----------------------------
# SEARCH
# -----------------------------

search = st.text_input(
    "🔍 Search NIT",
    placeholder="Type NIT name..."
)

if search:
    df = df[
        df["ShortName"]
        .str.contains(search, case=False)
    ]

# -----------------------------
# FEATURED SECTION
# -----------------------------

st.subheader("⭐ Top NITs")

featured = df.head(5)

cols = st.columns(5)

for idx, (_, row) in enumerate(featured.iterrows()):

    with cols[idx]:

        st.markdown(
            f"""
            <div class='nit-card'>
                <h4>#{row['DisplayRank']}</h4>
                <h3>{row['ShortName']}</h3>
                <p>{row['State']}</p>
                <p>{row['Tier']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# -----------------------------
# ALL NITS
# -----------------------------

st.write("")
st.subheader("🏛 Browse All NITs")

for _, row in df.iterrows():

    col1,col2,col3 = st.columns([4,1,1])

    with col1:

        st.markdown(
            f"""
            <div class='nit-card'>
            <h3>#{row['DisplayRank']} {row['ShortName']}</h3>
            <p>{row['City']}, {row['State']}</p>
            <p>{row['Tier']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        if row["WhatsAppLink"] != "PENDING":

            st.link_button(
                "💬 Join",
                row["WhatsAppLink"]
            )

        else:

            st.button(
                "🚧 Soon",
                key=row["ShortName"]
            )

    with col3:

        st.link_button(
            "🌐 Website",
            row["Website"]
        )

# -----------------------------
# ABOUT
# -----------------------------

st.write("")
st.write("---")

st.subheader("Why NITwork?")

st.write("""
Students spend hours searching for WhatsApp groups,
placement reports, campus information and counselling resources.

NITwork brings everything together in one place.
""")

# -----------------------------
# FOOTER
# -----------------------------

st.write("---")

st.markdown(
"""
<div class='footer'>

Built by <b>Gauri</b> 🚀

<a href="https://www.linkedin.com/in/gauri-92359a270/" target="_blank">
LinkedIn
</a>

</div>
""",
unsafe_allow_html=True
)
