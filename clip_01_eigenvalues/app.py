# Clip 01 — Eigenvalues and Eigenvectors

# Slides 1–3

# One action → one visual event

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

# PRESENTATION CSS

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

</style>
""",
unsafe_allow_html=True,
```

)


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
    text-align: center;
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
   SLIDE 3
   ======================================================== */

.slide3 {
    width: 100%;
    min-height: 100vh;
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
    width: 90vw;

    text-align: center;

    font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(2rem, 3.2vw, 3.8rem);
    font-weight: 600;
    line-height: 1.2;

    z-index: 30;
}


/* --------------------------------------------------------
   MAIN VISUAL STAGE
   -------------------------------------------------------- */

.football-stage {
    position: absolute;

    left: 5vw;
    right: 5vw;

    top: 14vh;
    height: 50vh;

    overflow: hidden;

    border-radius: 18px;
}


/* --------------------------------------------------------
   GREEN FOOTBALL GROUND
   -------------------------------------------------------- */

.football-ground {
    position: absolute;

    left: 0;
    right: 0;
    bottom: 0;

    height: 48%;

    background:
        linear-gradient(
            to bottom,
            #4e9f42 0%,
            #3d8d35 100%
        );

    border-radius: 50% 50% 0 0 / 20% 20% 0 0;

    box-shadow:
        inset 0 8px 0 rgba(255,255,255,0.10),
        inset 0 -12px 25px rgba(0,0,0,0.12);
}


.field-line {
    position: absolute;

    left: 12%;
    right: 12%;

    bottom: 22%;

    height: 2px;

    background: rgba(255,255,255,0.78);
}


.field-circle {
    position: absolute;

    left: 50%;
    bottom: 7%;

    transform: translateX(-50%);

    width: 150px;
    height: 75px;

    border: 2px solid rgba(255,255,255,0.75);

    border-radius: 50%;
}


/* --------------------------------------------------------
   FOOTBALL
   -------------------------------------------------------- */

.football {
    position: absolute;

    left: 50%;
    top: 36%;

    transform: translate(-50%, -50%);

    width: 130px;
    height: 130px;

    z-index: 10;

    filter:
        drop-shadow(0 12px 10px rgba(0,0,0,0.28));
}


/* --------------------------------------------------------
   FOOTBALL PUMPING ANIMATION
   -------------------------------------------------------- */

.football-pump {
    animation:
        footballInflate 3.2s ease-in-out forwards;
}


@keyframes footballInflate {

    0% {
        transform:
            translate(-50%, -50%)
            scale(1);
    }

    45% {
        transform:
            translate(-50%, -50%)
            scale(1.12);
    }

    100% {
        transform:
            translate(-50%, -50%)
            scale(1.27);
    }
}


/* --------------------------------------------------------
   ORIGIN
   -------------------------------------------------------- */

.origin-label {
    position: absolute;

    left: calc(50% - 18px);
    top: calc(36% + 12px);

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(1rem, 1.35vw, 1.5rem);

    font-weight: 700;

    z-index: 20;
}


/* --------------------------------------------------------
   RAYS
   -------------------------------------------------------- */

.ray {
    position: absolute;

    height: 4px;

    background: #111111;

    transform-origin: left center;

    z-index: 18;

    border-radius: 4px;
}


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
    border-left: 17px solid #111111;
}


.ray-op {
    left: 50%;
    top: 36%;
    width: 165px;
}


.ray-opp {
    left: 50%;
    top: 36%;
    width: 285px;
}


/* --------------------------------------------------------
   POINT LABELS
   -------------------------------------------------------- */

.point-label {
    position: absolute;

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(0.95rem, 1.3vw, 1.45rem);

    font-weight: 600;

    white-space: nowrap;

    z-index: 25;
}


.point-p {
    left: calc(50% + 165px);
    top: calc(36% - 42px);
}


.point-pp {
    left: calc(50% + 285px);
    top: calc(36% - 42px);
}


/* --------------------------------------------------------
   PUMPING MESSAGE
   -------------------------------------------------------- */

.pumping-label {
    position: absolute;

    left: 50%;
    bottom: 3%;

    transform: translateX(-50%);

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(1.2rem, 1.8vw, 2rem);

    font-weight: 600;

    letter-spacing: 0.03em;

    z-index: 25;
}


.pumping-active {
    animation:
        pumpingPulse 0.8s ease-in-out infinite alternate;
}


@keyframes pumpingPulse {

    from {
        opacity: 0.65;
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
    top: 39%;

    transform: translate(-50%, -50%);

    z-index: 60;

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(1.5rem, 2.5vw, 2.8rem);

    font-weight: 600;

    letter-spacing: 0.04em;

    padding: 1.2vh 2.5vw;

    background: rgba(255,255,255,0.94);

    border-radius: 12px;

    box-shadow:
        0 5px 20px rgba(0,0,0,0.12);
}


/* ========================================================
   LOWER EXPLANATION AREA
   ======================================================== */

.explanation-area {
    position: absolute;

    left: 6vw;
    right: 6vw;

    top: 66vh;
    bottom: 4vh;

    display: flex;

    gap: 5vw;

    align-items: flex-start;
}


.observation-box,
.conclusion-box {
    flex: 1;

    font-family: Georgia, "Times New Roman", serif;

    text-align: left;
}


.section-heading {
    font-size: clamp(1.35rem, 1.9vw, 2rem);

    font-weight: 700;

    margin-bottom: 1.5vh;
}


.math-point {
    font-size: clamp(0.9rem, 1.25vw, 1.4rem);

    line-height: 1.38;

    margin-bottom: 1.1vh;
}


.equation {
    font-size: clamp(1.2rem, 1.7vw, 1.8rem);

    text-align: center;

    margin: 1.2vh 0;
}


/* --------------------------------------------------------
   PRESENTER
   -------------------------------------------------------- */

.presenter {
    position: absolute;

    right: 2vw;
    bottom: 1.5vh;

    width: 75px;

    text-align: center;

    z-index: 40;
}


.presenter-circle {
    width: 58px;
    height: 58px;

    margin: auto;

    border-radius: 50%;

    background: #eeeeee;

    border: 2px solid #cccccc;

    display: flex;

    align-items: center;
    justify-content: center;

    font-family: Georgia, "Times New Roman", serif;

    font-size: 1rem;

    font-weight: 700;
}


.presenter-name {
    font-family: Georgia, "Times New Roman", serif;

    font-size: 0.55rem;

    margin-top: 0.5vh;

    white-space: nowrap;
}


/* --------------------------------------------------------
   CUMULATIVE REVEAL
   -------------------------------------------------------- */

.reveal {
    animation: revealItem 0.45s ease-out both;
}


@keyframes revealItem {

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
   FULL-SCREEN INVISIBLE CLICK / TOUCH AREA
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

# ADVANCE ONE STATE PER CLICK / TOUCH

# ------------------------------------------------------------

if st.session_state.presentation_state < 16:

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
            <div class="event reveal">

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
            <div class="event reveal">

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
            <div class="event reveal">

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
            <div class="event reveal">

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
            <div class="event reveal">

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

# STATES 8–16 — SLIDE 3

# ============================================================

elif 8 <= state <= 16:

```
# --------------------------------------------------------
# SLIDE 3 STATE CONDITIONS
# --------------------------------------------------------

first_pumping = state == 13
visualize_again = state == 14
second_pumping = state == 15

show_observation = state >= 16


# --------------------------------------------------------
# SLIDE 3
# --------------------------------------------------------

slide3_html = """
    <div class="slide3">

        <div class="slide3-title">
            Visualization of Soccer Match
        </div>

        <div class="football-stage">
"""


# --------------------------------------------------------
# STATE 8 — TITLE ONLY
# --------------------------------------------------------

if state >= 8:

    pass


# --------------------------------------------------------
# STATE 9 — GREEN GROUND
# --------------------------------------------------------

if state >= 9:

    slide3_html += """
            <div class="football-ground"></div>

            <div class="field-line"></div>

            <div class="field-circle"></div>
    """


# --------------------------------------------------------
# STATE 10 — FOOTBALL
# --------------------------------------------------------

if state >= 10:

    slide3_html += """
            <svg
                class="football"
                viewBox="0 0 200 200"
                xmlns="http://www.w3.org/2000/svg"
            >

                <defs>

                    <radialGradient
                        id="ballShade"
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
                            stop-color="#cfcfcf"
                        />

                    </radialGradient>

                </defs>


                <circle
                    cx="100"
                    cy="100"
                    r="78"
                    fill="url(#ballShade)"
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


                <path
                    d="M82 70 L68 55"
                    stroke="#222222"
                    stroke-width="3"
                    fill="none"
                />

                <path
                    d="M118 70 L132 55"
                    stroke="#222222"
                    stroke-width="3"
                    fill="none"
                />

                <path
                    d="M89 101 L76 112"
                    stroke="#222222"
                    stroke-width="3"
                    fill="none"
                />

                <path
                    d="M111 101 L124 112"
                    stroke="#222222"
                    stroke-width="3"
                    fill="none"
                />

            </svg>
    """


# --------------------------------------------------------
# STATE 11 — O AND P
# --------------------------------------------------------

if state >= 11:

    slide3_html += """
            <div class="origin-label">
                O(0,0,0)
            </div>

            <div class="point-label point-p">
                P(x,y,z)
            </div>
    """


# --------------------------------------------------------
# STATE 12 — OP RAY
# --------------------------------------------------------

if state >= 12:

    slide3_html += """
            <div class="ray ray-op"></div>
    """


# --------------------------------------------------------
# STATE 13 — FIRST PUMPING
# --------------------------------------------------------

if state >= 13:

    slide3_html += """
            <div class="ray ray-opp"></div>

            <div class="point-label point-pp">
                P′(x′,y′,z′)
            </div>

            <div class="pumping-label pumping-active">
                Pumping ...
            </div>
    """


# --------------------------------------------------------
# CLOSE MAIN STAGE
# --------------------------------------------------------

slide3_html += """
        </div>
"""


# --------------------------------------------------------
# VISUALIZE AGAIN
# --------------------------------------------------------

if visualize_again:

    slide3_html += """
        <div class="visualize-again">
            Visualize Again
        </div>
    """


# --------------------------------------------------------
# SECOND PUMPING MESSAGE
# --------------------------------------------------------

if second_pumping:

    slide3_html += """
        <div class="pumping-label pumping-active">
            Pumping ...
        </div>
    """


# --------------------------------------------------------
# OBSERVATION / CONCLUSION
# --------------------------------------------------------

if show_observation:

    slide3_html += """
        <div class="explanation-area">

            <div class="observation-box">

                <div class="section-heading reveal">
                    Observation
                </div>

                <div class="math-point reveal">
                    • Throughout the pumping process,
                    <b>P</b> moves in the direction <b>OP</b>
                    and finally reaches <b>P′</b>.
                </div>

                <div class="math-point reveal">

                    • The point <b>P</b> is scaled by a factor

                    <div class="equation">
                        λ = OP′ / OP
                    </div>

                </div>

                <div class="math-point reveal">

                    • The point <b>P</b> is non-zero.

                </div>

            </div>


            <div class="conclusion-box">

                <div class="section-heading reveal">
                    Conclusion
                </div>

                <div class="math-point reveal">

                    • The non-zero point <b>P</b> does not
                    change its direction while moving toward
                    <b>P′</b>.

                </div>

                <div class="math-point reveal">

                    Therefore, <b>P</b> is an
                    <b>eigenvector</b> corresponding to the
                    eigenvalue <b>λ</b>.

                </div>

                <div class="math-point reveal">

                    • All other non-zero points on the surface
                    of the football behave in the same way.

                    They are also eigenvectors corresponding
                    to the same eigenvalue <b>λ</b>.

                </div>

            </div>

        </div>
    """


# --------------------------------------------------------
# PRESENTER PLACEHOLDER
# --------------------------------------------------------

slide3_html += """
        <div class="presenter">

            <div class="presenter-circle">
                DS
            </div>

            <div class="presenter-name">
                Dr. Dhabalendu Samanta
            </div>

        </div>


    </div>
"""


st.html(slide3_html)
```
