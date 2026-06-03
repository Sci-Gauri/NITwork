import streamlit as st
import pandas as pd

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="NITwork",
    page_icon="🎓",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

/* MAIN APP */

.stApp {
    background-color: #020617;
}

/* WIDER PAGE */

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background-color: #071226 !important;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

[data-testid="stSidebarNav"] {
    background-color: #071226 !important;
}

/* TEXT */

h1,h2,h3,h4,h5,h6,p {
    color: white !important;
}

/* HERO */

.hero-title {
    text-align:center;
    font-size:72px;
    font-weight:800;
    color:white;
    margin-bottom:0px;
}

.hero-subtitle {
    text-align:center;
    color:#94A3B8;
    font-size:24px;
    margin-bottom:20px;
}

.hero-small {
    text-align:center;
    color:#64748B;
    font-size:18px;
    margin-bottom:50px;
}

/* SEARCH */

.stTextInput input {
    background-color:#0F172A !important;
    color:white !important;
    border:1px solid #334155 !important;
    border-radius:12px !important;
    height:60px !important;
    font-size:18px !important;
}

/* LINKS */

a {
    color:#38BDF8 !important;
}

/* FOOTER */

.footer {
    text-align:center;
    color:#94A3B8;
    margin-top:50px;
}

/* DIVIDER */

hr {
    border: 1px solid #1E293B;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HERO
# =====================================

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

st.markdown(
"""
<div class='hero-small'>
31 NITs • WhatsApp Communities • Student Built
</div>
""",
unsafe_allow_html=True
)

# =====================================
# LOAD CSV
# =====================================

df = pd.read_csv("data/nits.csv")

# =====================================
# SEARCH
# =====================================

search = st.text_input(
    "",
    placeholder="🔍 Search your NIT..."
)

if search:

    df = df[
        df["ShortName"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

# =====================================
# NIT LIST
# =====================================

st.subheader("🏛 Browse All NITs")

for _, row in df.iterrows():

    col1, col2, col3 = st.columns([6, 1.3, 2])

    # College Name

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

    # Website Button

    with col2:

        website = str(row["Website"]).strip()

        if website.startswith("http"):

            st.link_button(
                "🌐 Website",
                website,
                use_container_width=True
            )

    # WhatsApp Button

    with col3:

        wp = str(row["WhatsAppLink"]).strip()

        if (
            wp
            and wp != "PENDING"
            and wp != "nan"
            and wp.startswith("http")
        ):

            st.link_button(
                "🟢 Join WhatsApp Group",
                wp,
                use_container_width=True
            )

        else:

            st.button(
                "🚧 Coming Soon",
                key=f"wp_{row['ShortName']}",
                use_container_width=True
            )

    st.divider()

# =====================================
# ABOUT
# =====================================

st.write("")
st.write("")

st.subheader("About NITwork")

st.write("""
NITwork helps students discover NIT communities,
find official college websites,
and make better counselling decisions.

Built for students, by students.
""")

# =====================================
# FOOTER
# =====================================

st.write("---")

st.markdown("""
<div class='footer'>

<h4>Built by Gauri 🚀</h4>

<a href="https://www.linkedin.com/in/gauri-92359a270/" target="_blank">
Connect on LinkedIn
</a>

</div>
""",
unsafe_allow_html=True)
