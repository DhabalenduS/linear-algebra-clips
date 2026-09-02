# Clip 01 — Eigenvalues and Eigenvectors
# Slides 1–3 (Finalizing up to Slide 3: Clicks 1, 2, and 3)
# 1st Commit to Finalize up to Slide 3: Clicks 1, 2, and 3
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

/* LEFT PANEL (40% width area reserved for Observations & Conclusions) */
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

/* ==================== 3D FOOTBALL ==================== */

.football-container {
    position: absolute;
    /* Exactly at the centre of the soccer ground */
    left: calc(40vw + 27.5vw);
    top: calc(19vh + 34vh);
    width: 14vh;
    height: 14vh;
    transform: translate(-50%, -50%);
    z-index: 15;
    filter: drop-shadow(0.8vh 1.2vh 1.4vh rgba(0,0,0,0.38));
}

.football-svg {
    width: 100%;
    height: 100%;
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

    # CLICK 1 (State 8): Centered Title + Clean Reserved Left Panel
    content = """
    <div class="slide3">
        <div class="slide3-title">
            Visualization of Soccer Match
        </div>
        <div class="slide3-left-panel"></div>
    """

    # CLICK 2 (State 9): Green Football Pitch on Right Panel (60%)
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

    # CLICK 3 (State 10): 3D Black-and-White Soccer Ball at Center
    if state >= 10:
        content += """
        <div class="football-container reveal">
            <svg class="football-svg" viewBox="0 0 200 200">
                <defs>
                    <!-- Spherical 3D Shading -->
                    <radialGradient id="ballShading" cx="35%" cy="30%" r="65%">
                        <stop offset="0%" stop-color="#ffffff" stop-opacity="0.9" />
                        <stop offset="50%" stop-color="#dddddd" stop-opacity="0.2" />
                        <stop offset="85%" stop-color="#222222" stop-opacity="0.6" />
                        <stop offset="100%" stop-color="#050505" stop-opacity="0.95" />
                    </radialGradient>
                    <clipPath id="ballClip">
                        <circle cx="100" cy="100" r="96" />
                    </clipPath>
                </defs>

                <!-- Base Sphere Background -->
                <circle cx="100" cy="100" r="96" fill="#f4f4f4" stroke="#222222" stroke-width="3" />

                <!-- Classic Soccer Ball Geometry (Clipped to Sphere) -->
                <g clip-path="url(#ballClip)">
                    <!-- Central Pentagonal Patch -->
                    <polygon points="100,68 126,86 116,118 84,118 74,86" fill="#181818" stroke="#333" stroke-width="2"/>

                    <!-- Seam Lines radiating outward from center pentagon -->
                    <line x1="100" y1="68" x2="100" y2="30" stroke="#444" stroke-width="3.5" stroke-linecap="round"/>
                    <line x1="126" y1="86" x2="162" y2="72" stroke="#444" stroke-width="3.5" stroke-linecap="round"/>
                    <line x1="116" y1="118" x2="148" y2="152" stroke="#444" stroke-width="3.5" stroke-linecap="round"/>
                    <line x1="84" y1="118" x2="52" y2="152" stroke="#444" stroke-width="3.5" stroke-linecap="round"/>
                    <line x1="74" y1="86" x2="38" y2="72" stroke="#444" stroke-width="3.5" stroke-linecap="round"/>

                    <!-- Surrounding Outer Black Pentagons (Spherical Perspective) -->
                    <!-- Top Patch -->
                    <polygon points="82,0 118,0 126,20 100,30 74,20" fill="#181818" stroke="#333" stroke-width="2"/>
                    <!-- Top-Right Patch -->
                    <polygon points="162,72 188,52 205,75 190,105 168,102" fill="#181818" stroke="#333" stroke-width="2"/>
                    <!-- Bottom-Right Patch -->
                    <polygon points="148,152 172,142 180,178 145,200 125,182" fill="#181818" stroke="#333" stroke-width="2"/>
                    <!-- Bottom-Left Patch -->
                    <polygon points="52,152 75,182 55,200 20,178 28,142" fill="#181818" stroke="#333" stroke-width="2"/>
                    <!-- Top-Left Patch -->
                    <polygon points="38,72 32,102 10,105 -5,75 12,52" fill="#181818" stroke="#333" stroke-width="2"/>

                    <!-- Additional Hexagonal Seam Lines Connecting Outer Panels -->
                    <line x1="74" y1="20" x2="38" y2="72" stroke="#444" stroke-width="3.5"/>
                    <line x1="126" y1="20" x2="162" y2="72" stroke="#444" stroke-width="3.5"/>
                    <line x1="168" y1="102" x2="148" y2="152" stroke="#444" stroke-width="3.5"/>
                    <line x1="125" y1="182" x2="75" y2="182" stroke="#444" stroke-width="3.5"/>
                    <line x1="52" y1="152" x2="32" y2="102" stroke="#444" stroke-width="3.5"/>

                    <!-- 3D Volume Light & Shadow Overlay -->
                    <circle cx="100" cy="100" r="96" fill="url(#ballShading)" style="mix-blend-mode: multiply;" />
                </g>
            </svg>
        </div>
        """

    content += """
    </div>
    """

    st.html(content)
