# Clip 01 — Eigenvalues and Eigenvectors
# Slides 1–3 (Finalized up to Slide 3: Clicks 1, 2, and 3)
# 2nd to cimmote to finalize Slide 3: Clicks 1, 2, and 3
import streamlit as st

st.set_page_config(
    page_title="",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.session_state.setdefault("presentation_state", 0)

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

/* LEFT PANEL (40% width area for Observations & Conclusions) */
.slide3-left-panel {
    position: absolute;
    left: 4vw;
    top: 19vh;
    width: 33vw;
    height: 68vh;
    z-index: 30;
    font-family: Georgia, "Times New Roman", serif;
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

/* ==================== 3D FOOTBALL ==================== */

.soccer-ball {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 14vh;
    height: 14vh;
    border-radius: 50%;
    background: #ffffff;
    box-shadow:
        inset -1.2vh -1.2vh 2.5vh rgba(0,0,0,0.55),
        inset 1vh 1vh 2vh rgba(255,255,255,0.9),
        0.8vh 1.4vh 2vh rgba(0,0,0,0.45);
    border: 2px solid #222222;
    overflow: hidden;
    z-index: 25;
}

/* Central Black Pentagon */
.patch-center {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 4.2vh;
    height: 4.2vh;
    background: #111111;
    transform: translate(-50%, -50%);
    clip-path: polygon(50% 0%, 98% 35%, 79% 90%, 21% 90%, 2% 35%);
    box-shadow: 0 0 2px #000;
}

/* Outer Black Pentagons positioned geometrically around the sphere */
.patch-top {
    position: absolute;
    left: 50%;
    top: -1.2vh;
    width: 3.6vh;
    height: 3.6vh;
    background: #111111;
    transform: translateX(-50%);
    clip-path: polygon(50% 100%, 0% 40%, 20% 0%, 80% 0%, 100% 40%);
}

.patch-top-right {
    position: absolute;
    right: -1vh;
    top: 2.8vh;
    width: 3.4vh;
    height: 3.4vh;
    background: #111111;
    clip-path: polygon(0% 40%, 60% 0%, 100% 30%, 80% 100%, 20% 80%);
}

.patch-top-left {
    position: absolute;
    left: -1vh;
    top: 2.8vh;
    width: 3.4vh;
    height: 3.4vh;
    background: #111111;
    clip-path: polygon(100% 40%, 40% 0%, 0% 30%, 20% 100%, 80% 80%);
}

.patch-bottom-right {
    position: absolute;
    right: 0.2vh;
    bottom: -0.6vh;
    width: 3.6vh;
    height: 3.6vh;
    background: #111111;
    clip-path: polygon(30% 0%, 80% 20%, 100% 80%, 40% 100%, 0% 50%);
}

.patch-bottom-left {
    position: absolute;
    left: 0.2vh;
    bottom: -0.6vh;
    width: 3.6vh;
    height: 3.6vh;
    background: #111111;
    clip-path: polygon(70% 0%, 20% 20%, 0% 80%, 60% 100%, 100% 50%);
}

/* 3D Specular Highlight & Shading Layer */
.ball-shading-overlay {
    position: absolute;
    inset: 0;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 30%, rgba(255,255,255,0.45) 0%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.55) 100%);
    pointer-events: none;
}

/* ==================== REVEAL ANIMATION ==================== */

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

/* ==================== FULL SCREEN CLICK CONTROL ==================== */

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

if st.session_state.presentation_state < 20:
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

    # CLICK 1 (State 8): Centered Title + Clean Reserved Left Panel
    content = """
    <div class="slide3">
        <div class="slide3-title">
            Visualization of Soccer Match
        </div>
        <div class="slide3-left-panel"></div>
    """

    # CLICK 2 (State 9): Clean Green Ground on Right Panel (60%)
    if state >= 9:
        reveal = "reveal" if state == 9 else ""
        content += f"""
        <div class="football-ground {reveal}">
            <div class="half-line"></div>
            <div class="centre-circle"></div>
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
        """

        # CLICK 3 (State 10): 3D Black-and-White Soccer Ball at Center
        if state >= 10:
            content += """
            <div class="soccer-ball reveal">
                <div class="patch-center"></div>
                <div class="patch-top"></div>
                <div class="patch-top-right"></div>
                <div class="patch-top-left"></div>
                <div class="patch-bottom-right"></div>
                <div class="patch-bottom-left"></div>
                <div class="ball-shading-overlay"></div>
            </div>
            """

        content += """
        </div>
        """

    content += """
    </div>
    """

    st.html(content)
