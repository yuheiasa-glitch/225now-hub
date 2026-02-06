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
# Style (Force Black background, White & Orange)
# -------------------------------------------------
st.markdown("""
<style>
/* Force app background (Streamlit new UI) */
[data-testid="stAppViewContainer"] {
    background-color: #000000;
    color: #FFFFFF;
}

/* Transparent header bar */
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* Main container spacing */
.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
    max-width: 720px;
}

/* Headings + text */
h1, h2, h3, p, li, span, div {
    color: #FFFFFF;
}

/* Slightly softer body text */
p, li {
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

/* Link buttons */
.stLinkButton > a {
    background-color: transparent;
    border: 1px solid #FF8C00;
    color: #FF8C00 !important;
    padding: 0.6rem 1rem;
    border-radius: 6px;
    margin: 0.25rem 0;
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
    margin: 1.5rem 0;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Header (NO big title)
# -------------------------------------------------
st.markdown("""
<p style="margin:0; opacity:0.85;">
Independent analytical models referenced in selected podcast episodes.<br>
Access is granted individually after payment confirmation.<br><br>
This service supports understanding of analytical frameworks and
<strong>does not constitute investment advice or recommendations</strong>.
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------------------------
# Links
# -------------------------------------------------
st.markdown("### Links")

st.link_button("Podcast", "https://open.spotify.com/show/23KfzDdn2LBuF9tfj2NIsZ")
st.link_button("Model Sample (PDF)", "https://drive.google.com/file/d/1k4QfO36VVqlggO-vFPKo9MymmfnmFnuJ/view?usp=sharing")
st.link_button("Apply for Model Access (Form)", "https://forms.gle/RDmtP9h7ryMuntwQ8")

st.markdown("<br>", unsafe_allow_html=True)

st.link_button("Stripe Payment – Monthly (USD 700)", "https://buy.stripe.com/cNi8wR6Xr9VX4fB0RBfw400")
st.link_button("Stripe Payment – Annual (USD 5,000)", "https://buy.stripe.com/aFa14pgy12tv8vR1VFfw401")

st.markdown("<br>", unsafe_allow_html=True)

st.link_button("Model Access", "https://225now.streamlit.app/")

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
    '<p style="font-size: 0.8rem; opacity: 0.5; margin:0;">© 225NOW</p>',
    unsafe_allow_html=True
)
