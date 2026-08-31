# Clip 01 — Eigenvalues and Eigenvectors

# Slides 1–3

# One action → one visual event

# Slide 2 uses fixed positioning and cumulative reveal

# Slide 3 uses cumulative soccer visualization

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

# State 0  = blank

# State 1  = complete Slide 1

#

# State 2  = Slide 2 heading

# State 3  = Slide 2 + point (i)

# State 4  = Slide 2 + points (i)–(ii)

# State 5  = Slide 2 + points (i)–(iii)

# State 6  = Slide 2 + points (i)–(iv)

# State 7  = complete Slide 2

#

# State 8  = Slide 3 heading

# State 9  = football ground

# State 10 = football

# State 11 = P and O

# State 12 = OP ray

# State 13 = first pumping

# State 14 = Visualize Again

# State 15 = second pumping

# State 16 = Observation heading

# State 17 = Observation point 1

# State 18 = Observation point 2

# State 19 = Observation point 3

# State 20 = Conclusion heading

# State 21 = Conclusion point 1

# State 22 = Conclusion point 2

# State 23 = Conclusion point 3

# State 24 = complete Slide 3

if "presentation_state" not in st.session_state:
st.session_state.presentation_state = 0

# ------------------------------------------------------------

# PRESENTATION-STYLE CSS

# ------------------------------------------------------------

st.markdown(
""" <style>

```
/* ========================================================
   HIDE STREAMLIT INTERFACE
   ======================================================== */

#MainMenu,
footer,
header,
[data-testid="stToolbar"],
[data-testid="stDecoration"] {
    visibility: hidden;
}


/* ========================================================
   REMOVE DEFAULT STREAMLIT SPACING
   ======================================================== */

.block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}


/* ========================================================
   COMMON PRESENTATION CANVAS
   ======================================================== */

.slide {
    width: 100%;
    min-height: 100vh;
    box-sizing: border-box;
    background: #ffffff;
    text-align: center;
    position: relative;
    overflow: hidden;
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

    font-family: Georgia, "Times New Roman", serif;
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

    font-family: Georgia, "Times New Roman", serif;
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
   SLIDE 2 REVEAL
   ======================================================== */

.heading-reveal,
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


/* --------------------------------------------------------
   SLIDE 3 TITLE
   -------------------------------------------------------- */

.slide3-title {
    position: absolute;

    top: 5vh;
    left: 50%;

    transform: translateX(-50%);

    width: 92vw;

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(2rem, 3.4vw, 3.8rem);

    font-weight: 600;

    line-height: 1.2;

    text-align: center;

    z-index: 100;
}


/* --------------------------------------------------------
   MAIN VISUAL
   -------------------------------------------------------- */

.visual-area {
    position: absolute;

    left: 5vw;
    right: 5vw;

    top: 15vh;
    height: 46vh;

    overflow: hidden;
}


/* --------------------------------------------------------
   GREEN FOOTBALL GROUND
   -------------------------------------------------------- */

.football-ground {
    position: absolute;

    left: 4%;
    right: 4%;

    bottom: 0;

    height: 52%;

    background: #4c9a45;

    border-radius: 48% 48% 0 0 / 35% 35% 0 0;

    box-shadow:
        inset 0 8px 0 rgba(255,255,255,0.12),
        inset 0 -14px 24px rgba(0,0,0,0.12);
}


/* --------------------------------------------------------
   FIELD MARKINGS
   -------------------------------------------------------- */

.field-line {
    position: absolute;

    left: 11%;
    right: 11%;

    bottom: 18%;

    height: 2px;

    background: rgba(255,255,255,0.82);
}

.field-circle {
    position: absolute;

    left: 50%;
    bottom: 2%;

    transform: translateX(-50%);

    width: 150px;
    height: 70px;

    border: 2px solid rgba(255,255,255,0.80);

    border-radius: 50%;
}


/* --------------------------------------------------------
   FOOTBALL
   -------------------------------------------------------- */

.football {
    position: absolute;

    left: 50%;
    top: 37%;

    width: 118px;
    height: 118px;

    transform: translate(-50%, -50%);

    z-index: 30;

    filter:
        drop-shadow(0 10px 7px rgba(0,0,0,0.24));
}


/* --------------------------------------------------------
   FOOTBALL PUMPING
   -------------------------------------------------------- */

.pump-first {
    animation: pumpFirst 2.8s ease-in-out forwards;
}

.pump-second {
    animation: pumpSecond 2.8s ease-in-out forwards;
}

@keyframes pumpFirst {

    0% {
        transform:
            translate(-50%, -50%)
            scale(1);
    }

    45% {
        transform:
            translate(-50%, -50%)
            scale(1.08);
    }

    100% {
        transform:
            translate(-50%, -50%)
            scale(1.22);
    }
}

@keyframes pumpSecond {

    0% {
        transform:
            translate(-50%, -50%)
            scale(1.22);
    }

    45% {
        transform:
            translate(-50%, -50%)
            scale(1.29);
    }

    100% {
        transform:
            translate(-50%, -50%)
            scale(1.34);
    }
}


/* --------------------------------------------------------
   ORIGIN
   -------------------------------------------------------- */

.origin {
    position: absolute;

    left: calc(50% - 18px);

    top: calc(37% + 70px);

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(0.85rem, 1.15vw, 1.25rem);

    font-weight: 700;

    z-index: 50;
}


/* --------------------------------------------------------
   RAYS
   -------------------------------------------------------- */

.ray {
    position: absolute;

    height: 4px;

    background: #111111;

    transform-origin: left center;

    border-radius: 5px;

    z-index: 45;
}


/*
   Arrowhead is at the FRONT / END of the ray.
*/

.ray::after {
    content: "";

    position: absolute;

    right: -2px;

    top: 50%;

    transform: translateY(-50%);

    width: 0;
    height: 0;

    border-top: 9px solid transparent;

    border-bottom: 9px solid transparent;

    border-left: 16px solid #111111;
}


.ray-op {
    left: 50%;

    top: 37%;

    width: 150px;
}


.ray-opp {
    left: 50%;

    top: 37%;

    width: 255px;
}


/* --------------------------------------------------------
   POINT LABELS
   -------------------------------------------------------- */

.point {
    position: absolute;

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(0.9rem, 1.25vw, 1.3rem);

    font-weight: 600;

    white-space: nowrap;

    z-index: 55;
}


.point-p {
    left: calc(50% + 150px);

    top: calc(37% - 38px);
}


.point-pp {
    left: calc(50% + 255px);

    top: calc(37% - 38px);
}


/* --------------------------------------------------------
   PUMPING LABEL
   -------------------------------------------------------- */

.pumping-label {
    position: absolute;

    left: 50%;

    bottom: 2%;

    transform: translateX(-50%);

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(1.1rem, 1.7vw, 1.8rem);

    font-weight: 600;

    letter-spacing: 0.03em;

    z-index: 80;
}


.pumping-pulse {
    animation: pumpingPulse 0.7s ease-in-out infinite alternate;
}

@keyframes pumpingPulse {

    from {
        opacity: 0.55;
    }

    to {
        opacity: 1;
    }
}


/* --------------------------------------------------------
   VISUALIZE AGAIN
   -------------------------------------------------------- */

.visualize-again {
    position: absolute;

    left: 50%;
    top: 38%;

    transform: translate(-50%, -50%);

    padding: 1.2vh 2.2vw;

    background: rgba(255,255,255,0.96);

    border-radius: 12px;

    box-shadow:
        0 5px 22px rgba(0,0,0,0.16);

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(1.4rem, 2.3vw, 2.5rem);

    font-weight: 600;

    letter-spacing: 0.03em;

    z-index: 200;
}


/* ========================================================
   OBSERVATION / CONCLUSION
   ======================================================== */

.explanation {
    position: absolute;

    left: 6vw;
    right: 6vw;

    top: 64vh;
    bottom: 3vh;

    display: flex;

    gap: 5vw;

    align-items: flex-start;

    z-index: 90;
}


.observation,
.conclusion {
    flex: 1;

    font-family: Georgia, "Times New Roman", serif;

    text-align: left;
}


.section-heading {
    font-size: clamp(1.25rem, 1.75vw, 1.9rem);

    font-weight: 700;

    margin-bottom: 1.0vh;
}


.explanation-point {
    font-size: clamp(0.82rem, 1.08vw, 1.25rem);

    line-height: 1.35;

    margin-bottom: 0.9vh;
}


.equation {
    text-align: center;

    font-size: clamp(1rem, 1.4vw, 1.5rem);

    margin: 0.7vh 0;
}


.reveal {
    animation: smoothReveal 0.45s ease-out both;
}

@keyframes smoothReveal {

    from {
        opacity: 0;
        transform: translateY(8px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}


/* ========================================================
   INVISIBLE FULL-SCREEN INTERACTION AREA
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

# ------------------------------------------------------------

# ADVANCE PRESENTATION

# ------------------------------------------------------------

if st.session_state.presentation_state < 24:

```
if st.button(
    "advance",
    key=f"advance_{st.session_state.presentation_state}",
):
    st.session_state.presentation_state += 1
    st.rerun()
```

state = st.session_state.presentation_state

# ============================================================

# STATE 0 — COMPLETELY BLANK

# ============================================================

if state == 0:

```
pass
```

# ============================================================

# STATE 1 — SLIDE 1

# ============================================================

elif state == 1:

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

elif 2 <= state <= 7:

```
slide2_content = """
    <div class="slide2">

        <div class="slide2-title">
            The Event: Soccer Match
        </div>

        <div class="event-list">
"""

if state >= 3:

    slide2_content += """
            <div class="event new-event">

                <div class="event-number">
                    (i)
                </div>

                <div class="event-text">
                    A Soccer match is about to kick off.
                </div>

            </div>
    """

if state >= 4:

    slide2_content += """
            <div class="event new-event">

                <div class="event-number">
                    (ii)
                </div>

                <div class="event-text">
                    The referee inspects and finds that the air
                    inside the football is insufficient.
                </div>

            </div>
    """

if state >= 5:

    slide2_content += """
            <div class="event new-event">

                <div class="event-number">
                    (iii)
                </div>

                <div class="event-text event-emphasis">
                    Air is then pumped into the football.
                </div>

            </div>
    """

if state >= 6:

    slide2_content += """
            <div class="event new-event">

                <div class="event-number">
                    (iv)
                </div>

                <div class="event-text">
                    After a short duration, pumping is successfully
                    completed.
                </div>

            </div>
    """

if state >= 7:

    slide2_content += """
            <div class="event new-event">

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
```

# ============================================================

# STATES 8–24 — SLIDE 3

# ============================================================

elif 8 <= state <= 24:

```
slide3_content = """
    <div class="slide3">

        <div class="slide3-title">
            Visualization of Soccer Match
        </div>

        <div class="visual-area">
"""


# --------------------------------------------------------
# STATE 9 — FOOTBALL GROUND
# --------------------------------------------------------

if state >= 9:

    slide3_content += """
            <div class="football-ground"></div>

            <div class="field-line"></div>

            <div class="field-circle"></div>
    """


# --------------------------------------------------------
# STATE 10 — FOOTBALL
# --------------------------------------------------------

if state >= 10:

    ball_class = ""

    if state == 13:
        ball_class = "pump-first"

    elif state >= 15:
        ball_class = "pump-second"

    slide3_content += f"""
            <svg
                class="football {ball_class}"
                viewBox="0 0 200 200"
                xmlns="http://www.w3.org/2000/svg"
            >

                <circle
                    cx="100"
                    cy="100"
                    r="78"
                    fill="#f5f5f5"
                    stroke="#222222"
                    stroke-width="3"
                />

                <polygon
                    points="100,67 117,79 112,101 88,101 83,79"
                    fill="#111111"
                />

                <polygon
                    points="53,68 68,55 82,70 76,88 57,84"
                    fill="#111111"
                />

                <polygon
                    points="147,68 132,55 118,70 124,88 143,84"
                    fill="#111111"
                />

                <polygon
                    points="62,130 76,113 91,123 86,143 68,148"
                    fill="#111111"
                />

                <polygon
                    points="138,130 124,113 109,123 114,143 132,148"
                    fill="#111111"
                />

                <path
                    d="M82 70 L60 38"
                    stroke="#222222"
                    stroke-width="4"
                    fill="none"
                />

                <path
                    d="M118 70 L140 38"
                    stroke="#222222"
                    stroke-width="4"
                    fill="none"
                />

            </svg>
    """


# --------------------------------------------------------
# STATE 11 — P AND O
# --------------------------------------------------------

if state >= 11:

    slide3_content += """
            <div class="origin">
                O(0,0,0)
            </div>

            <div class="point point-p">
                P(x,y,z)
            </div>
    """


# --------------------------------------------------------
# STATE 12 — OP
# --------------------------------------------------------

if state >= 12:

    slide3_content += """
            <div class="ray ray-op"></div>
    """


# --------------------------------------------------------
# STATE 13 — FIRST PUMPING
# --------------------------------------------------------

if state >= 13:

    slide3_content += """
            <div class="ray ray-opp"></div>

            <div class="point point-pp">
                P′(x′,y′,z′)
            </div>

            <div class="pumping-label pumping-pulse">
                Pumping ...
            </div>
    """


slide3_content += """
        </div>
"""


# --------------------------------------------------------
# STATE 14 — VISUALIZE AGAIN
# --------------------------------------------------------

if state == 14:

    slide3_content += """
        <div class="visualize-again">
            Visualize Again
        </div>
    """


# --------------------------------------------------------
# STATE 15 — SECOND PUMPING
# --------------------------------------------------------

if state == 15:

    slide3_content += """
        <div class="pumping-label pumping-pulse">
            Pumping ...
        </div>
    """


# --------------------------------------------------------
# STATES 16–19 — OBSERVATION
# --------------------------------------------------------

if state >= 16:

    slide3_content += """
        <div class="explanation">

            <div class="observation">

                <div class="section-heading reveal">
                    Observation
                </div>
    """

    if state >= 17:

        slide3_content += """
                <div class="explanation-point reveal">

                    • Throughout the pumping process, the point
                    <b>P</b> moves in the direction <b>OP</b>
                    and finally reaches <b>P′</b>.

                </div>
        """

    if state >= 18:

        slide3_content += """
                <div class="explanation-point reveal">

                    • The point <b>P</b> is scaled by a factor

                    <div class="equation">
                        λ = OP′ / OP
                    </div>

                </div>
        """

    if state >= 19:

        slide3_content += """
                <div class="explanation-point reveal">

                    • The point <b>P</b> is non-zero.

                </div>
        """

    slide3_content += """
            </div>
    """


# --------------------------------------------------------
# STATES 20–24 — CONCLUSION
# --------------------------------------------------------

if state >= 20:

    slide3_content += """
            <div class="conclusion">

                <div class="section-heading reveal">
                    Conclusion
                </div>
    """

    if state >= 21:

        slide3_content += """
                <div class="explanation-point reveal">

                    • The non-zero point <b>P</b> does not change
                    its direction while moving toward <b>P′</b>.

                </div>
        """

    if state >= 22:

        slide3_content += """
                <div class="explanation-point reveal">

                    Therefore, <b>P</b> is an
                    <b>eigenvector</b> corresponding to the
                    eigenvalue <b>λ</b>.

                </div>
        """

    if state >= 23:

        slide3_content += """
                <div class="explanation-point reveal">

                    • All other non-zero points on the surface of
                    the football behave in the same way.

                    They are also eigenvectors corresponding to
                    the same eigenvalue <b>λ</b>.

                </div>
        """

    if state >= 24:

        slide3_content += """
                <div class="explanation-point reveal">

                    Hence, the direction-preserving scaling of
                    the football gives us the central idea of
                    an eigenvector and its eigenvalue.

                </div>
        """

    slide3_content += """
            </div>

        </div>
    """


slide3_content += """
    </div>
"""

st.html(slide3_content)
```
