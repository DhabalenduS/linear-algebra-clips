### `app.py`

```python
# Clip 01 — Eigenvalues and Eigenvectors
# First commit — 31 August 2026, 2:20 PM

import streamlit as st


# ------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------

st.set_page_config(
    page_title="The Essence of Eigenvalues and Eigenvectors",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ------------------------------------------------------------
# PRESENTATION-STYLE CSS
# ------------------------------------------------------------

st.markdown(
    """
    <style>

    /* Remove Streamlit interface elements */
    #MainMenu,
    footer,
    header,
    [data-testid="stToolbar"],
    [data-testid="stDecoration"] {
        visibility: hidden;
    }

    /* Remove default page spacing */
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }

    /* Main presentation canvas */
    .slide {
        width: 100%;
        min-height: 100vh;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        box-sizing: border-box;
        padding: 6vh 8vw;

        background: #ffffff;

        text-align: center;
    }

    /* Main title */
    .slide-title {
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(2.2rem, 4vw, 4.5rem);
        font-weight: 600;
        line-height: 1.2;

        letter-spacing: 0.01em;

        margin-bottom: 7vh;
    }

    /* Byline */
    .by {
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(1.4rem, 2vw, 2.2rem);

        margin-bottom: 1.5vh;
    }

    /* Presenter name */
    .author {
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(1.7rem, 2.5vw, 2.8rem);
        font-weight: 600;

        letter-spacing: 0.02em;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------------------------
# SLIDE 1
# ------------------------------------------------------------

st.html(
    """
    <div class="slide">

        <div class="slide-title">
            The Essence of Eigenvalues and Eigenvectors
        </div>

        <div class="by">
            By
        </div>

        <div class="author">
            Dr. Dhabalendu Samanta
        </div>

    </div>
    """
)
```

### `requirements.txt`

```text
streamlit==1.48.0
```
