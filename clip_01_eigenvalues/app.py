# Clip 01 — Eigenvalues and Eigenvectors
# Slides 1–3 (Finalized up to Slide 3: Clicks 1, 2, and 3)
# This is first commit using Google Studi AI for slide 3 - Click 1, click 2, Click 3
import streamlit as st
import os
import base64

st.set_page_config(
    page_title="",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.session_state.setdefault("presentation_state", 0)

# Helper function to load tutor photo if available
def get_tutor_photo_html():
    for fname in ["tutor.jpg", "tutor.png", "profile.png", "profile.jpg"]:
        if os.path.exists(fname):
            with open(fname, "rb") as img_file:
                b64_data = base64.b64encode(img_file.read()).decode()
                return f"""
                <div class="tutor-card">
                    <img src="data:image/png;base64,{b64_data}" class="tutor-photo" />
                    <div>
                        <div class="tutor-name">Dr. Dhabalendu Samanta</div>
                        <div class="tutor-sub">Linear Algebra Expert</div>
                    </div>
                </div>
                """
    return """
    <div class="tutor-card">
        <div class="tutor-avatar">👨‍🏫</div>
        <div>
            <div class="tutor-name">Dr. Dhabalendu Samanta</div>
            <div class="tutor-sub">Linear Algebra Expert</div>
        </div>
    </div>
    """

st.markdown(
"""
<style>
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
    font-family: Georgia, "Times New Roman", serif;
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

/* LEFT PANEL (40% width area) */
.slide3-left-panel {
    position: absolute;
    left: 5vw;
    top: 19vh;
    width: 32vw;
    height: 68vh;
    z-index: 30;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

.tutor-card {
    display: flex;
    align-items: center;
    gap: 14px;
    background: #f8fafc;
    border: 1.5px solid #e2e8f0;
    padding: 10px 16px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.tutor-photo {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #2b6cb0;
}

.tutor-avatar {
    font-size: 32px;
}

.tutor-name {
    font-size: 1rem;
    font-weight: 700;
    color: #1a365d;
}

.tutor-sub {
    font-size: 0.8rem;
    color: #4a5568;
}

/* RIGHT PANEL (60% width area): FOOTBALL GROUND */
.football-ground {
    position: absolute;
    left: 40vw;
    top: 19vh;
    width: 55vw;
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

.corner-tl {
    position: absolute;
    left: 0;
    top: 0;
    width: 25px;
    height: 25px;
    border-right: 3px solid rgba(255,255,255,0.95);
    border-bottom: 3px solid rgba(255,255,255,0.95);
    border-radius: 0 0 100% 0;
}

.corner-tr {
    position: absolute;
    right: 0;
    top: 0;
    width: 25px;
    height: 25px;
    border-left: 3px solid rgba(255,255,255,0.95);
    border-bottom: 3px solid rgba(255,255,255,0.95);
    border-radius: 0 0 0 100%;
}

.corner-bl {
    position: absolute;
    left: 0;
    bottom: 0;
    width: 25px;
    height: 25px;
    border-right: 3px solid rgba(255,255,255,0.95);
    border-top: 3px solid rgba(255,255,255,0.95);
    border-radius: 0 100% 0 0;
}

.corner-br {
    position: absolute;
    right: 0;
    bottom: 0;
    width: 25px;
    height: 25px;
    border-left: 3px solid rgba(255,255,255,0.95);
    border-top: 3px solid rgba(255,255,255,0.95);
    border-radius: 100% 0 0 0;
}

/* ==================== FOOTBALL ==================== */

.football {
    position: absolute;
    /* Exact centre of the 60% right football ground */
    left: calc(40vw + 27.5vw);
    top: calc(19vh + 34vh);

    width: 13vh;
    height: 13vh;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 32% 27%,
            #ffffff 0%,
            #ffffff 12%,
            #eeeeee 28%,
            #cfcfcf 58%,
            #8f8f8f 82%,
            #555555 100%
        );

    border: 2px solid #222222;

    box-shadow:
        0.8vh 1vh 1.8vh rgba(0,0,0,0.30),
        inset -1.2vh -1.2vh 2vh rgba(0,0,0,0.22),
        inset 1vh 0.8vh 1.5vh rgba(255,255,255,0.55);

    z-index: 15;

    transform: translate(-50%, -50%);
}

/* Black pentagonal panels */
.football::before {
    content: "";
    position: absolute;
    left: 50%;
    top: 50%;
    width: 3.4vh;
    height: 3.4vh;
    background: #111111;
    clip-path: polygon(
        50% 0%,
        97% 35%,
        79% 90%,
        21% 90%,
        3% 35%
    );
    transform: translate(-50%, -50%);
    box-shadow: 0 0.2vh 0.4vh rgba(0,0,0,0.35);
}

/* Additional black panels */
.football::after {
    content: "";
    position: absolute;
    width: 2.4vh;
    height: 2.4vh;
    left: 1.8vh;
    top: 6.8vh;
    background: #151515;
    clip-path: polygon(
        50% 0%,
        95% 35%,
        78% 90%,
        22% 90%,
        5% 35%
    );
    box-shadow:
        6.4vh -4.2vh 0 -0.1vh #151515,
        5.8vh 3.5vh 0 -0.1vh #151515;
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
# STATES 8–10 — SLIDE 3 (CLICKS 1, 2, 3)
# ============================================================

elif 8 <= st.session_state.presentation_state <= 10:

    state = st.session_state.presentation_state

    # CLICK 1 (State 8): Centered Title + Permanent Left Tutor Photo
    content = f"""
    <div class="slide3">
        <div class="slide3-title">
            Visualization of Soccer Match
        </div>
        <div class="slide3-left-panel">
            {get_tutor_photo_html()}
        </div>
    """

    # CLICK 2 (State 9): Beautiful Green Ground on Right Panel (60%)
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
            <div class="corner-tl"></div>
            <div class="corner-tr"></div>
            <div class="corner-bl"></div>
            <div class="corner-br"></div>
        </div>
        """

    # CLICK 3 (State 10): Black-and-White Football at the Center Mark
    if state >= 10:
        content += """
        <div class="football reveal"></div>
        """

    content += """
    </div>
    """

    st.html(content)
