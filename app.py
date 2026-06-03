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

/* ===== APP ===== */

.stApp {
    background-color: #020617;
}

/* ===== REMOVE TOP BAR ===== */

header[data-testid="stHeader"] {
    background: #020617;
}

/* ===== HIDE SIDEBAR ===== */

section[data-testid="stSidebar"] {
    display: none;
}

/* ===== HIDE MENU ===== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* ===== PAGE WIDTH ===== */

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
}

/* ===== TEXT ===== */

h1,h2,h3,h4,h5,h6,p {
    color: white !important;
}

/* ===== HERO ===== */

.hero-title{
    text-align:center;
    font-size:80px;
    font-weight:800;
    margin-bottom:0px;
}

.hero-subtitle{
    text-align:center;
    color:#94A3B8;
    font-size:24px;
}

.hero-small{
    text-align:center;
    color:#64748B;
    font-size:18px;
    margin-bottom:40px;
}

/* ===== SEARCH ===== */

.stTextInput input {

    background-color:#0F172A !important;

    color:white !important;

    border:1px solid #334155 !important;

    border-radius:12px !important;

    height:60px !important;

    font-size:18px !important;
}

/* ===== BUTTONS ===== */

.stLinkButton button,
.stButton button {

    background-color:#0F172A !important;

    color:white !important;

    border:1px solid #334155 !important;

    border-radius:10px !important;

    height:48px !important;

    font-weight:600 !important;
}

/* ===== DIVIDERS ===== */

hr {
    border:1px solid #1E293B;
}

/* ===== FOOTER ===== */

.footer{
    text-align:center;
    color:#94A3B8;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HERO
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
# LOAD DATA
# ==================================================

df = pd.read_csv("data/nits.csv")

# ==================================================
# SEARCH BAR
# ==================================================

left, center, right = st.columns([1,5,1])

with center:

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

# ==================================================
# TITLE
# ==================================================

st.markdown("## 🏛 Browse All NITs")

st.write("")

# ==================================================
# NIT LIST
# ==================================================

for _, row in df.iterrows():

    col1, col2, col3 = st.columns([8, 1.5, 2.5])

    # College Info

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
st.write("")

st.markdown("## About NITwork")

st.write("""
NITwork helps students discover NIT communities,
find official college websites,
and make better counselling decisions.

Built for students, by students.
""")

# ==================================================
# FOOTER
# ==================================================

st.write("---")

st.markdown("""
<div class='footer'>

<h4>Built by Gauri 🚀</h4>

<a href='https://www.linkedin.com/in/gauri-92359a270/'
target='_blank'
style='color:#38BDF8;text-decoration:none;'>

Connect on LinkedIn

</a>

</div>
""", unsafe_allow_html=True)
