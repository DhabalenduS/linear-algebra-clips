# Clip 01 — Eigenvalues and Eigenvectors
# Slides 1–3 (Finalized with True WebGL 3D Visualization)
# 6th Commit for Slide 3 for click 4 and 5 
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

/* RIGHT PANEL (60% width area): 3D WEBGL STAGE */
.webgl-stage-container {
    position: absolute;
    left: 40vw;
    top: 19vh;
    width: 55vw;
    height: 68vh;
    border: 5px solid #ffffff;
    border-radius: 2vh;
    box-shadow: 0 1.5vh 3vh rgba(0,0,0,0.18);
    overflow: hidden;
    background: #2e7d32;
    z-index: 5;
}

#three-canvas {
    width: 100%;
    height: 100%;
    display: block;
}

/* 3D Floating Mathematical Badges */
.math-3d-badge {
    position: absolute;
    background: rgba(255, 255, 255, 0.95);
    border: 2px solid #1d4ed8;
    color: #1d4ed8;
    padding: 4px 10px;
    border-radius: 6px;
    font-family: Georgia, serif;
    font-size: 1.1rem;
    font-weight: 800;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    pointer-events: none;
    z-index: 40;
    transition: all 0.3s ease;
}

.vector-3d-badge {
    position: absolute;
    background: #1d4ed8;
    color: #ffffff;
    padding: 3px 8px;
    border-radius: 4px;
    font-family: Georgia, serif;
    font-size: 1rem;
    font-weight: 800;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    pointer-events: none;
    z-index: 40;
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
# STATES 8–12 — SLIDE 3 (TRUE WEBGL 3D)
# ============================================================

elif 8 <= st.session_state.presentation_state <= 12:

    state = st.session_state.presentation_state

    # Include Three.js via CDN
    content = f"""
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

    <div class="slide3">
        <div class="slide3-title">
            Visualization of Soccer Match
        </div>
        <div class="slide3-left-panel"></div>

        <div class="webgl-stage-container" id="stage-container">
            <canvas id="three-canvas"></canvas>
            
            <!-- Floating HTML badges synced with 3D points -->
            <div id="badge-o" class="math-3d-badge" style="display: none;">O(0, 0, 0)</div>
            <div id="badge-p" class="math-3d-badge" style="display: none;">P(x, y, z)</div>
            <div id="badge-op" class="vector-3d-badge" style="display: none;">OP&#8407;</div>
        </div>
    </div>

    <script>
    (function() {{
        const container = document.getElementById('stage-container');
        const canvas = document.getElementById('three-canvas');
        const currentState = {state};

        if (!container || !canvas || typeof THREE === 'undefined') return;

        const width = container.clientWidth;
        const height = container.clientHeight;

        // 1. Scene & Camera
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x388e3c);

        const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
        camera.position.set(0, 14, 22);
        camera.lookAt(0, 0, 0);

        const renderer = new THREE.WebGLRenderer({{ canvas: canvas, antialias: true }});
        renderer.setSize(width, height);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer.shadowMap.enabled = true;
        renderer.shadowMap.type = THREE.PCFSoftShadowMap;

        // 2. Studio Lighting
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
        scene.add(ambientLight);

        const dirLight = new THREE.DirectionalLight(0xffffff, 1.1);
        dirLight.position.set(15, 25, 15);
        dirLight.castShadow = true;
        dirLight.shadow.mapSize.width = 1024;
        dirLight.shadow.mapSize.height = 1024;
        scene.add(dirLight);

        // CLICK 2 (State >= 9): 3D Soccer Pitch
        if (currentState >= 9) {{
            // Pitch Ground Plane
            const pitchGeo = new THREE.PlaneGeometry(36, 22);
            const pitchMat = new THREE.MeshStandardMaterial({{
                color: 0x43a047,
                roughness: 0.8,
                metalness: 0.1
            }});
            const pitch = new THREE.Mesh(pitchGeo, pitchMat);
            pitch.rotation.x = -Math.PI / 2;
            pitch.receiveShadow = true;
            scene.add(pitch);

            // Pitch Markings (Center Circle & Half Line)
            const lineMat = new THREE.MeshBasicMaterial({{ color: 0xffffff }});
            
            // Half line
            const lineGeo = new THREE.PlaneGeometry(0.12, 22);
            const halfLine = new THREE.Mesh(lineGeo, lineMat);
            halfLine.rotation.x = -Math.PI / 2;
            halfLine.position.y = 0.02;
            scene.add(halfLine);

            // Center Circle
            const circleGeo = new THREE.RingGeometry(3.6, 3.75, 64);
            const centerCircle = new THREE.Mesh(circleGeo, lineMat);
            centerCircle.rotation.x = -Math.PI / 2;
            centerCircle.position.y = 0.02;
            scene.add(centerCircle);
        }}

        // CLICK 3 (State >= 10): True 3D Volumetric Soccer Ball
        let ball = null;
        const ballRadius = 2.8;

        if (currentState >= 10) {{
            // Procedural High-Res Classic Soccer Ball Texture
            const texCanvas = document.createElement('canvas');
            texCanvas.width = 1024;
            texCanvas.height = 512;
            const ctx = texCanvas.getContext('2d');

            ctx.fillStyle = '#f8fafc';
            ctx.fillRect(0, 0, 1024, 512);

            // Draw clean pentagonal dark patches
            ctx.fillStyle = '#181818';
            function drawPentagon(cx, cy, r) {{
                ctx.beginPath();
                for (let i = 0; i < 5; i++) {{
                    const angle = (i * 2 * Math.PI / 5) - Math.PI / 2;
                    const x = cx + r * Math.cos(angle);
                    const y = cy + r * Math.sin(angle);
                    if (i === 0) ctx.moveTo(x, y);
                    else ctx.lineTo(x, y);
                }}
                ctx.closePath();
                ctx.fill();
            }}

            // Draw authentic pattern distribution
            drawPentagon(512, 256, 68);
            drawPentagon(220, 140, 52);
            drawPentagon(804, 140, 52);
            drawPentagon(220, 372, 52);
            drawPentagon(804, 372, 52);
            drawPentagon(512, 60, 48);
            drawPentagon(512, 452, 48);

            const texture = new THREE.CanvasTexture(texCanvas);
            const ballGeo = new THREE.SphereGeometry(ballRadius, 64, 64);
            const ballMat = new THREE.MeshStandardMaterial({{
                map: texture,
                roughness: 0.35,
                metalness: 0.12,
                wireframe: false
            }});

            ball = new THREE.Mesh(ballGeo, ballMat);
            ball.position.set(0, ballRadius, 0);
            ball.castShadow = true;
            ball.receiveShadow = true;
            scene.add(ball);
        }}

        // CLICK 4 (State >= 11): Center Origin O(0,0,0) and Surface Point P(x,y,z)
        const pPos = new THREE.Vector3(
            ballRadius * Math.cos(Math.PI / 4) * 0.85,
            ballRadius + (ballRadius * Math.sin(Math.PI / 4) * 0.85),
            ballRadius * 0.35
        );
        const oPos = new THREE.Vector3(0, ballRadius, 0);

        if (currentState >= 11) {{
            // Origin Point O(0,0,0)
            const oGeo = new THREE.SphereGeometry(0.24, 32, 32);
            const oMat = new THREE.MeshBasicMaterial({{ color: 0x1d4ed8 }});
            const oMesh = new THREE.Mesh(oGeo, oMat);
            oMesh.position.copy(oPos);
            scene.add(oMesh);

            // Surface Point P(x,y,z)
            const pGeo = new THREE.SphereGeometry(0.26, 32, 32);
            const pMat = new THREE.MeshBasicMaterial({{ color: 0x1d4ed8 }});
            const pMesh = new THREE.Mesh(pGeo, pMat);
            pMesh.position.copy(pPos);
            scene.add(pMesh);

            // Make ball slightly translucent so interior O(0,0,0) is clearly visible
            if (ball) {{
                ball.material.transparent = true;
                ball.material.opacity = 0.82;
            }}
        }}

        // CLICK 5 (State >= 12): 3D Vector Ray OP with Arrowhead
        if (currentState >= 12) {{
            const dir = new THREE.Vector3().subVectors(pPos, oPos);
            const length = dir.length();
            dir.normalize();

            // 3D Arrow Cylinder + Cone
            const arrowColor = 0x1d4ed8;
            const arrowHelper = new THREE.ArrowHelper(dir, oPos, length, arrowColor, 0.7, 0.4);
            arrowHelper.line.material.linewidth = 4;
            scene.add(arrowHelper);
        }}

        // Render loop & Projecting 3D Coordinates to Screen Badges
        function toScreenPosition(objVec, camera) {{
            const vector = objVec.clone();
            vector.project(camera);
            return {{
                x: (vector.x * 0.5 + 0.5) * width,
                y: (-(vector.y * 0.5) + 0.5) * height
            }};
        }}

        function updateBadges() {{
            if (currentState >= 11) {{
                const oScr = toScreenPosition(oPos, camera);
                const badgeO = document.getElementById('badge-o');
                if (badgeO) {{
                    badgeO.style.display = 'block';
                    badgeO.style.left = (oScr.x - 120) + 'px';
                    badgeO.style.top = (oScr.y + 10) + 'px';
                }}

                const pScr = toScreenPosition(pPos, camera);
                const badgeP = document.getElementById('badge-p');
                if (badgeP) {{
                    badgeP.style.display = 'block';
                    badgeP.style.left = (pScr.x + 20) + 'px';
                    badgeP.style.top = (pScr.y - 25) + 'px';
                }}
            }}

            if (currentState >= 12) {{
                const midPos = new THREE.Vector3().addVectors(oPos, pPos).multiplyScalar(0.5);
                const opScr = toScreenPosition(midPos, camera);
                const badgeOP = document.getElementById('badge-op');
                if (badgeOP) {{
                    badgeOP.style.display = 'block';
                    badgeOP.style.left = (opScr.x + 10) + 'px';
                    badgeOP.style.top = (opScr.y - 30) + 'px';
                }}
            }}
        }}

        function animate() {{
            requestAnimationFrame(animate);
            renderer.render(scene, camera);
            updateBadges();
        }}
        animate();

    }})();
    </script>
    """

    st.html(content)
