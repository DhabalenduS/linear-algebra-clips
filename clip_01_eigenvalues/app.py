# Clip 01 — Eigenvalues and Eigenvectors

# Slides 1–3

# One action → one visual event

#

# Slide 3:

# 1  = Visualization of Soccer Match

# 2  = Football ground

# 3  = Football

# 4  = P(x,y,z) + O(0,0,0)

# 5  = OP ray with front arrow

# 6  = First pumping: P -> P'

# 7  = Visualize Again

# 8  = Second pumping

# 9  = Observation heading

# 10 = Observation point 1

# 11 = Observation point 2

# 12 = Observation point 3

# 13 = Conclusion heading

# 14 = Conclusion point 1

# 15 = Conclusion point 2

# 16 = Conclusion point 3

import streamlit as st
import os
import base64

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

# OPTIONAL PRESENTER PHOTO

# ------------------------------------------------------------

def get_photo_data():

```
photo_path = os.path.join(
    os.path.dirname(__file__),
    "author_photo.png"
)

if os.path.exists(photo_path):

    with open(photo_path, "rb") as photo_file:
        encoded = base64.b64encode(
            photo_file.read()
        ).decode()

    return f"data:image/png;base64,{encoded}"

return ""
```

photo_data = get_photo_data()

# ------------------------------------------------------------

# PRESENTATION-STYLE CSS

# ------------------------------------------------------------

st.markdown(
""" <style>

```
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
   SLIDE 3
   -------------------------------------------------------- */

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

    top: 6vh;
    left: 50%;

    transform: translateX(-50%);

    width: 90vw;

    text-align: center;

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(2rem, 3.2vw, 3.8rem);

    font-weight: 600;

    line-height: 1.2;

    z-index: 20;
}


/* --------------------------------------------------------
   MAIN FOOTBALL VISUAL AREA
   -------------------------------------------------------- */

.football-stage {

    position: absolute;

    left: 4vw;
    right: 4vw;

    top: 15vh;

    height: 49vh;

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


/* Football pitch markings */

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

    z-index: 8;

    filter:
        drop-shadow(0 12px 10px rgba(0,0,0,0.28));
}


.football.inflate {

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
            scale(1.13);
    }

    100% {
        transform:
            translate(-50%, -50%)
            scale(1.28);
    }
}


/* --------------------------------------------------------
   RAY SYSTEM
   -------------------------------------------------------- */

.ray {

    position: absolute;

    height: 4px;

    background: #111111;

    transform-origin: left center;

    z-index: 12;

    border-radius: 3px;
}


.ray::after {

    content: "";

    position: absolute;

    right: -1px;
    top: 50%;

    transform:
        translateY(-50%)
        rotate(0deg);

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

    opacity: 0;
}


.show-opp {

    animation:
        showOpp 0.7s ease-out forwards;
}


@keyframes showOpp {

    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}


/* --------------------------------------------------------
   POINT O
   -------------------------------------------------------- */

.origin-label {

    position: absolute;

    left: calc(50% - 18px);
    top: calc(36% + 12px);

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(1.1rem, 1.5vw, 1.7rem);

    font-weight: 700;

    z-index: 16;
}


/* --------------------------------------------------------
   P AND P' LABELS
   -------------------------------------------------------- */

.point-label {

    position: absolute;

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(1rem, 1.35vw, 1.5rem);

    font-weight: 600;

    white-space: nowrap;

    z-index: 18;
}


.point-p {

    left: calc(50% + 165px);

    top: calc(36% - 46px);
}


.point-pp {

    left: calc(50% + 285px);

    top: calc(36% - 46px);

    opacity: 0;
}


.show-pp {

    animation:
        showOpp 0.7s ease-out forwards;
}


/* --------------------------------------------------------
   PUMPING LABEL
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

    z-index: 20;
}


.pumping-active {

    animation:
        pumpingPulse 0.8s ease-in-out infinite alternate;
}


@keyframes pumpingPulse {

    from {
        opacity: 0.65;
        transform: translateX(-50%) scale(1);
    }

    to {
        opacity: 1;
        transform: translateX(-50%) scale(1.04);
    }
}


/* --------------------------------------------------------
   LOWER EXPLANATION AREA
   -------------------------------------------------------- */

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

    font-size: clamp(0.95rem, 1.35vw, 1.45rem);

    line-height: 1.38;

    margin-bottom: 1.1vh;
}


.math-emphasis {

    font-weight: 700;
}


.equation {

    font-size: clamp(1.2rem, 1.7vw, 1.8rem);

    text-align: center;

    margin: 1.2vh 0;
}


/* --------------------------------------------------------
   PRESENTER PHOTO
   -------------------------------------------------------- */

.presenter {

    position: absolute;

    right: 2.5vw;

    bottom: 2vh;

    width: clamp(70px, 7vw, 105px);

    text-align: center;

    z-index: 30;
}


.presenter img {

    width: clamp(55px, 5.5vw, 82px);

    height: clamp(55px, 5.5vw, 82px);

    object-fit: cover;

    border-radius: 50%;

    border: 2px solid #ffffff;

    box-shadow:
        0 4px 14px rgba(0,0,0,0.20);
}


.presenter-placeholder {

    width: clamp(55px, 5.5vw, 82px);

    height: clamp(55px, 5.5vw, 82px);

    margin: auto;

    border-radius: 50%;

    background: #eeeeee;

    border: 2px solid #cccccc;

    display: flex;

    align-items: center;

    justify-content: center;

    font-family: Georgia, "Times New Roman", serif;

    font-size: 1.2rem;

    font-weight: 700;
}


.presenter-name {

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(0.55rem, 0.75vw, 0.8rem);

    margin-top: 0.5vh;

    white-space: nowrap;
}


/* --------------------------------------------------------
   VISUALIZE AGAIN
   -------------------------------------------------------- */

.visualize-again {

    position: absolute;

    left: 50%;
    top: 50%;

    transform: translate(-50%, -50%);

    z-index: 50;

    font-family: Georgia, "Times New Roman", serif;

    font-size: clamp(1.5rem, 2.5vw, 2.8rem);

    font-weight: 600;

    letter-spacing: 0.04em;

    padding: 1.2vh 2.5vw;

    background: rgba(255,255,255,0.92);

    border-radius: 12px;

    box-shadow:
        0 5px 20px rgba(0,0,0,0.12);

    animation:
        visualizeAppear 0.6s ease-out both;
}


@keyframes visualizeAppear {

    from {
        opacity: 0;
        transform:
            translate(-50%, -50%)
            scale(0.95);
    }

    to {
        opacity: 1;
        transform:
            translate(-50%, -50%)
            scale(1);
    }
}


/* --------------------------------------------------------
   FULL-SCREEN INVISIBLE ADVANCE BUTTON
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
```

)

# ------------------------------------------------------------

# ADVANCE PRESENTATION

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

# ------------------------------------------------------------

# CURRENT STATE

# ------------------------------------------------------------

state = st.session_state.presentation_state

# ------------------------------------------------------------

# STATE 0 — COMPLETELY BLANK

# ------------------------------------------------------------

if state == 0:

```
pass
```

# ------------------------------------------------------------

# STATE 1 — SLIDE 1

# ------------------------------------------------------------

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

# ------------------------------------------------------------

# STATES 2–7 — SLIDE 2

# ------------------------------------------------------------

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

    reveal_class = "new-event" if state == 3 else ""

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


if state >= 4:

    reveal_class = "new-event" if state == 4 else ""

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


if state >= 5:

    reveal_class = "new-event" if state == 5 else ""

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


if state >= 6:

    reveal_class = "new-event" if state == 6 else ""

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


if state >= 7:

    reveal_class = "new-event" if state == 7 else ""

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
```

# ------------------------------------------------------------

# STATES 8–16 — SLIDE 3

# ------------------------------------------------------------

elif 8 <= state <= 16:

```
# --------------------------------------------------------
# DETERMINE VISUAL CONDITIONS
# --------------------------------------------------------

first_pumping = state == 8

visualize_again = state == 9

second_pumping = state == 10

show_observation = state >= 11

show_observation_1 = state >= 12
show_observation_2 = state >= 13
show_observation_3 = state >= 14

show_conclusion = state >= 15

show_conclusion_1 = state >= 16


# --------------------------------------------------------
# SLIDE 3 HTML
# --------------------------------------------------------

slide3_html = f"""
    <div class="slide3">

        <!-- TITLE -->

        <div class="slide3-title">
            Visualization of Soccer Match
        </div>


        <!-- MAIN FOOTBALL STAGE -->

        <div class="football-stage">


            <!-- GREEN GROUND -->

            <div class="football-ground"></div>

            <div class="field-line"></div>

            <div class="field-circle"></div>


            <!-- FOOTBALL -->

            <svg
                class="football {'inflate' if first_pumping or second_pumping else ''}"
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


                <!-- Central black pentagon -->

                <polygon
                    points="100,68 117,80 111,101 89,101 83,80"
                    fill="#111111"
                />


                <!-- Surrounding black panels -->

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

                <!-- Connecting seams -->

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


            <!-- ORIGIN -->

            <div class="origin-label">
                O(0,0,0)
            </div>
"""


# --------------------------------------------------------
# POINT P
# --------------------------------------------------------

if state >= 5:

    slide3_html += """
            <div class="point-label point-p">
                P(x,y,z)
            </div>
    """


# --------------------------------------------------------
# OP RAY
# --------------------------------------------------------

if state >= 6:

    slide3_html += """
            <div class="ray ray-op"></div>
    """


# --------------------------------------------------------
# PUMPING / OP'
# --------------------------------------------------------

if state >= 8:

    slide3_html += """
            <div class="ray ray-opp show-opp"></div>

            <div class="point-label point-pp show-pp">
                P′(x′,y′,z′)
            </div>
    """


# --------------------------------------------------------
# PUMPING LABEL
# --------------------------------------------------------

if first_pumping or second_pumping:

    slide3_html += """
            <div class="pumping-label pumping-active">
                Pumping ...
            </div>
    """

elif state >= 8:

    slide3_html += """
            <div class="pumping-label">
                Pumping completed
            </div>
    """


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
# EXPLANATION AREA
# --------------------------------------------------------

if show_observation or show_conclusion:

    slide3_html += """
        <div class="explanation-area">
    """


    # ----------------------------------------------------
    # OBSERVATION
    # ----------------------------------------------------

    if show_observation:

        slide3_html += """
            <div class="observation-box">

                <div class="section-heading">
                    Observation
                </div>
        """


    if show_observation_1:

        slide3_html += """
                <div class="math-point new-event">

                    • Throughout the pumping process,
                    <b>P</b> moves in the direction <b>OP</b>
                    and finally reaches <b>P′</b>.

                </div>
        """


    if show_observation_2:

        slide3_html += """
                <div class="math-point new-event">

                    • The position vector is scaled by a factor

                    <div class="equation">
                        λ = OP′ / OP
                    </div>

                </div>
        """


    if show_observation_3:

        slide3_html += """
                <div class="math-point new-event">

                    • The point <b>P</b> is non-zero.

                </div>
        """


    if show_observation:

        slide3_html += """
            </div>
        """


    # ----------------------------------------------------
    # CONCLUSION
    # ----------------------------------------------------

    if show_conclusion:

        slide3_html += """
            <div class="conclusion-box">

                <div class="section-heading">
                    Conclusion
                </div>
        """


    if show_conclusion_1:

        slide3_html += """
                <div class="math-point new-event">

                    • The non-zero point <b>P</b> does not
                    change its direction while moving toward
                    <b>P′</b>.

                </div>

                <div class="math-point new-event">

                    Therefore, <b>P</b> is an
                    <b>eigenvector</b> corresponding to the
                    eigenvalue <b>λ</b>.

                </div>

                <div class="math-point new-event">

                    • All other non-zero points on the surface
                    of the football behave in the same way.

                    They are also eigenvectors corresponding
                    to the same eigenvalue <b>λ</b>.

                </div>
        """


    if show_conclusion:

        slide3_html += """
            </div>
        """


    slide3_html += """
        </div>
    """


# --------------------------------------------------------
# PRESENTER PHOTO
# --------------------------------------------------------

if photo_data:

    slide3_html += f"""
        <div class="presenter">

            <img src="{photo_data}">

            <div class="presenter-name">
                Dr. Dhabalendu Samanta
            </div>

        </div>
    """

else:

    slide3_html += """
        <div class="presenter">

            <div class="presenter-placeholder">
                DS
            </div>

            <div class="presenter-name">
                Dr. Dhabalendu Samanta
            </div>

        </div>
    """


slide3_html += """
    </div>
"""


st.html(slide3_html)
```
