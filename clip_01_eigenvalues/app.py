# Clip 01 — Eigenvalues and Eigenvectors

# Slides 1–3

# One action → one visual event

# Cumulative presentation

# Slide 3: Visualization of Soccer Match

import streamlit as st

# ============================================================

# PAGE CONFIGURATION

# ============================================================

st.set_page_config(
page_title="",
page_icon="📐",
layout="wide",
initial_sidebar_state="collapsed",
)

# ============================================================

# PRESENTATION STATE

# ============================================================

# 0  = blank

# 1  = Slide 1

#

# 2  = Slide 2 heading

# 3  = Slide 2 + (i)

# 4  = Slide 2 + (i)-(ii)

# 5  = Slide 2 + (i)-(iii)

# 6  = Slide 2 + (i)-(iv)

# 7  = Slide 2 + (i)-(v)

#

# 8  = Slide 3 heading

# 9  = Slide 3 + football ground

# 10 = Slide 3 + football

# 11 = Slide 3 + P and O

# 12 = Slide 3 + OP arrow

# 13 = First pumping

# 14 = "Visualize Again"

# 15 = Second pumping

# 16 = Observation (i)

# 17 = Observation (ii)

# 18 = Observation (iii)

# 19 = Conclusion (i)

# 20 = Conclusion (ii)

if "presentation_state" not in st.session_state:
st.session_state.presentation_state = 0

# ============================================================

# PRESENTATION CSS

# ============================================================

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


/* ========================================================
   SLIDE 1
   ======================================================== */

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


/* ========================================================
   SLIDE 2
   ======================================================== */

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


/* ========================================================
   SLIDE 3
   ======================================================== */

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
    top: 5vh;
    left: 50%;
    transform: translateX(-50%);
    width: 90vw;
    text-align: center;
    font-size: clamp(2rem, 3.2vw, 3.7rem);
    font-weight: 600;
    line-height: 1.2;
    z-index: 20;
}


/* ========================================================
   FOOTBALL GROUND
   ======================================================== */

.football-ground {
    position: absolute;
    left: 5vw;
    top: 20vh;
    width: 57vw;
    height: 65vh;

    background:
        repeating-linear-gradient(
            90deg,
            #4d9b4d 0px,
            #4d9b4d 45px,
            #55a655 45px,
            #55a655 90px
        );

    border: 5px solid #ffffff;
    border-radius: 1.5vh;

    box-shadow:
        0 1.2vh 2.5vh rgba(0,0,0,0.18),
        inset 0 0 0 2px rgba(0,0,0,0.15);

    overflow: hidden;
    z-index: 5;
}


/* Outer field markings */

.field-line {
    position: absolute;
    border: 3px solid rgba(255,255,255,0.95);
    box-sizing: border-box;
}

.field-boundary {
    inset: 2.5%;
}


/* Halfway line */

.half-line {
    position: absolute;
    left: 50%;
    top: 2.5%;
    width: 3px;
    height: 95%;
    background: rgba(255,255,255,0.95);
    transform: translateX(-50%);
}


/* Centre circle */

.centre-circle {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 19vh;
    height: 19vh;

    border: 3px solid rgba(255,255,255,0.95);
    border-radius: 50%;

    transform: translate(-50%, -50%);
}


/* Centre spot */

.centre-spot {
    position: absolute;
    left: 50%;
    top: 50%;

    width: 1.1vh;
    height: 1.1vh;

    background: #ffffff;
    border-radius: 50%;

    transform: translate(-50%, -50%);
}


/* Penalty areas */

.penalty-area-left {
    position: absolute;
    left: 2.5%;
    top: 28%;
    width: 15%;
    height: 44%;

    border: 3px solid rgba(255,255,255,0.95);
    border-left: none;
    box-sizing: border-box;
}

.penalty-area-right {
    position: absolute;
    right: 2.5%;
    top: 28%;
    width: 15%;
    height: 44%;

    border: 3px solid rgba(255,255,255,0.95);
    border-right: none;
    box-sizing: border-box;
}


/* Goal areas */

.goal-area-left {
    position: absolute;
    left: 2.5%;
    top: 40%;
    width: 7%;
    height: 20%;

    border: 3px solid rgba(255,255,255,0.95);
    border-left: none;
    box-sizing: border-box;
}

.goal-area-right {
    position: absolute;
    right: 2.5%;
    top: 40%;
    width: 7%;
    height: 20%;

    border: 3px solid rgba(255,255,255,0.95);
    border-right: none;
    box-sizing: border-box;
}


/* Penalty spots */

.penalty-spot-left,
.penalty-spot-right {
    position: absolute;

    width: 1vh;
    height: 1vh;

    background: #ffffff;
    border-radius: 50%;

    top: 50%;
    transform: translateY(-50%);
}

.penalty-spot-left {
    left: 13%;
}

.penalty-spot-right {
    right: 13%;
}


/* Goals */

.goal-left,
.goal-right {
    position: absolute;

    top: 42%;
    width: 2.5%;
    height: 16%;

    border: 3px solid #ffffff;
    background: rgba(255,255,255,0.18);

    box-sizing: border-box;
}

.goal-left {
    left: -0.5%;
    border-left: none;
}

.goal-right {
    right: -0.5%;
    border-right: none;
}


/* ========================================================
   THREE-DIMENSIONAL FOOTBALL
   ======================================================== */

.football {
    position: absolute;

    left: 28vw;
    top: 49vh;

    width: 13vh;
    height: 13vh;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 32% 25%,
            #ffffff 0%,
            #ffffff 12%,
            #f1f1f1 30%,
            #d8d8d8 58%,
            #a8a8a8 82%,
            #777777 100%
        );

    border: 2px solid #555555;

    box-shadow:
        inset -1.5vh -1.5vh 2vh rgba(0,0,0,0.30),
        inset 1vh 1vh 1.5vh rgba(255,255,255,0.80),
        0 1.2vh 2vh rgba(0,0,0,0.28);

    z-index: 10;
}


/* Black pentagonal patches */

.football::before {
    content: "";

    position: absolute;

    width: 3.2vh;
    height: 3.2vh;

    left: 50%;
    top: 50%;

    transform: translate(-50%, -50%) rotate(12deg);

    background: #151515;

    clip-path: polygon(
        50% 0%,
        97% 35%,
        79% 91%,
        21% 91%,
        3% 35%
    );

    border-radius: 12%;
}


.football::after {
    content: "";

    position: absolute;

    width: 2.2vh;
    height: 2.2vh;

    left: 22%;
    top: 55%;

    background: #202020;

    clip-path: polygon(
        50% 0%,
        97% 35%,
        79% 91%,
        21% 91%,
        3% 35%
    );

    border-radius: 10%;

    box-shadow:
        6vh -3vh 0 -0.1vh #202020,
        5.2vh 4.2vh 0 -0.1vh #202020,
        -1vh -4.5vh 0 -0.1vh #202020;
}


/* Small shadow beneath football */

.football-shadow {
    position: absolute;

    left: 28.8vw;
    top: 61vh;

    width: 11vh;
    height: 2.8vh;

    background: rgba(0,0,0,0.25);

    border-radius: 50%;

    filter: blur(4px);

    z-index: 8;
}


/* ========================================================
   P, O AND OP — UNCHANGED FOR NOW
   ======================================================== */

.point-p {
    position: absolute;
    left: 31vw;
    top: 45vh;
    font-size: clamp(1.1rem, 1.7vw, 1.8rem);
    font-weight: 700;
    z-index: 15;
    white-space: nowrap;
}

.point-o {
    position: absolute;
    left: 32vw;
    top: 66vh;
    font-size: clamp(1.1rem, 1.7vw, 1.8rem);
    font-weight: 700;
    z-index: 15;
}

.ray {
    position: absolute;
    left: 32.5vw;
    top: 55vh;
    width: 15vw;
    height: 4px;
    background: #222222;
    transform-origin: left center;
    z-index: 12;
}

.ray-arrow {
    position: absolute;
    right: -1px;
    top: -9px;
    font-size: 2rem;
    line-height: 1;
    font-weight: 700;
}


/* ========================================================
   PUMP — UNCHANGED FOR NOW
   ======================================================== */

.pump-panel {
    position: absolute;
    right: 6vw;
    top: 27vh;
    width: 27vw;
    min-height: 35vh;
    text-align: center;
}

.pump-title {
    font-size: clamp(1.5rem, 2.3vw, 2.5rem);
    font-weight: 700;
    margin-bottom: 4vh;
}

.pump {
    position: relative;
    width: 7vw;
    height: 25vh;
    margin: auto;
}

.pump-cylinder {
    position: absolute;
    left: 50%;
    top: 3vh;
    transform: translateX(-50%);
    width: 4vw;
    height: 13vh;
    border: 3px solid #333333;
    border-radius: 1vh;
    background: #eeeeee;
}

.pump-handle {
    position: absolute;
    left: 50%;
    top: 0;
    transform: translateX(-50%);
    width: 8vw;
    height: 3px;
    background: #333333;
}

.pump-rod {
    position: absolute;
    left: 50%;
    top: 0;
    width: 3px;
    height: 5vh;
    background: #333333;
}

.pump-hose {
    position: absolute;
    left: 50%;
    top: 16vh;
    width: 10vw;
    height: 5vh;
    border-bottom: 4px solid #333333;
    border-radius: 0 0 5vw 5vw;
}

.pumping-animation {
    animation: pumpAction 0.9s ease-in-out infinite alternate;
    transform-origin: center;
}

@keyframes pumpAction {
    from {
        transform: translateY(0);
    }
    to {
        transform: translateY(5vh);
    }
}


/* ========================================================
   OBSERVATION / CONCLUSION — UNCHANGED
   ======================================================== */

.analysis-panel {
    position: absolute;
    right: 4vw;
    top: 18vh;
    width: 34vw;
    text-align: left;
    font-size: clamp(1rem, 1.35vw, 1.45rem);
    line-height: 1.4;
    z-index: 30;
}

.analysis-heading {
    font-size: clamp(1.4rem, 2vw, 2.1rem);
    font-weight: 700;
    margin-bottom: 2vh;
}

.analysis-point {
    margin-bottom: 2vh;
}

.analysis-point strong {
    font-weight: 700;
}

.conclusion {
    margin-top: 3vh;
    padding-top: 2vh;
    border-top: 2px solid #dddddd;
}

.visualize-again {
    position: absolute;
    right: 7vw;
    top: 70vh;
    width: 30vw;
    text-align: center;
    font-size: clamp(1.4rem, 2vw, 2rem);
    font-weight: 700;
    z-index: 40;
}


/* ========================================================
   REVEAL ANIMATION
   ======================================================== */

.reveal {
    animation: revealEvent 0.5s ease-out both;
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


/* ========================================================
   INVISIBLE FULL-SCREEN BUTTON
   ======================================================== */

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
```

)

# ============================================================

# ADVANCE PRESENTATION

# ============================================================

if st.session_state.presentation_state < 20:

```
if st.button(
    "advance",
    key=f"advance_{st.session_state.presentation_state}",
):
    st.session_state.presentation_state += 1
    st.rerun()
```

# ============================================================

# STATE 0 — BLANK

# ============================================================

if st.session_state.presentation_state == 0:

```
pass
```

# ============================================================

# STATE 1 — SLIDE 1

# ============================================================

elif st.session_state.presentation_state == 1:

```
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
```

# ============================================================

# STATES 2–7 — SLIDE 2

# ============================================================

elif 2 <= st.session_state.presentation_state <= 7:

```
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
```

# ============================================================

# STATES 8–20 — SLIDE 3

# ============================================================

elif 8 <= st.session_state.presentation_state <= 20:

```
state = st.session_state.presentation_state

content = """
<div class="slide3">

    <div class="slide3-title">
        Visualization of Soccer Match
    </div>
"""


# --------------------------------------------------------
# CLICK 2 — FOOTBALL GROUND
# --------------------------------------------------------

if state >= 9:

    content += """
    <div class="football-ground reveal">

        <div class="field-line field-boundary"></div>

        <div class="half-line"></div>

        <div class="centre-circle"></div>

        <div class="centre-spot"></div>

        <div class="penalty-area-left"></div>
        <div class="penalty-area-right"></div>

        <div class="goal-area-left"></div>
        <div class="goal-area-right"></div>

        <div class="penalty-spot-left"></div>
        <div class="penalty-spot-right"></div>

        <div class="goal-left"></div>
        <div class="goal-right"></div>

    </div>
    """


# --------------------------------------------------------
# CLICK 3 — FOOTBALL
# --------------------------------------------------------

if state >= 10:

    content += """
    <div class="football-shadow reveal"></div>

    <div class="football reveal"></div>
    """


# --------------------------------------------------------
# CLICK 4 — P AND O
# --------------------------------------------------------

if state >= 11:

    content += """
    <div class="point-p reveal">
        P(x,y,z)
    </div>

    <div class="point-o reveal">
        O(0,0,0)
    </div>
    """


# --------------------------------------------------------
# CLICK 5 — OP RAY WITH FRONT ARROW
# --------------------------------------------------------

if state >= 12:

    content += """
    <div class="ray reveal">
        <div class="ray-arrow">▶</div>
    </div>
    """


# --------------------------------------------------------
# CLICK 6 — FIRST PUMPING
# --------------------------------------------------------

if state == 13:

    content += """
    <div class="pump-panel reveal">

        <div class="pump-title">
            Pumping
        </div>

        <div class="pump pumping-animation">

            <div class="pump-handle"></div>

            <div class="pump-rod"></div>

            <div class="pump-cylinder"></div>

            <div class="pump-hose"></div>

        </div>

    </div>
    """


# --------------------------------------------------------
# AFTER FIRST PUMPING — VISUALIZE AGAIN
# --------------------------------------------------------

if state == 14:

    content += """
    <div class="visualize-again reveal">
        Visualize Again
    </div>
    """


# --------------------------------------------------------
# SECOND / FINAL PUMPING
# --------------------------------------------------------

if state >= 15:

    content += """
    <div class="pump-panel reveal">

        <div class="pump-title">
            Pumping
        </div>

        <div class="pump pumping-animation">

            <div class="pump-handle"></div>

            <div class="pump-rod"></div>

            <div class="pump-cylinder"></div>

            <div class="pump-hose"></div>

        </div>

    </div>

    <div class="point-p reveal">
        P(x,y,z)
    </div>

    <div class="point-o reveal">
        O(0,0,0)
    </div>

    <div class="ray reveal">
        <div class="ray-arrow">▶</div>
    </div>
    """


# --------------------------------------------------------
# OBSERVATION PANEL
# --------------------------------------------------------

if state >= 16:

    content += """
    <div class="analysis-panel">

        <div class="analysis-heading">
            Observation:
        </div>
    """

    if state >= 16:

        reveal = "reveal" if state == 16 else ""

        content += f"""
        <div class="analysis-point {reveal}">
            <strong>(i)</strong>
            Throughout the pumping process, the point
            <strong>P</strong> is moving in the direction
            <strong>OP</strong> and finally reaches
            <strong>P'</strong>.
        </div>
        """

    if state >= 17:

        reveal = "reveal" if state == 17 else ""

        content += f"""
        <div class="analysis-point {reveal}">
            <strong>(ii)</strong>
            The point <strong>P</strong> is scaled by a factor of
            <strong>λ = OP'/OP</strong>.
        </div>
        """

    if state >= 18:

        reveal = "reveal" if state == 18 else ""

        content += f"""
        <div class="analysis-point {reveal}">
            <strong>(iii)</strong>
            The point <strong>P</strong> is non-zero.
        </div>
        """

    if state >= 19:

        content += """
        <div class="conclusion">

            <div class="analysis-heading">
                Conclusion:
            </div>
        """

        if state >= 19:

            reveal = "reveal" if state == 19 else ""

            content += f"""
            <div class="analysis-point {reveal}">
                <strong>(i)</strong>
                The non-zero point <strong>P</strong> does not
                change its direction while moving towards
                <strong>P'</strong>, and is therefore defined as
                an <strong>eigenvector</strong> corresponding to
                the eigenvalue <strong>λ</strong>.
            </div>
            """

        if state >= 20:

            reveal = "reveal" if state == 20 else ""

            content += f"""
            <div class="analysis-point {reveal}">
                <strong>(ii)</strong>
                All other points on the surface of the football
                also do not change their direction and are scaled
                by a factor of <strong>λ</strong>. Therefore, they
                are eigenvectors corresponding to the eigenvalue
                <strong>λ</strong>.
            </div>
            """

        content += """
        </div>
        """

    content += """
    </div>
    """

content += """
</div>
"""

st.html(content)
```
