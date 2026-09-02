# Clip 01 — Eigenvalues and Eigenvectors
# Slides 1–3 (True WebGL 3D Visualization via Components)
#  7th Commit for slide 3 for click 4 and 5
import streamlit as st
import streamlit.components.v1 as components

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

.slide3-left-panel {
    position: absolute;
    left: 4vw;
    top: 19vh;
    width: 33vw;
    height: 68vh;
    z-index: 30;
    font-family: Georgia, "Times New Roman", serif;
}

.webgl-container {
    position: absolute;
    left: 40vw;
    top: 19vh;
    width: 55vw;
    height: 68vh;
    z-index: 10;
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
        content += """
            <div class="event">
                <div class="event-number">(i)</div>
                <div class="event-text">
                    A Soccer match is about to kick off.
                </div>
            </div>
        """

    if state >= 4:
        content += """
            <div class="event">
                <div class="event-number">(ii)</div>
                <div class="event-text">
                    The referee inspects and finds that the air
                    inside the football is insufficient.
                </div>
            </div>
        """

    if state >= 5:
        content += """
            <div class="event">
                <div class="event-number">(iii)</div>
                <div class="event-text event-emphasis">
                    Air is then pumped into the football.
                </div>
            </div>
        """

    if state >= 6:
        content += """
            <div class="event">
                <div class="event-number">(iv)</div>
                <div class="event-text">
                    After a short duration, pumping is successfully
                    completed.
                </div>
            </div>
        """

    if state >= 7:
        content += """
            <div class="event">
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
# STATES 8–12 — SLIDE 3 (TRUE WEBGL 3D COMPONENT)
# ============================================================

elif 8 <= st.session_state.presentation_state <= 12:

    state = st.session_state.presentation_state

    # Render Title and Left Panel
    st.html(
        """
        <div class="slide3">
            <div class="slide3-title">
                Visualization of Soccer Match
            </div>
            <div class="slide3-left-panel"></div>
        </div>
        """
    )

    # 3D WebGL Three.js Component for Right Panel
    three_js_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <style>
            html, body {{
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100%;
                overflow: hidden;
                background: transparent;
                pointer-events: none;
            }}
            #stage {{
                width: 100%;
                height: 100%;
                position: relative;
                border: 5px solid #ffffff;
                border-radius: 16px;
                box-sizing: border-box;
                overflow: hidden;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            }}
            canvas {{
                width: 100%;
                height: 100%;
                display: block;
            }}
            .math-badge {{
                position: absolute;
                background: #ffffff;
                border: 2.5px solid #1d4ed8;
                color: #1d4ed8;
                padding: 4px 10px;
                border-radius: 6px;
                font-family: Georgia, serif;
                font-size: 16px;
                font-weight: bold;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3);
                white-space: nowrap;
                transform: translate(-50%, -50%);
                display: none;
            }}
            .vector-badge {{
                position: absolute;
                background: #1d4ed8;
                color: #ffffff;
                padding: 3px 8px;
                border-radius: 4px;
                font-family: Georgia, serif;
                font-size: 15px;
                font-weight: bold;
                box-shadow: 0 4px 10px rgba(0,0,0,0.35);
                transform: translate(-50%, -50%);
                display: none;
            }}
        </style>
    </head>
    <body>
        <div id="stage">
            <canvas id="canvas3d"></canvas>
            <div id="badge-o" class="math-badge">O(0, 0, 0)</div>
            <div id="badge-p" class="math-badge">P(x, y, z)</div>
            <div id="badge-op" class="vector-badge">OP&#8407;</div>
        </div>

        <script>
            const currentState = {state};
            const stage = document.getElementById('stage');
            const canvas = document.getElementById('canvas3d');

            const width = stage.clientWidth;
            const height = stage.clientHeight;

            // 1. Scene & Camera Setup
            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0x388e3c);

            const camera = new THREE.PerspectiveCamera(40, width / height, 0.1, 1000);
            camera.position.set(0, 16, 26);
            camera.lookAt(0, 0, 0);

            const renderer = new THREE.WebGLRenderer({{ canvas: canvas, antialias: true }});
            renderer.setSize(width, height);
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
            renderer.shadowMap.enabled = true;
            renderer.shadowMap.type = THREE.PCFSoftShadowMap;

            // 2. Lighting
            const ambient = new THREE.AmbientLight(0xffffff, 0.75);
            scene.add(ambient);

            const sun = new THREE.DirectionalLight(0xffffff, 1.1);
            sun.position.set(15, 25, 15);
            sun.castShadow = true;
            scene.add(sun);

            // CLICK 2 (State >= 9): Green Pitch Ground with Markings
            if (currentState >= 9) {{
                const pitchGeo = new THREE.PlaneGeometry(38, 24);
                const pitchMat = new THREE.MeshStandardMaterial({{ color: 0x43a047, roughness: 0.85 }});
                const pitch = new THREE.Mesh(pitchGeo, pitchMat);
                pitch.rotation.x = -Math.PI / 2;
                pitch.receiveShadow = true;
                scene.add(pitch);

                const lineMat = new THREE.MeshBasicMaterial({{ color: 0xffffff }});
                
                // Border lines
                const borderGeo = new THREE.EdgesGeometry(pitchGeo);
                const borderLines = new THREE.LineSegments(borderGeo, lineMat);
                borderLines.rotation.x = -Math.PI / 2;
                borderLines.position.y = 0.02;
                scene.add(borderLines);

                // Half line
                const halfGeo = new THREE.PlaneGeometry(0.14, 24);
                const halfLine = new THREE.Mesh(halfGeo, lineMat);
                halfLine.rotation.x = -Math.PI / 2;
                halfLine.position.y = 0.02;
                scene.add(halfLine);

                // Center Circle
                const circleGeo = new THREE.RingGeometry(3.8, 3.96, 64);
                const centerCircle = new THREE.Mesh(circleGeo, lineMat);
                centerCircle.rotation.x = -Math.PI / 2;
                centerCircle.position.y = 0.02;
                scene.add(centerCircle);
            }}

            // CLICK 3 (State >= 10): 3D Volumetric Soccer Ball
            let ball = null;
            const ballRadius = 3.0;

            if (currentState >= 10) {{
                const texCanvas = document.createElement('canvas');
                texCanvas.width = 1024;
                texCanvas.height = 512;
                const ctx = texCanvas.getContext('2d');

                ctx.fillStyle = '#f8fafc';
                ctx.fillRect(0, 0, 1024, 512);

                ctx.fillStyle = '#181818';
                function drawPentagon(cx, cy, r) {{
                    ctx.beginPath();
                    for (let i = 0; i < 5; i++) {{
                        const a = (i * 2 * Math.PI / 5) - Math.PI / 2;
                        const x = cx + r * Math.cos(a);
                        const y = cy + r * Math.sin(a);
                        if (i === 0) ctx.moveTo(x, y);
                        else ctx.lineTo(x, y);
                    }}
                    ctx.closePath();
                    ctx.fill();
                }}

                drawPentagon(512, 256, 72);
                drawPentagon(220, 140, 56);
                drawPentagon(804, 140, 56);
                drawPentagon(220, 372, 56);
                drawPentagon(804, 372, 56);
                drawPentagon(512, 60, 50);
                drawPentagon(512, 452, 50);

                const texture = new THREE.CanvasTexture(texCanvas);
                const ballGeo = new THREE.SphereGeometry(ballRadius, 64, 64);
                const ballMat = new THREE.MeshStandardMaterial({{
                    map: texture,
                    roughness: 0.35,
                    metalness: 0.1
                }});

                ball = new THREE.Mesh(ballGeo, ballMat);
                ball.position.set(0, ballRadius, 0);
                ball.castShadow = true;
                scene.add(ball);
            }}

            // 3D Math Coordinates
            const oPos = new THREE.Vector3(0, ballRadius, 0);
            const pPos = new THREE.Vector3(
                ballRadius * 0.72,
                ballRadius + (ballRadius * 0.68),
                ballRadius * 0.28
            );

            // CLICK 4 (State >= 11): Origin O(0,0,0) and Surface Point P(x,y,z)
            if (currentState >= 11) {{
                // Origin Point Core
                const oGeo = new THREE.SphereGeometry(0.25, 32, 32);
                const oMat = new THREE.MeshBasicMaterial({{ color: 0x1d4ed8 }});
                const oMesh = new THREE.Mesh(oGeo, oMat);
                oMesh.position.copy(oPos);
                scene.add(oMesh);

                // Surface Point P
                const pGeo = new THREE.SphereGeometry(0.28, 32, 32);
                const pMat = new THREE.MeshBasicMaterial({{ color: 0x1d4ed8 }});
                const pMesh = new THREE.Mesh(pGeo, pMat);
                pMesh.position.copy(pPos);
                scene.add(pMesh);

                // Make ball translucent so interior O(0,0,0) is clearly visible
                if (ball) {{
                    ball.material.transparent = true;
                    ball.material.opacity = 0.85;
                }}
            }}

            // CLICK 5 (State >= 12): 3D Vector Ray OP with Arrowhead
            if (currentState >= 12) {{
                const dir = new THREE.Vector3().subVectors(pPos, oPos);
                const len = dir.length();
                dir.normalize();

                const arrow = new THREE.ArrowHelper(dir, oPos, len, 0x1d4ed8, 0.8, 0.45);
                scene.add(arrow);
            }}

            // Project 3D Positions to HTML Badges
            function toScreen(vec) {{
                const v = vec.clone().project(camera);
                return {{
                    x: (v.x * 0.5 + 0.5) * width,
                    y: (-(v.y * 0.5) + 0.5) * height
                }};
            }}

            function updateBadges() {{
                if (currentState >= 11) {{
                    const oScr = toScreen(oPos);
                    const bO = document.getElementById('badge-o');
                    if (bO) {{
                        bO.style.display = 'block';
                        bO.style.left = (oScr.x - 70) + 'px';
                        bO.style.top = (oScr.y + 35) + 'px';
                    }}

                    const pScr = toScreen(pPos);
                    const bP = document.getElementById('badge-p');
                    if (bP) {{
                        bP.style.display = 'block';
                        bP.style.left = (pScr.x + 65) + 'px';
                        bP.style.top = (pScr.y - 25) + 'px';
                    }}
                }}

                if (currentState >= 12) {{
                    const mid = new THREE.Vector3().addVectors(oPos, pPos).multiplyScalar(0.5);
                    const opScr = toScreen(mid);
                    const bOP = document.getElementById('badge-op');
                    if (bOP) {{
                        bOP.style.display = 'block';
                        bOP.style.left = (opScr.x + 25) + 'px';
                        bOP.style.top = (opScr.y - 20) + 'px';
                    }}
                }}
            }}

            function animate() {{
                requestAnimationFrame(animate);
                renderer.render(scene, camera);
                updateBadges();
            }}
            animate();
        </script>
    </body>
    </html>
    """

    # Embed inside the right 60% panel container
    with st.container():
        st.markdown('<div class="webgl-container">', unsafe_allow_html=True)
        components.html(three_js_html, height=520, scrolling=False)
        st.markdown('</div>', unsafe_allow_html=True)
