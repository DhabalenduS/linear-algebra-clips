#1st commit for the clip_01_eigenvalues dated 31th August at 2:20 pm  
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

    /* Remove Streamlit's default presentation clutter */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    [data-testid="stToolbar"] {
        visibility: hidden;
    }

    [data-testid="stDecoration"] {
        visibility: hidden;
    }

    /* Remove default page padding */
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: 100%;
    }

    /* Main presentation canvas */
    .slide {
        width: 100%;
        min-height: 100vh;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        text-align: center;

        box-sizing: border-box;
        padding: 6vh 8vw;

        background: white;
    }

    /* Main title */
    .slide-title {
        font-family: "Georgia", "Times New Roman", serif;
        font-size: clamp(2.2rem, 4vw, 4.5rem);
        font-weight: 600;
        line-height: 1.2;

        letter-spacing: 0.01em;

        margin-bottom: 7vh;
    }

    /* Byline */
    .by {
        font-family: "Georgia", "Times New Roman", serif;
        font-size: clamp(1.4rem, 2vw, 2.2rem);

        margin-bottom: 1.5vh;
    }

    /* Presenter name */
    .author {
        font-family: "Georgia", "Times New Roman", serif;
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
st.markdown(
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
    """,
    unsafe_allow_html=True,
)
