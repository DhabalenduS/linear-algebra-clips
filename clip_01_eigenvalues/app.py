# Clip 01 — Eigenvalues and Eigenvectors
# Slides 1–2
# One action → one visual event
# Slide 2 uses fixed positioning and cumulative reveal

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

    /* --------------------------------------------------------
       HIDE STREAMLIT INTERFACE
       -------------------------------------------------------- */

    #MainMenu,
    footer,
    header,
    [data-testid="stToolbar"],
    [data-testid="stDecoration"] {
        visibility: hidden;
    }


    /* --------------------------------------------------------
       REMOVE DEFAULT STREAMLIT SPACING
       -------------------------------------------------------- */

    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }


    /* --------------------------------------------------------
       COMMON PRESENTATION CANVAS
       -------------------------------------------------------- */

    .slide {
        width: 100%;
        min-height: 100vh;

        box-sizing: border-box;

        background: #ffffff;
        text-align: center;

        position: relative;

        overflow: hidden;
    }


    /* --------------------------------------------------------
       SLIDE 1
       -------------------------------------------------------- */

    .slide1-content {
        position: absolute;

        top: 50%;
        left: 50%;

        transform: translate(-50%, -50%);

        width: 84vw;
    }

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

    .slide2 {
        width: 100%;
        min-height: 100vh;

        box-sizing: border-box;

        background: #ffffff;

        position: relative;

        overflow: hidden;
    }


    /* --------------------------------------------------------
       FIXED SLIDE 2 HEADING
       -------------------------------------------------------- */

    .slide2-title {
        position: absolute;

        top: 9vh;
        left: 50%;

        transform: translateX(-50%);

        width: 90vw;

        font-family: Georgia, "Times New Roman", serif;

        font-size: clamp(2.2rem, 3.5vw, 4rem);

        font-weight: 600;

        line-height: 1.2;

        text-align: center;
    }


    /* --------------------------------------------------------
       FIXED SLIDE 2 CONTENT AREA
       -------------------------------------------------------- */

    .event-list {
        position: absolute;

        top: 24vh;
        left: 50%;

        transform: translateX(-50%);

        width: min(1100px, 84vw);

        text-align: left;

        font-family: Georgia, "Times New Roman", serif;

        font-size: clamp(1.15rem, 1.8vw, 2rem);

        line-height: 1.45;
    }


    /* --------------------------------------------------------
       INDIVIDUAL EVENT
       -------------------------------------------------------- */

    .event {
        margin: 0 0 2.5vh 0;

        min-height: 10vh;

        display: flex;

        align-items: flex-start;
    }


    .event-number {
        flex: 0 0 4.5rem;

        font-weight: 700;
    }


    .event-text {
        flex: 1;
    }


    .event-emphasis {
        font-weight: 700;
    }


    /* --------------------------------------------------------
       HEADING REVEAL
       -------------------------------------------------------- */

    .heading-reveal {
        animation: headingAppear 0.45s ease-out both;
    }

    @keyframes headingAppear {

        from {
            opacity: 0;
        }

        to {
            opacity: 1;
        }

    }


    /* --------------------------------------------------------
       NEW EVENT REVEAL
       -------------------------------------------------------- */

    .new-event {
        animation: eventAppear 0.45s ease-out both;
    }

    @keyframes eventAppear {

        from {
            opacity: 0;
            transform: translateY(8px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }

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
# STATE 0 — COMPLETELY BLANK
# ------------------------------------------------------------

if st.session_state.presentation_state == 0:

    pass


# ------------------------------------------------------------
# STATE 1 — SLIDE 1
# ------------------------------------------------------------

elif st.session_state.presentation_state == 1:

    st.html(
        """
        <div class="slide">

            <div class="slide1-content">

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

        </div>
        """
    )


# ------------------------------------------------------------
# STATE 2 — SLIDE 2 HEADING ONLY
# ------------------------------------------------------------

elif st.session_state.presentation_state == 2:

    st.html(
        """
        <div class="slide2">

            <div class="slide2-title heading-reveal">
                The Event: Soccer Match
            </div>

        </div>
        """
    )


# ------------------------------------------------------------
# STATES 3–7 — CUMULATIVE SLIDE 2
# ------------------------------------------------------------

elif 3 <= st.session_state.presentation_state <= 7:

    state = st.session_state.presentation_state

    slide2_content = """
        <div class="slide2">

            <div class="slide2-title">
                The Event: Soccer Match
            </div>

            <div class="event-list">
    """


    # --------------------------------------------------------
    # POINT (i)
    # --------------------------------------------------------

    if state >= 3:

        if state == 3:
            reveal_class = "new-event"
        else:
            reveal_class = ""

        slide2_content += f"""
                <div class="event {reveal_class}">

                    <div class="event-number">
                        (i)
                    </div>

                    <div class="event-text">
                        A Soccer match is about to kick off.
                    </div>

                </div>
        """


    # --------------------------------------------------------
    # POINT (ii)
    # --------------------------------------------------------

    if state >= 4:

        if state == 4:
            reveal_class = "new-event"
        else:
            reveal_class = ""

        slide2_content += f"""
                <div class="event {reveal_class}">

                    <div class="event-number">
                        (ii)
                    </div>

                    <div class="event-text">
                        The referee inspects and finds that the air
                        inside the football is insufficient.
                    </div>

                </div>
        """


    # --------------------------------------------------------
    # POINT (iii)
    # --------------------------------------------------------

    if state >= 5:

        if state == 5:
            reveal_class = "new-event"
        else:
            reveal_class = ""

        slide2_content += f"""
                <div class="event {reveal_class}">

                    <div class="event-number">
                        (iii)
                    </div>

                    <div class="event-text event-emphasis">
                        Air is then pumped into the football.
                    </div>

                </div>
        """


    # --------------------------------------------------------
    # POINT (iv)
    # --------------------------------------------------------

    if state >= 6:

        if state == 6:
            reveal_class = "new-event"
        else:
            reveal_class = ""

        slide2_content += f"""
                <div class="event {reveal_class}">

                    <div class="event-number">
                        (iv)
                    </div>

                    <div class="event-text">
                        After a short duration, pumping is successfully
                        completed.
                    </div>

                </div>
        """


    # --------------------------------------------------------
    # POINT (v)
    # --------------------------------------------------------

    if state >= 7:

        if state == 7:
            reveal_class = "new-event"
        else:
            reveal_class = ""

        slide2_content += f"""
                <div class="event {reveal_class}">

                    <div class="event-number">
                        (v)
                    </div>

                    <div class="event-text">
                        The football is now fully ready for the match
                        to kick off.
                    </div>

                </div>
        """


    slide2_content += """
            </div>

        </div>
    """


    st.html(slide2_content)
