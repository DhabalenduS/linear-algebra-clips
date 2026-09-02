# Clip 01 — Eigenvalues and Eigenvectors
# Slides 1–3 Complete Implementation (True TV-Grade WebGL 3D Visualization)
# 10th Commit for slide 3
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Essence of Eigenvalues & Eigenvectors",
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
    top: 4.5vh;
    left: 50%;
    transform: translateX(-50%);
    width: 92vw;
    text-align: center;
    font-size: clamp(1.8rem, 2.8vw, 3.2rem);
    font-weight: 700;
    color: #0f172a;
    line-height: 1.2;
    z-index: 20;
}

.slide3-left-panel {
    position: absolute;
    left: 3.5vw;
    top: 14vh;
    width: 38vw;
    height: 80vh;
    z-index: 30;
    font-family: Georgia, "Times New Roman", serif;
    overflow-y: auto;
    padding-right: 1vw;
    box-sizing: border-box;
}

.panel-section-title {
    font-size: clamp(1.2rem, 1.6vw, 1.8rem);
    font-weight: 700;
    color: #1e3a8a;
    margin-top: 1.5vh;
    margin-bottom: 1vh;
    border-bottom: 2px solid #bfdbfe;
    padding-bottom: 4px;
}

.panel-bullet {
    font-size: clamp(0.95rem, 1.22vw, 1.35rem);
    line-height: 1.45;
    color: #1e293b;
    margin-bottom: 1.4vh;
    display: flex;
    align-items: flex-start;
}

.panel-bullet-icon {
    color: #2563eb;
    margin-right: 8px;
    font-weight: 700;
}

.math-term {
    font-weight: 700;
    color: #1d4ed8;
    background: #eff6ff;
    padding: 1px 6px;
    border-radius: 4px;
    border: 1px solid #dbeafe;
}

.highlight-keyword {
    font-weight: 700;
    color: #b91c1c;
}

.webgl-stage-box {
    position: absolute;
    left: 43vw;
    top: 14vh;
    width: 53.5vw;
    height: 80vh;
    z-index: 10;
    pointer-events: none;
}

/* CRUCIAL FIX: Let clicks fall through iframes to the advance button */
iframe {
    pointer-events: none !important;
    border: none !important;
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
# ADVANCE PRESENTATION (Clicks state 0 through 18)
# ============================================================

if st.session_state.presentation_state < 18:
    if st.button("advance", key="advance_button"):
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
# STATES 8–18 — SLIDE 3 (VISUALIZATION, OBSERVATION & CONCLUSION)
# ============================================================

elif 8 <= st.session_state.presentation_state <= 18:
    state = st.session_state.presentation_state

    # Construct Left Panel step-by-step
    left_panel_html = '<div class="slide3-left-panel">'

    # Observation Header & Points (Clicks 7–9 -> States 14–16)
    if state >= 14:
        left_panel_html += '<div class="panel-section-title">Observation:</div>'
        left_panel_html += """
        <div class="panel-bullet">
            <span class="panel-bullet-icon">&#9679;</span>
            <span>Throughout the pumping process, the point <span class="math-term">P</span> is moving in the direction <span class="math-term">OP&#8407;</span> and finally reaches a point <span class="math-term">P'</span>.</span>
        </div>
        """

    if state >= 15:
        left_panel_html += """
        <div class="panel-bullet">
            <span class="panel-bullet-icon">&#9679;</span>
            <span>The point <span class="math-term">P</span> is scaled by a factor of <span class="math-term">&lambda; = OP' / OP</span>.</span>
        </div>
        """

    if state >= 16:
        left_panel_html += """
        <div class="panel-bullet">
            <span class="panel-bullet-icon">&#9679;</span>
            <span>The point <span class="math-term">P</span> is <strong>non-zero</strong> (<span class="math-term">P &ne; O</span>).</span>
        </div>
        """

    # Conclusion Header & Points (Clicks 10–11 -> States 17–18)
    if state >= 17:
        left_panel_html += '<div class="panel-section-title" style="margin-top: 2.2vh; color: #991b1b; border-bottom: 2px solid #fecaca;">Conclusion:</div>'
        left_panel_html += """
        <div class="panel-bullet">
            <span class="panel-bullet-icon" style="color: #dc2626;">&#9679;</span>
            <span>The non-zero point <span class="math-term">P</span> does not change its direction while moving towards <span class="math-term">P'</span>, and is therefore defined as an <span class="highlight-keyword">eigenvector</span> corresponding to the <span class="highlight-keyword">eigenvalue &lambda;</span>.</span>
        </div>
        """

    if state >= 18:
        left_panel_html += """
        <div class="panel-bullet">
            <span class="panel-bullet-icon" style="color: #dc2626;">&#9679;</span>
            <span>Also, <strong>all other points</strong> on the surface of the football do not change their direction and are scaled by a factor of <span class="math-term">&lambda;</span>. Therefore, they are all <span class="highlight-keyword">eigenvectors</span> corresponding to the eigenvalue <span class="highlight-keyword">&lambda;</span>.</span>
        </div>
        """

    left_panel_html += '</div>'

    # Render Slide 3 Base
    st.html(
        f"""
        <div class="slide3">
            <div class="slide3-title">
                Visualization of Soccer Match
            </div>
            {left_panel_html}
        </div>
        """
    )

    # WebGL 3D Scene (State >= 9)
    if state >= 9:
        three_js_code = f"""
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
                }}
                #stage {{
                    width: 100%;
                    height: 100%;
                    position: relative;
                    border: 4px solid #ffffff;
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
                    background: rgba(255, 255, 255, 0.96);
                    border: 2px solid #1d4ed8;
                    color: #1d4ed8;
                    padding: 3px 8px;
                    border-radius: 7px;
                    font-family: Georgia, serif;
                    font-size: 14px;
                    font-weight: 800;
                    box-shadow: 0 3px 10px rgba(0,0,0,0.25);
                    white-space: nowrap;
                    transform: translate(-50%, -50%);
                    display: none;
                    pointer-events: none;
                    z-index: 100;
                }}
                .vector-badge {{
                    position: absolute;
                    background: #1d4ed8;
                    color: #ffffff;
                    padding: 3px 7px;
                    border-radius: 5px;
                    font-family: Georgia, serif;
                    font-size: 13px;
                    font-weight: 800;
                    box-shadow: 0 3px 8px rgba(0,0,0,0.3);
                    transform: translate(-50%, -50%);
                    display: none;
                    pointer-events: none;
                    z-index: 100;
                }}
                .pumped-badge {{
                    background: #dc2626 !important;
                    border: 2px solid #fee2e2 !important;
                    color: #ffffff !important;
                }}
            </style>
        </head>
        <body>
            <div id="stage">
                <canvas id="canvas3d"></canvas>
                <div id="badge-o" class="math-badge">O(0, 0, 0)</div>
                <div id="badge-p" class="math-badge">P(x, y, z)</div>
                <div id="badge-p-prime" class="math-badge pumped-badge">P'(x', y', z')</div>
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

                const camera = new THREE.PerspectiveCamera(38, width / height, 0.1, 1000);
                camera.position.set(0, 16, 26);
                camera.lookAt(0, 3.2, 0);

                const renderer = new THREE.WebGLRenderer({{ canvas: canvas, antialias: true }});
                renderer.setSize(width, height);
                renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
                renderer.shadowMap.enabled = true;
                renderer.shadowMap.type = THREE.PCFSoftShadowMap;

                // 2. Studio Lighting
                const ambient = new THREE.AmbientLight(0xffffff, 0.85);
                scene.add(ambient);

                const sun = new THREE.DirectionalLight(0xffffff, 1.25);
                sun.position.set(16, 28, 16);
                sun.castShadow = true;
                sun.shadow.mapSize.width = 1024;
                sun.shadow.mapSize.height = 1024;
                scene.add(sun);

                // CLICK 2 (State >= 9): 3D Soccer Pitch Ground
                const pitchGeo = new THREE.PlaneGeometry(42, 26);
                const pitchMat = new THREE.MeshStandardMaterial({{ color: 0x43a047, roughness: 0.85 }});
                const pitch = new THREE.Mesh(pitchGeo, pitchMat);
                pitch.rotation.x = -Math.PI / 2;
                pitch.receiveShadow = true;
                scene.add(pitch);

                const lineMat = new THREE.MeshBasicMaterial({{ color: 0xffffff }});
                
                const borderGeo = new THREE.EdgesGeometry(pitchGeo);
                const borderLines = new THREE.LineSegments(borderGeo, lineMat);
                borderLines.rotation.x = -Math.PI / 2;
                borderLines.position.y = 0.02;
                scene.add(borderLines);

                const halfGeo = new THREE.PlaneGeometry(0.14, 26);
                const halfLine = new THREE.Mesh(halfGeo, lineMat);
                halfLine.rotation.x = -Math.PI / 2;
                halfLine.position.y = 0.02;
                scene.add(halfLine);

                const circleGeo = new THREE.RingGeometry(3.8, 3.96, 64);
                const centerCircle = new THREE.Mesh(circleGeo, lineMat);
                centerCircle.rotation.x = -Math.PI / 2;
                centerCircle.position.y = 0.02;
                scene.add(centerCircle);

                // CLICK 3 (State >= 10): True 3D Soccer Ball
                let ball = null;
                const ballRadius = 3.0;
                const lambdaFactor = 1.45; // Scaling factor lambda = 1.45
                const oPos = new THREE.Vector3(0, 3.2, 0);

                // Initial surface point vector relative to origin
                const relP = new THREE.Vector3(ballRadius * 0.70, ballRadius * 0.65, ballRadius * 0.28);
                const pPos = new THREE.Vector3().addVectors(oPos, relP);
                const pPrimePos = new THREE.Vector3().addVectors(oPos, relP.clone().multiplyScalar(lambdaFactor));

                let currentPPos = pPos.clone();

                if (currentState >= 10) {{
                    const texCanvas = document.createElement('canvas');
                    texCanvas.width = 1024;
                    texCanvas.height = 512;
                    const ctx = texCanvas.getContext('2d');

                    ctx.fillStyle = '#f8fafc';
                    ctx.fillRect(0, 0, 1024, 512);

                    ctx.fillStyle = '#1c1c1c';
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
                        metalness: 0.1,
                        transparent: currentState >= 11,
                        opacity: currentState >= 11 ? 0.82 : 1.0
                    }});

                    ball = new THREE.Mesh(ballGeo, ballMat);
                    ball.position.copy(oPos);
                    ball.castShadow = true;
                    scene.add(ball);
                }}

                // CLICK 4 (State >= 11): Origin O(0,0,0) and Surface Point P Markers
                let oMesh = null;
                let pMesh = null;
                let pPrimeMesh = null;

                if (currentState >= 11) {{
                    const oGeo = new THREE.SphereGeometry(0.24, 32, 32);
                    const oMat = new THREE.MeshBasicMaterial({{ color: 0x1d4ed8 }});
                    oMesh = new THREE.Mesh(oGeo, oMat);
                    oMesh.position.copy(oPos);
                    scene.add(oMesh);

                    const pGeo = new THREE.SphereGeometry(0.26, 32, 32);
                    const pMat = new THREE.MeshBasicMaterial({{ color: 0x1d4ed8 }});
                    pMesh = new THREE.Mesh(pGeo, pMat);
                    pMesh.position.copy(pPos);
                    scene.add(pMesh);
                }}

                // CLICK 5 (State >= 12): Vector Arrow Ray OP
                let arrow = null;
                if (currentState >= 12) {{
                    const dir = new THREE.Vector3().subVectors(pPos, oPos);
                    const len = dir.length();
                    dir.normalize();

                    arrow = new THREE.ArrowHelper(dir, oPos, len, 0x1d4ed8, 0.8, 0.45);
                    scene.add(arrow);
                }}

                // CLICK 6 (State >= 13): Pumping Animation & Sound
                let pumpProgress = currentState >= 14 ? 1.0 : (currentState === 13 ? 0.0 : 0.0);

                // Synthesized Air Pumping Audio (Web Audio API)
                function playPumpingSound() {{
                    try {{
                        const AudioContext = window.AudioContext || window.webkitAudioContext;
                        if (!AudioContext) return;
                        const actx = new AudioContext();
                        const dur = 1.6;
                        const bufferSize = actx.sampleRate * dur;
                        const buffer = actx.createBuffer(1, bufferSize, actx.sampleRate);
                        const output = buffer.getChannelData(0);
                        for (let i = 0; i < bufferSize; i++) {{
                            output[i] = (Math.random() * 2 - 1) * Math.exp(-2.2 * (i / bufferSize));
                        }}
                        const whiteNoise = actx.createBufferSource();
                        whiteNoise.buffer = buffer;

                        const filter = actx.createBiquadFilter();
                        filter.type = "lowpass";
                        filter.frequency.setValueAtTime(320, actx.currentTime);
                        filter.frequency.linearRampToValueAtTime(950, actx.currentTime + 0.6);
                        filter.frequency.exponentialRampToValueAtTime(180, actx.currentTime + dur);

                        const gainNode = actx.createGain();
                        gainNode.gain.setValueAtTime(0.01, actx.currentTime);
                        gainNode.gain.linearRampToValueAtTime(0.35, actx.currentTime + 0.3);
                        gainNode.gain.exponentialRampToValueAtTime(0.001, actx.currentTime + dur);

                        whiteNoise.connect(filter);
                        filter.connect(gainNode);
                        gainNode.connect(actx.destination);
                        whiteNoise.start();
                    }} catch(e) {{}}
                }}

                if (currentState === 13) {{
                    playPumpingSound();
                }}

                if (currentState >= 13) {{
                    // P' Point marker at final inflated destination
                    const pPrimeGeo = new THREE.SphereGeometry(0.28, 32, 32);
                    const pPrimeMat = new THREE.MeshBasicMaterial({{ color: 0xdc2626 }});
                    pPrimeMesh = new THREE.Mesh(pPrimeGeo, pPrimeMat);
                    pPrimeMesh.position.copy(pPrimePos);
                    scene.add(pPrimeMesh);
                }}

                // Project 3D positions to 2D UI Screen Badges
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
                            bO.style.top = (oScr.y + 30) + 'px';
                        }}

                        const pScr = toScreen(pPos);
                        const bP = document.getElementById('badge-p');
                        if (bP) {{
                            bP.style.display = 'block';
                            bP.style.left = (pScr.x - 55) + 'px';
                            bP.style.top = (pScr.y - 25) + 'px';
                        }}
                    }}

                    if (currentState >= 12 && arrow) {{
                        const mid = new THREE.Vector3().addVectors(oPos, currentPPos).multiplyScalar(0.5);
                        const opScr = toScreen(mid);
                        const bOP = document.getElementById('badge-op');
                        if (bOP) {{
                            bOP.style.display = 'block';
                            bOP.style.left = (opScr.x + 24) + 'px';
                            bOP.style.top = (opScr.y - 18) + 'px';
                        }}
                    }}

                    if (currentState >= 13 && pumpProgress > 0.6) {{
                        const pPrimeScr = toScreen(pPrimePos);
                        const bPPrime = document.getElementById('badge-p-prime');
                        if (bPPrime) {{
                            bPPrime.style.display = 'block';
                            bPPrime.style.left = (pPrimeScr.x + 65) + 'px';
                            bPPrime.style.top = (pPrimeScr.y - 22) + 'px';
                        }}
                    }}
                }}

                function animate() {{
                    requestAnimationFrame(animate);

                    // Smooth Pumping Easing
                    if (currentState === 13 && pumpProgress < 1.0) {{
                        pumpProgress += 0.018;
                        if (pumpProgress > 1.0) pumpProgress = 1.0;
                    }}

                    if (currentState >= 13 && ball) {{
                        const currentScale = 1.0 + (lambdaFactor - 1.0) * pumpProgress;
                        ball.scale.set(currentScale, currentScale, currentScale);

                        // Current animated P vector
                        currentPPos.copy(oPos).add(relP.clone().multiplyScalar(currentScale));

                        if (arrow) {{
                            const dir = new THREE.Vector3().subVectors(currentPPos, oPos);
                            const len = dir.length();
                            dir.normalize();
                            arrow.setDirection(dir);
                            arrow.setLength(len, 0.8, 0.45);
                        }}
                    }}

                    renderer.render(scene, camera);
                    updateBadges();
                }}
                animate();
            </script>
        </body>
        </html>
        """

        # Embed the WebGL container with full click-through capability
        st.markdown('<div class="webgl-stage-box">', unsafe_allow_html=True)
        components.html(three_js_code, height=620, scrolling=False)
        st.markdown('</div>', unsafe_allow_html=True)
