import streamlit as st
import pandas as pd

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="NITwork",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

/* =========================
   GLOBAL
========================= */

.stApp {
    background-color: #020617;
}

/* Hide Streamlit Menu */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Header */

header[data-testid="stHeader"] {
    background: #020617;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    display: none;
}

/* Container */

.block-container {
    max-width: 1350px;
    padding-top: 2rem;
}

/* =========================
   TEXT
========================= */

h1,h2,h3,h4,h5,h6,p {
    color: white !important;
}

/* =========================
   HERO
========================= */

.hero-title {
    text-align:center;
    font-size:80px;
    font-weight:800;
    margin-bottom:0px;
}

.hero-subtitle {
    text-align:center;
    color:#94A3B8;
    font-size:24px;
    margin-top:0px;
}

.hero-small {
    text-align:center;
    color:#64748B;
    font-size:18px;
    margin-bottom:40px;
}

/* =========================
   SEARCH
========================= */

.stTextInput input {

    background-color:#0F172A !important;

    color:white !important;

    border:1px solid #334155 !important;

    border-radius:12px !important;

    font-size:18px !important;

    padding-top:14px !important;
    padding-bottom:14px !important;

    min-height:55px !important;
}

/* =========================
   BUTTONS
========================= */

.stLinkButton button,
.stButton button {

    background-color:#0F172A !important;

    color:white !important;

    border:1px solid #334155 !important;

    border-radius:10px !important;

    height:46px !important;

    font-weight:600 !important;
}

.stLinkButton button:hover,
.stButton button:hover {

    border:1px solid #38BDF8 !important;
}

/* =========================
   DIVIDERS
========================= */

hr {
    border:1px solid #1E293B;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HERO SECTION
# ==================================================

st.markdown("""
<h1 class='hero-title'>
<span style='color:#38BDF8;'>NIT</span>work
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hero-subtitle'>
Find your NIT. Join your community. Choose with confidence.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hero-small'>
31 NITs • WhatsApp Communities • Student Built
</div>
""", unsafe_allow_html=True)

# ==================================================
# LOAD CSV
# ==================================================

df = pd.read_csv("data/nits.csv")

# ==================================================
# SEARCH BAR
# ==================================================

left, center, right = st.columns([1,4,1])

with center:

    search = st.text_input(
    "",
    placeholder="Search NIT Trichy, Surathkal, Warangal..."
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

# ==================================================
# NIT LIST
# ==================================================

st.markdown("## 🏛 Browse All NITs")

st.write("")

for _, row in df.iterrows():

    col1, col2, col3 = st.columns([7, 1.4, 2.2])

    # College

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

    # Website

    with col2:

        website = str(row["Website"]).strip()

        if website.startswith("http"):

            st.link_button(
                "Website",
                website,
                use_container_width=True
            )

    # WhatsApp

    with col3:

        wp = str(row["WhatsAppLink"]).strip()

        if (
            wp
            and wp != "nan"
            and wp != "PENDING"
            and wp.startswith("http")
        ):

            st.link_button(
                "Join WhatsApp Group",
                wp,
                use_container_width=True
            )

        else:

            st.button(
                "Coming Soon",
                key=f"wp_{row['ShortName']}",
                use_container_width=True
            )

    st.divider()

# ==================================================
# ABOUT
# ==================================================

st.write("")

st.markdown("## About NITwork")

st.write("""
NITwork helps students discover NIT communities,
find official college websites,
and make better counselling decisions.

Built for students, by students.
""")
