# Clip 01 — Eigenvalues and Eigenvectors
# Slide 1
# Initial state: blank
# First interaction: display complete Slide 1

import streamlit as st


# ------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------

st.set_page_config(
    page_title="",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ------------------------------------------------------------
# PRESENTATION STATE
# ------------------------------------------------------------

if "slide_1_visible" not in st.session_state:
    st.session_state.slide_1_visible = False


# ------------------------------------------------------------
# PRESENTATION-STYLE CSS
# ------------------------------------------------------------

st.markdown(
    """
    <style>

    /* Hide Streamlit interface elements */
    #MainMenu,
    footer,
    header,
    [data-testid="stToolbar"],
    [data-testid="stDecoration"] {
        visibility: hidden;
    }

    /* Remove default Streamlit spacing */
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }

    /* Full presentation canvas */
    .slide {
        width: 100%;
        min-height: 100vh;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        box-sizing: border-box;
        padding: 6vh 8vw;

        background: #ffffff;
        text-align: center;
    }

    /* Slide title */
    .slide-title {
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(2.2rem, 4vw, 4.5rem);
        font-weight: 600;
        line-height: 1.2;
        letter-spacing: 0.01em;

        margin-bottom: 7vh;
    }

    /* Byline */
    .by {
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(1.4rem, 2vw, 2.2rem);

        margin-bottom: 1.5vh;
    }

    /* Author */
    .author {
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(1.7rem, 2.5vw, 2.8rem);
        font-weight: 600;

        letter-spacing: 0.02em;
    }

    /*
    Invisible interaction area.

    It occupies the complete presentation canvas,
    but has no visible border, text, or styling.
    */
    div[data-testid="stButton"] button {
        position: fixed;
        inset: 0;

        width: 100vw;
        height: 100vh;

        opacity: 0;
        z-index: 9999;

        cursor: pointer;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------------------------
# INITIAL BLANK STATE
# ------------------------------------------------------------

if not st.session_state.slide_1_visible:

    # Invisible full-screen interaction button.
    # Any mouse click / touch activates Slide 1.

    if st.button("advance", key="advance_slide_1"):
        st.session_state.slide_1_visible = True
        st.rerun()


# ------------------------------------------------------------
# SLIDE 1
# ------------------------------------------------------------

if st.session_state.slide_1_visible:

    st.html(
        """
        <div class="slide">

            <div class="slide-title">
                Welcome to The Essence of Eigenvalues and Eigenvectors
            </div>

            <div class="by">
                By
            </div>

            <div class="author">
                Dr. Dhabalendu Samanta
            </div>

        </div>
        """
    )

