# Clip 01 — Eigenvalues and Eigenvectors
# Slides 1–2
# Initial state: blank
# One interaction: advance by one presentation event

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

if "presentation_state" not in st.session_state:
    st.session_state.presentation_state = 0


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

    /* --------------------------------------------------------
       SLIDE 1
       -------------------------------------------------------- */

    .slide-title {
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(2.2rem, 4vw, 4.5rem);
        font-weight: 600;
        line-height: 1.2;
        letter-spacing: 0.01em;

        margin-bottom: 7vh;
    }

    .by {
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(1.4rem, 2vw, 2.2rem);

        margin-bottom: 1.5vh;
    }

    .author {
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(1.7rem, 2.5vw, 2.8rem);
        font-weight: 600;

        letter-spacing: 0.02em;
    }

    /* --------------------------------------------------------
       SLIDE 2
       -------------------------------------------------------- */

    .slide2-title {
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(2.2rem, 3.5vw, 4rem);
        font-weight: 600;
        line-height: 1.2;

        margin-bottom: 5vh;
    }

    .event-list {
        width: min(1100px, 88vw);

        text-align: left;

        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(1.15rem, 1.8vw, 2rem);
        line-height: 1.55;
    }

    .event {
        margin-bottom: 2.2vh;
    }

    .event strong {
        font-weight: 700;
    }

    /* --------------------------------------------------------
       INVISIBLE FULL-SCREEN INTERACTION AREA
       -------------------------------------------------------- */

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
# ONE-ACTION ADVANCE CONTROL
# ------------------------------------------------------------

# The invisible button is present after Slide 1 appears.
# Each click/tap advances exactly one presentation state.

if st.session_state.presentation_state >= 1:

    if st.button(
        "advance",
        key=f"advance_{st.session_state.presentation_state}",
    ):
        st.session_state.presentation_state += 1
        st.rerun()


# ------------------------------------------------------------
# INITIAL BLANK STATE
# ------------------------------------------------------------

if st.session_state.presentation_state == 0:

    # Completely blank presentation screen.
    # First click/touch reveals Slide 1.

    if st.button("start", key="start_presentation"):
        st.session_state.presentation_state = 1
        st.rerun()


# ------------------------------------------------------------
# SLIDE 1
# ------------------------------------------------------------

elif st.session_state.presentation_state == 1:

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


# ------------------------------------------------------------
# SLIDE 2
# ------------------------------------------------------------

elif st.session_state.presentation_state == 2:

    st.html(
        """
        <div class="slide">

            <div class="slide2-title">
                The Event: Soccer Match
            </div>

            <div class="event-list">

                <div class="event">
                    <strong>(i)</strong>
                    A Soccer match is about to kick off.
                </div>

                <div class="event">
                    <strong>(ii)</strong>
                    The referee inspects and finds that the air
                    inside the football is insufficient.
                </div>

                <div class="event">
                    <strong>(iii)</strong>
                    <strong>Air is then pumped into the football.</strong>
                </div>

                <div class="event">
                    <strong>(iv)</strong>
                    After a short duration, pumping is successfully
                    completed.
                </div>

                <div class="event">
                    <strong>(v)</strong>
                    The football is now fully ready for the match
                    to kick off.
                </div>

            </div>

        </div>
        """
    )

