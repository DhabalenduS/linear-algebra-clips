# Clip 01 — Eigenvalues and Eigenvectors

# Slides 1–3

# One action → one visual event

# Slide 2 uses fixed positioning and cumulative reveal

# Slide 3 uses cumulative visualization and point-by-point explanation

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

# States 2–7  = Slide 2

#

# State 8  = Slide 3 heading

# State 9  = football ground

# State 10 = football

# State 11 = P(x,y,z) and O(0,0,0)

# State 12 = OP ray with front arrow

# State 13 = first pumping

# State 14 = Visualize Again

# State 15 = second pumping

#

# State 16 = Observation heading

# State 17 = Observation point 1

# State 18 = Observation point 2

# State 19 = Observation point 3

#

# State 20 = Conclusion heading

# State 21 = Conclusion point 1

# State 22 = Conclusion point 2

# State 23 = Conclusion point 3

#

# State 24 = complete Slide 3

if "presentation_state" not in st.session_state:
st.session_state.presentation_state = 0

# ------------------------------------------------------------

# PRESENTATION-STYLE CSS

# ------------------------------------------------------------

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


/* ========================================================
   COMMON SLIDE
   ======================================================== */

.slide {
    width: 100%;
    min-height: 100vh;
    box-sizing: border-box;
    background: #ffffff;
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
    text-align: center;
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
   SLIDE 3 HEADING
   -------------------------------------------------------- */

.slide3-title {
    position: absolute;

    top: 5vh;
    left: 50%;

    transform: translateX(-50%);

    width: 90vw;

    text-align: center;

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(2rem, 3.2vw, 3.8rem);

    font-weight: 600;

    line-height: 1.2;

    z-index: 50;
}


/* --------------------------------------------------------
   MAIN VISUAL AREA
   -------------------------------------------------------- */

.visual-area {
    position: absolute;

    left: 5vw;
    right: 5vw;

    top: 14vh;
    height: 47vh;

    overflow: hidden;
}


/* --------------------------------------------------------
   FOOTBALL GROUND
   -------------------------------------------------------- */

.football-ground {
    position: absolute;

    left: 0;
    right: 0;

    bottom: 0;

    height: 42%;

    background:
        linear-gradient(
            to bottom,
            #4f9f43,
            #3d8c35
        );

    border-radius: 50% 50% 0 0 / 25% 25% 0 0;

    box-shadow:
        inset 0 8px 0 rgba(255,255,255,0.10),
        inset 0 -12px 25px rgba(0,0,0,0.12);
}


/* --------------------------------------------------------
   FIELD MARKINGS
   -------------------------------------------------------- */

.field-line {
    position: absolute;

    left: 10%;
    right: 10%;

    bottom: 18%;

    height: 2px;

    background: rgba(255,255,255,0.8);
}

.field-circle {
    position: absolute;

    left: 50%;
    bottom: 3%;

    transform: translateX(-50%);

    width: 150px;
    height: 70px;

    border: 2px solid rgba(255,255,255,0.75);

    border-radius: 50%;
}


/* --------------------------------------------------------
   FOOTBALL
   -------------------------------------------------------- */

.football {
    position: absolute;

    left: 50%;
    top: 35%;

    transform: translate(-50%, -50%);

    width: 120px;
    height: 120px;

    z-index: 20;

    filter:
        drop-shadow(0 10px 8px rgba(0,0,0,0.25));
}


/* --------------------------------------------------------
   PUMPING ANIMATION
   -------------------------------------------------------- */

.pump-animation {
    animation:
        pumpBall 3s ease-in-out forwards;
}

@keyframes pumpBall {

    0% {
        transform:
            translate(-50%, -50%)
            scale(1);
    }

    45% {
        transform:
            translate(-50%, -50%)
            scale(1.10);
    }

    100% {
        transform:
            translate(-50%, -50%)
            scale(1.25);
    }
}


/* --------------------------------------------------------
   ORIGIN
   -------------------------------------------------------- */

.origin {
    position: absolute;

    left: calc(50% - 12px);
    top: calc(35% + 45px);

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(0.9rem, 1.2vw, 1.3rem);

    font-weight: 700;

    z-index: 35;
}


/* --------------------------------------------------------
   RAYS
   -------------------------------------------------------- */

.ray {
    position: absolute;

    height: 4px;

    background: #111111;

    transform-origin: left center;

    border-radius: 4px;

    z-index: 30;
}


/*
   Arrowhead is placed at the FRONT of the ray.
   This is the requested OP → presentation style.
*/

.ray::after {
    content: "";

    position: absolute;

    right: -1px;
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
    top: 35%;

    width: 160px;
}


.ray-opp {
    left: 50%;
    top: 35%;

    width: 285px;
}


/* --------------------------------------------------------
   POINT LABELS
   -------------------------------------------------------- */

.point {
    position: absolute;

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(0.95rem, 1.25vw, 1.35rem);

    font-weight: 600;

    white-space: nowrap;

    z-index: 40;
}


.point-p {
    left: calc(50% + 160px);
    top: calc(35% - 38px);
}


.point-pp {
    left: calc(50% + 285px);
    top: calc(35% - 38px);
}


/* --------------------------------------------------------
   PUMPING TEXT
   -------------------------------------------------------- */

.pumping {
    position: absolute;

    left: 50%;

    bottom: 1%;

    transform: translateX(-50%);

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(1.15rem, 1.7vw, 1.8rem);

    font-weight: 600;

    letter-spacing: 0.03em;

    z-index: 45;
}

.pumping-pulse {
    animation: pumpingPulse 0.75s ease-in-out infinite alternate;
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

    padding: 1.2vh 2.4vw;

    background: rgba(255,255,255,0.95);

    border-radius: 12px;

    box-shadow:
        0 5px 20px rgba(0,0,0,0.15);

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(1.4rem, 2.4vw, 2.6rem);

    font-weight: 600;

    letter-spacing: 0.03em;

    z-index: 100;
}


/* ========================================================
   EXPLANATION AREA
   ======================================================== */

.explanation {
    position: absolute;

    left: 6vw;
    right: 6vw;

    top: 64vh;
    bottom: 4vh;

    display: flex;

    gap: 5vw;

    align-items: flex-start;
}


.observation,
.conclusion {
    flex: 1;

    font-family: Georgia, "Times New Roman", serif;

    text-align: left;
}


.section-heading {
    font-size: clamp(1.3rem, 1.8vw, 1.9rem);

    font-weight: 700;

    margin-bottom: 1.2vh;
}


.explanation-point {
    font-size: clamp(0.85rem, 1.15vw, 1.3rem);

    line-height: 1.38;

    margin-bottom: 1.0vh;
}


.equation {
    text-align: center;

    font-size: clamp(1.1rem, 1.5vw, 1.6rem);

    margin: 1vh 0;
}


/* --------------------------------------------------------
   SMOOTH REVEAL
   -------------------------------------------------------- */

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
   INVISIBLE FULL-SCREEN CLICK / TOUCH AREA
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

# ADVANCE ONE VISUAL EVENT

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

# STATE 0 — BLANK

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
# STATE 9 — GROUND
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

    if state == 13 or state == 15:
        ball_class = "pump-animation"

    slide3_content += f"""
            <svg
                class="football {ball_class}"
                viewBox="0 0 200 200"
                xmlns="http://www.w3.org/2000/svg"
            >

                <defs>

                    <radialGradient
                        id="ballGradient"
                        cx="35%"
                        cy="30%"
                        r="70%"
                    >

                        <stop
                            offset="0%"
                            stop-color="#ffffff"
                        />

                        <stop
                            offset="75%"
                            stop-color="#eeeeee"
                        />

                        <stop
                            offset="100%"
                            stop-color="#cccccc"
                        />

                    </radialGradient>

                </defs>


                <circle
                    cx="100"
                    cy="100"
                    r="78"
                    fill="url(#ballGradient)"
                    stroke="#222222"
                    stroke-width="3"
                />


                <polygon
                    points="100,68 117,80 111,101 89,101 83,80"
                    fill="#111111"
                />


                <polygon
                    points="53,67 68,55 82,70 76,88 57,84"
                    fill="#111111"
                />


                <polygon
                    points="147,67 132,55 118,70 124,88 143,84"
                    fill="#111111"
                />


                <polygon
                    points="61,128 76,112 91,123 86,143 68,147"
                    fill="#111111"
                />


                <polygon
                    points="139,128 124,112 109,123 114,143 132,147"
                    fill="#111111"
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

            <div class="pumping pumping-pulse">
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
        <div class="pumping pumping-pulse">
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


    slide3_content += """
            </div>

        </div>
    """


# --------------------------------------------------------
# CLOSE SLIDE 3
# --------------------------------------------------------

slide3_content += """
    </div>
"""


st.html(slide3_content)
```
