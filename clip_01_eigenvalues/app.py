# Clip 01 — Eigenvalues and Eigenvectors
# Slides 1–2
# One action → one visual event
# Slide 2 uses cumulative content reveal

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

# State 0 = blank
# State 1 = complete Slide 1
# State 2 = Slide 2 heading
# State 3 = Slide 2 + point (i)
# State 4 = Slide 2 + points (i)–(ii)
# State 5 = Slide 2 + points (i)–(iii)
# State 6 = Slide 2 + points (i)–(iv)
# State 7 = complete Slide 2

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
# ADVANCE PRESENTATION
# ------------------------------------------------------------

if st.session_state.presentation_state < 7:

    if st.button(
        "advance",
        key=f"advance_{st.session_state.presentation_state}",
    ):
        st.session_state.presentation_state += 1
        st.rerun()


# ------------------------------------------------------------
# STATE 0 — BLANK
# ------------------------------------------------------------

if st.session_state.presentation_state == 0:

    # Completely blank screen.
    # The invisible button above waits for the first interaction.

    pass


# ------------------------------------------------------------
# STATE 1 — SLIDE 1
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
# STATES 2–7 — SLIDE 2 CUMULATIVE BUILD
# ------------------------------------------------------------

elif 2 <= st.session_state.presentation_state <= 7:

    state = st.session_state.presentation_state

    # Heading is always visible from State 2 onward.

    slide2_content = """
        <div class="slide">

            <div class="slide2-title">
                The Event: Soccer Match
            </div>

            <div class="event-list">
    """

    # --------------------------------------------------------
    # POINT (i)
    # --------------------------------------------------------

    if state >= 3:
        slide2_content += """
                <div class="event">
                    <strong>(i)</strong>
                    A Soccer match is about to kick off.
                </div>
        """

    # --------------------------------------------------------
    # POINT (ii)
    # --------------------------------------------------------

    if state >= 4:
        slide2_content += """
                <div class="event">
                    <strong>(ii)</strong>
                    The referee inspects and finds that the air
                    inside the football is insufficient.
                </div>
        """

    # --------------------------------------------------------
    # POINT (iii)
    # --------------------------------------------------------

    if state >= 5:
        slide2_content += """
                <div class="event">
                    <strong>(iii)</strong>
                    <strong>Air is then pumped into the football.</strong>
                </div>
        """

    # --------------------------------------------------------
    # POINT (iv)
    # --------------------------------------------------------

    if state >= 6:
        slide2_content += """
                <div class="event">
                    <strong>(iv)</strong>
                    After a short duration, pumping is successfully
                    completed.
                </div>
        """

    # --------------------------------------------------------
    # POINT (v)
    # --------------------------------------------------------

    if state >= 7:
        slide2_content += """
                <div class="event">
                    <strong>(v)</strong>
                    The football is now fully ready for the match
                    to kick off.
                </div>
        """

    slide2_content += """
            </div>

        </div>
    """

    st.html(slide2_content)
