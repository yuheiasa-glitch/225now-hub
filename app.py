import streamlit as st

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="225NOW",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------
# Style (Black background, White & Orange)
# -------------------------------------------------
st.markdown("""
<style>
/* Base */
html, body, [class*="css"] {
    background-color: #000000;
    color: #FFFFFF;
}

/* Container spacing */
.block-container {
    padding-top: 4rem;
    padding-bottom: 4rem;
    max-width: 720px;
}

/* Headings */
h1, h2, h3 {
    color: #FFFFFF;
    letter-spacing: 0.04em;
}

/* Text */
p, li {
    color: #FFFFFF;
    opacity: 0.9;
}

/* Links */
a {
    color: #FF8C00 !important;
    text-decoration: none;
    font-weight: 500;
}
a:hover {
    text-decoration: underline;
}

/* Buttons */
.stLinkButton > a {
    background-color: transparent;
    border: 1px solid #FF8C00;
    color: #FF8C00 !important;
    padding: 0.6rem 1rem;
    border-radius: 6px;
    margin: 0.2rem 0;
    width: 100%;
    text-align: center;
}
.stLinkButton > a:hover {
    background-color: #FF8C00;
    color: #000000 !important;
}

/* Divider */
hr {
    border: none;
    border-top: 1px solid #222222;
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Header
# -------------------------------------------------
st.title("225NOW")

st.markdown("""
Independent analytical models referenced in selected podcast episodes.  
Access to the models is granted individually after payment confirmation.

This service supports understanding of analytical frameworks  
and **does not constitute investment advice or recommendations**.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------------------------
# Links
# -------------------------------------------------
st.markdown("### Links")

st.link_button(
    "Podcast",
    "https://open.spotify.com/show/23KfzDdn2LBuF9tfj2NIsZ"
)

st.link_button(
    "Model Sample (PDF)",
    "https://drive.google.com/file/d/1k4QfO36VVqlggO-vFPKo9MymmfnmFnuJ/view?usp=sharing"
)

st.link_button(
    "Apply for Model Access (Form)",
    "https://forms.gle/RDmtP9h7ryMuntwQ8"
)

st.markdown("<br>", unsafe_allow_html=True)

st.link_button(
    "Stripe Payment – Monthly (USD 700)",
    "https://buy.stripe.com/cNi8wR6Xr9VX4fB0RBfw400"
)

st.link_button(
    "Stripe Payment – Annual (USD 5,000)",
    "https://buy.stripe.com/aFa14pgy12tv8vR1VFfw401"
)

st.markdown("<br>", unsafe_allow_html=True)

st.link_button(
    "Model Access",
    "https://225now.streamlit.app/"
)

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------------------------
# Legal
# -------------------------------------------------
st.markdown("### Legal")
st.page_link("pages/tokusho.py", label="Specified Commercial Transactions Act")


# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    '<p style="font-size: 0.8rem; opacity: 0.5;">'
    '© 225NOW</p>',
    unsafe_allow_html=True
)


