import streamlit as st
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="NITwork",
    page_icon="🎓",
    layout="wide"
)

# =====================================================
# DARK THEME CSS
# =====================================================

st.markdown("""
<style>

.stApp {
    background-color: #020617;
}

/* Main container */
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

/* Headings */
h1,h2,h3,h4,h5,h6 {
    color: white !important;
}

/* Paragraphs */
p {
    color: #CBD5E1 !important;
}

/* Search Bar */
.stTextInput input {
    background-color: #0F172A !important;
    color: white !important;
    border: 1px solid #334155 !important;
    border-radius: 10px;
}

/* Hero */
.hero-title{
    text-align:center;
    font-size:72px;
    font-weight:800;
    color:white;
}

.hero-subtitle{
    text-align:center;
    font-size:22px;
    color:#94A3B8;
    margin-bottom:40px;
}

/* Metric Cards */
.metric-card{
    background:#0F172A;
    border:1px solid #1E293B;
    padding:20px;
    border-radius:15px;
    text-align:center;
}

/* NIT Card */
.nit-card{
    background:#0F172A;
    border:1px solid #1E293B;
    border-radius:15px;
    padding:25px;
    margin-bottom:15px;
}

/* Footer */
.footer{
    text-align:center;
    color:#94A3B8;
    margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HERO SECTION
# =====================================================

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

# =====================================================
# STATS
# =====================================================

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class='metric-card'>
        <h2>31</h2>
        <p>NITs</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='metric-card'>
        <h2>100%</h2>
        <p>Free</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='metric-card'>
        <h2>Student</h2>
        <p>Made</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# =====================================================
# LOAD CSV
# =====================================================

df = pd.read_csv("data/nits.csv")

# =====================================================
# SEARCH
# =====================================================

search = st.text_input(
    "🔍 Search NIT",
    placeholder="Search by NIT name..."
)

if search:
    df = df[
        df["ShortName"]
        .str.contains(search, case=False, na=False)
    ]


# =====================================================
# ALL NITS
# =====================================================

st.write("")
st.subheader("🏛 Browse All NITs")

for _, row in df.iterrows():

    col1, col2, col3 = st.columns([5, 1.5, 1.5])

    with col1:

        st.markdown(
            f"""
            ### #{row['DisplayRank']} {row['ShortName']}
            <span style='color:#94A3B8'>
            {row['City']}, {row['State']}
            </span>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.link_button(
            "🌐 Website",
            row["Website"],
            use_container_width=True
        )

    with col3:

        wp_link = str(row["WhatsAppLink"]).strip()

        if (
            wp_link
            and wp_link != "PENDING"
            and wp_link != "nan"
            and wp_link.startswith("http")
        ):

            st.link_button(
                "💬 Join",
                wp_link,
                use_container_width=True
            )

        else:

            st.button(
                "🚧 Soon",
                key=row["ShortName"],
                use_container_width=True
            )

    st.divider()
# =====================================================
# ABOUT
# =====================================================

st.write("")
st.subheader("About NITwork")

st.write("""
NITwork helps students discover NIT communities,
find official college websites,
and make more informed counselling decisions.

Built for students, by students.
""")

# =====================================================
# FOOTER
# =====================================================

st.write("---")

st.markdown("""
<div class='footer'>

<h4>Built by Gauri 🚀</h4>

<a href="https://www.linkedin.com/in/gauri-92359a270/" target="_blank">
Connect on LinkedIn
</a>

</div>
""", unsafe_allow_html=True)
