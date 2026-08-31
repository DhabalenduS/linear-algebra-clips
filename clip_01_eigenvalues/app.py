# Clip 01 — Eigenvalues and Eigenvectors
# This commit is just to re-ansure the code. 
# Slides 1–3

# Stable Slides 1–2 + first three visual events of Slide 3

import streamlit as st

st.set_page_config(
page_title="",
page_icon="📐",
layout="wide",
initial_sidebar_state="collapsed",
)

st.session_state.setdefault("presentation_state", 0)

st.markdown(
""" <style>

```
#MainMenu,
footer,
header,
[data-testid="stToolbar"],
[data-testid="stDecoration"] {
    visibility: hidden;
}

.block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}

.slide {
    width: 100%;
    min-height: 100vh;
    box-sizing: border-box;
    background: #ffffff;
    position: relative;
    overflow: hidden;
    font-family: Georgia, "Times New Roman", serif;
}

/* ==================== SLIDE 1 ==================== */

.slide1-content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 84vw;
    text-align: center;
}

.slide-title {
    font-size: clamp(2.2rem, 4vw, 4.5rem);
    font-weight: 600;
    line-height: 1.2;
    letter-spacing: 0.01em;
    margin-bottom: 7vh;
}

.by {
    font-size: clamp(1.4rem, 2vw, 2.2rem);
    margin-bottom: 1.5vh;
}

.author {
    font-size: clamp(1.7rem, 2.5vw, 2.8rem);
    font-weight: 600;
    letter-spacing: 0.02em;
}

/* ==================== SLIDE 2 ==================== */

.slide2 {
    width: 100%;
    min-height: 100vh;
    box-sizing: border-box;
    background: #ffffff;
    position: relative;
    overflow: hidden;
}

.slide2-title {
    position: absolute;
    top: 9vh;
    left: 50%;
    transform: translateX(-50%);
    width: 90vw;
    font-size: clamp(2.2rem, 3.5vw, 4rem);
    font-weight: 600;
    line-height: 1.2;
    text-align: center;
}

.event-list {
    position: absolute;
    top: 24vh;
    left: 50%;
    transform: translateX(-50%);
    width: min(1100px, 84vw);
    text-align: left;
    font-size: clamp(1.15rem, 1.8vw, 2rem);
    line-height: 1.45;
}

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

/* ==================== SLIDE 3 ==================== */

.slide3 {
    width: 100%;
    min-height: 100vh;
    box-sizing: border-box;
    background: #ffffff;
    position: relative;
    overflow: hidden;
}

.slide3-title {
    position: absolute;
    top: 6vh;
    left: 50%;
    transform: translateX(-50%);
    width: 90vw;
    text-align: center;
    font-size: clamp(2rem, 3.2vw, 3.7rem);
    font-weight: 600;
    line-height: 1.2;
    z-index: 20;
}

/* ==================== FOOTBALL GROUND ==================== */

.football-ground {
    position: absolute;
    left: 7vw;
    top: 19vh;
    width: 66vw;
    height: 68vh;

    background:
        repeating-linear-gradient(
            90deg,
            #3f963f 0px,
            #3f963f 55px,
            #459e45 55px,
            #459e45 110px
        );

    border: 5px solid #ffffff;
    border-radius: 2vh;

    box-shadow:
        0 1.5vh 3vh rgba(0,0,0,0.18),
        inset 0 0 0 2px rgba(0,0,0,0.12);

    overflow: hidden;
    z-index: 5;
}

.half-line {
    position: absolute;
    left: 50%;
    top: 0;
    width: 3px;
    height: 100%;
    background: rgba(255,255,255,0.95);
    transform: translateX(-50%);
}

.centre-circle {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 17vh;
    height: 17vh;
    border: 3px solid rgba(255,255,255,0.95);
    border-radius: 50%;
    transform: translate(-50%, -50%);
}

.centre-spot {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 10px;
    height: 10px;
    background: #ffffff;
    border-radius: 50%;
    transform: translate(-50%, -50%);
}

.penalty-area-left {
    position: absolute;
    left: 0;
    top: 27%;
    width: 16%;
    height: 46%;
    border: 3px solid rgba(255,255,255,0.95);
    border-left: none;
    box-sizing: border-box;
}

.penalty-area-right {
    position: absolute;
    right: 0;
    top: 27%;
    width: 16%;
    height: 46%;
    border: 3px solid rgba(255,255,255,0.95);
    border-right: none;
    box-sizing: border-box;
}

.goal-area-left {
    position: absolute;
    left: 0;
    top: 37%;
    width: 7%;
    height: 26%;
    border: 3px solid rgba(255,255,255,0.95);
    border-left: none;
    box-sizing: border-box;
}

.goal-area-right {
    position: absolute;
    right: 0;
    top: 37%;
    width: 7%;
    height: 26%;
    border: 3px solid rgba(255,255,255,0.95);
    border-right: none;
    box-sizing: border-box;
}

.goal-left {
    position: absolute;
    left: -1.2%;
    top: 43%;
    width: 1.5%;
    height: 14%;
    border: 3px solid #ffffff;
    background: rgba(255,255,255,0.12);
    box-sizing: border-box;
}

.goal-right {
    position: absolute;
    right: -1.2%;
    top: 43%;
    width: 1.5%;
    height: 14%;
    border: 3px solid #ffffff;
    background: rgba(255,255,255,0.12);
    box-sizing: border-box;
}

/* ==================== FOOTBALL ==================== */

.football {
    position: absolute;
    left: 39vw;
    top: 49vh;
    width: 13vh;
    height: 13vh;
    border-radius: 50%;

    background:
        radial-gradient(
            circle at 31% 28%,
            #ffffff 0%,
            #ffffff 32%,
            transparent 33%
        ),
        radial-gradient(
            circle at 70% 70%,
            #d8d8d8 0%,
            #f5f5f5 58%,
            #bdbdbd 100%
        );

    border: 2px solid #222222;

    box-shadow:
        0 1vh 2vh rgba(0,0,0,0.28);

    z-index: 15;
}

.football-patch {
    position: absolute;
    width: 2.8vh;
    height: 2.8vh;
    background: #151515;

    clip-path: polygon(
        50% 0%,
        95% 35%,
        78% 90%,
        22% 90%,
        5% 35%
    );
}

.patch-1 {
    left: 5vh;
    top: 4.7vh;
}

.patch-2 {
    left: 2.2vh;
    top: 7.8vh;
}

.patch-3 {
    left: 8.1vh;
    top: 8vh;
}

.patch-4 {
    left: 5.1vh;
    top: 9.5vh;
}

/* ==================== REVEAL ==================== */

.reveal {
    animation: revealEvent 0.55s ease-out both;
}

@keyframes revealEvent {
    from {
        opacity: 0;
        transform: translateY(10px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* ==================== FULL SCREEN CONTROL ==================== */

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

# ============================================================

# ADVANCE PRESENTATION

# ============================================================

if st.session_state.presentation_state < 10:
    if st.button(
        "advance",
        key="advance_button",
    ):
        st.session_state.presentation_state += 1
        st.rerun()

# ============================================================

# STATE 0 — BLANK

# ============================================================

if st.session_state.presentation_state == 0:
    pass

# ============================================================
# STATE 1 — SLIDE 1
# ============================================================

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

# ============================================================
# STATES 2–7 — SLIDE 2
# ============================================================

elif 2 <= st.session_state.presentation_state <= 7:

    state = st.session_state.presentation_state

    content = """
    <div class="slide2">

        <div class="slide2-title">
            The Event: Soccer Match
        </div>

        <div class="event-list">
    """

    if state >= 3:

        reveal = "reveal" if state == 3 else ""

        content += f"""
            <div class="event {reveal}">
                <div class="event-number">(i)</div>
                <div class="event-text">
                    A Soccer match is about to kick off.
                </div>
            </div>
        """

    if state >= 4:

        reveal = "reveal" if state == 4 else ""

        content += f"""
            <div class="event {reveal}">
                <div class="event-number">(ii)</div>
                <div class="event-text">
                    The referee inspects and finds that the air
                    inside the football is insufficient.
                </div>
            </div>
        """

    if state >= 5:

        reveal = "reveal" if state == 5 else ""

        content += f"""
            <div class="event {reveal}">
                <div class="event-number">(iii)</div>
                <div class="event-text event-emphasis">
                    Air is then pumped into the football.
                </div>
            </div>
        """

    if state >= 6:

        reveal = "reveal" if state == 6 else ""

        content += f"""
            <div class="event {reveal}">
                <div class="event-number">(iv)</div>
                <div class="event-text">
                    After a short duration, pumping is successfully
                    completed.
                </div>
            </div>
        """

    if state >= 7:

        reveal = "reveal" if state == 7 else ""

        content += f"""
            <div class="event {reveal}">
                <div class="event-number">(v)</div>
                <div class="event-text">
                    The football is now fully ready for the match
                    to kick off.
                </div>
            </div>
        """

    content += """
        </div>
    </div>
    """

    st.html(content)

# ============================================================
# STATES 8–10 — SLIDE 3
# ============================================================

elif 8 <= st.session_state.presentation_state <= 10:

    state = st.session_state.presentation_state

    content = """
    <div class="slide3">

        <div class="slide3-title">
            Visualization of Soccer Match
        </div>
    """

    # ========================================================
    # CLICK 2 — FOOTBALL GROUND
    # ========================================================

    if state >= 9:

        reveal = "reveal" if state == 9 else ""

        content += f"""
        <div class="football-ground {reveal}">

            <div class="half-line"></div>

            <div class="centre-circle"></div>

            <div class="centre-spot"></div>

            <div class="penalty-area-left"></div>

            <div class="penalty-area-right"></div>

            <div class="goal-area-left"></div>

            <div class="goal-area-right"></div>

            <div class="goal-left"></div>

            <div class="goal-right"></div>

        </div>
        """

    # ========================================================
    # CLICK 3 — FOOTBALL
    # ========================================================

    if state >= 10:

        content += """
        <div class="football reveal">

            <div class="football-patch patch-1"></div>

            <div class="football-patch patch-2"></div>

            <div class="football-patch patch-3"></div>

            <div class="football-patch patch-4"></div>

        </div>
        """

    content += """
    </div>
    """

    st.html(content)
