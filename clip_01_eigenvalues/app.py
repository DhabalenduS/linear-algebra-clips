# Clip 01 - Eigenvalues and Eigenvectors
# Slides 1-3 Complete Implementation (True TV-Grade WebGL 3D Visualization)
# Immediately before version slide 3 upto Clic 3 is locked
# In this commit we are trying to achieve Click 4 with OP
#But this will change the Click 3 also, as 3D Football  will be slightly transparanet 

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="The Essence of Eigenvalues & Eigenvectors",
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

    iframe {
        position: fixed !important;
        left: 43vw !important;
        top: 14vh !important;
        width: 53.5vw !important;
        height: 80vh !important;
        z-index: 25 !important;
        border: 3px solid #e2e8f0 !important;
        border-radius: 16px !important;
        pointer-events: none !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15) !important;
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
# STATE 0 - BLANK
# ============================================================

if st.session_state.presentation_state == 0:
    pass

# ============================================================
# STATE 1 - SLIDE 1
# ============================================================

elif st.session_state.presentation_state == 1:
    st.html(
        """
        <div class="slide">
            <div class="slide1-content">
                <div class="slide-title">
                    Welcome to
                </div>
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
        </div>
        """
    )

# ============================================================
# STATES 2-7 - SLIDE 2
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
# STATES 8-18 - SLIDE 3 (VISUALIZATION, OBSERVATION & CONCLUSION)
# ============================================================

elif 8 <= st.session_state.presentation_state <= 18:
    state = st.session_state.presentation_state

    # Construct Left Panel step-by-step
    left_panel_html = '<div class="slide3-left-panel">'

    # Observation Header & Points (Clicks 7-9 -> States 14-16)
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

    # Conclusion Header & Points (Clicks 10-11 -> States 17-18)
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
                * {{
                    box-sizing: border-box;
                    margin: 0;
                    padding: 0;
                }}
                html, body {{
                    width: 100%;
                    height: 100%;
                    overflow: hidden;
                    background: transparent;
                }}
                #canvas3d {{
                    width: 100%;
                    height: 100%;
                    display: block;
                }}
            </style>
        </head>
        <body>
            <canvas id="canvas3d"></canvas>

            <script>
                const currentState = {state};
                const canvas = document.getElementById('canvas3d');

                // 1. Scene Setup
                const scene = new THREE.Scene();

                const w = window.innerWidth;
                const h = window.innerHeight;

                // Overhead TV Camera calibrated to stage dimensions
                const camera = new THREE.PerspectiveCamera(40, w / h, 0.1, 1000);
                camera.position.set(0, 30, 0.01);
                camera.lookAt(0, 0, 0);

                const renderer = new THREE.WebGLRenderer({{
                    canvas: canvas,
                    antialias: true,
                    alpha: true,
                    powerPreference: "high-performance"
                }});
                renderer.setSize(w, h);
                renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
                renderer.shadowMap.enabled = true;
                renderer.shadowMap.type = THREE.PCFSoftShadowMap;
                renderer.toneMapping = THREE.ACESFilmicToneMapping;
                renderer.toneMappingExposure = 1.12;

                // 2. Broadcast Lighting Rig
                const ambient = new THREE.AmbientLight(0xffffff, 0.90);
                scene.add(ambient);

                const hemiLight = new THREE.HemisphereLight(0xebfbee, 0x1b431e, 0.45);
                scene.add(hemiLight);

                const floodLight = new THREE.DirectionalLight(0xffffff, 1.15);
                floodLight.position.set(10, 35, 10);
                floodLight.castShadow = true;
                floodLight.shadow.mapSize.width = 2048;
                floodLight.shadow.mapSize.height = 2048;
                floodLight.shadow.bias = -0.0003;
                scene.add(floodLight);

                // ============================================================
                // CLICK 2 (State >= 9): Football Pitch Fills Entire Card Edge-to-Edge
                // ============================================================
                function createPitchTexture() {{
                    const pCanvas = document.createElement('canvas');
                    pCanvas.width = 2048;
                    pCanvas.height = 1536; // 4:3 aspect ratio matching the 53.5vw / 80vh stage box
                    const ctx = pCanvas.getContext('2d');

                    // 1. Edge-to-Edge Lawn Stripes
                    const stripes = 10;
                    const sh = 1536 / stripes;
                    for (let i = 0; i < stripes; i++) {{
                        ctx.fillStyle = (i % 2 === 0) ? '#28792c' : '#308e36';
                        ctx.fillRect(0, i * sh, 2048, sh);
                    }}

                    // 2. Perfectly Uniform Outer Green Border (140px on all sides)
                    const mx = 110;
                    const my = 140;
                    const pw = 2048 - (2 * mx); // 1768
                    const ph = 1536 - (2 * my); // 1256
                    const cx = 2048 / 2;
                    const cy = 1536 / 2;

                    ctx.strokeStyle = '#ffffff';
                    ctx.lineWidth = 15;
                    ctx.lineCap = 'round';

                    // Full Outer Boundary Line
                    ctx.strokeRect(mx, my, pw, ph);

                    // Halfway Line
                    ctx.beginPath();
                    ctx.moveTo(cx, my);
                    ctx.lineTo(cx, my + ph);
                    ctx.stroke();

                    // Center Circle & Center Spot
                    ctx.beginPath();
                    ctx.arc(cx, cy, 185, 0, Math.PI * 2);
                    ctx.stroke();

                    ctx.fillStyle = '#ffffff';
                    ctx.beginPath();
                    ctx.arc(cx, cy, 15, 0, Math.PI * 2);
                    ctx.fill();

                    // Left Penalty Box & Goal Box
                    ctx.strokeRect(mx, cy - 275, 270, 550);
                    ctx.strokeRect(mx, cy - 110, 100, 220);
                    ctx.beginPath();
                    ctx.arc(mx + 200, cy, 105, -Math.PI * 0.32, Math.PI * 0.32);
                    ctx.stroke();

                    // Right Penalty Box & Goal Box
                    ctx.strokeRect(mx + pw - 270, cy - 275, 270, 550);
                    ctx.strokeRect(mx + pw - 100, cy - 110, 100, 220);
                    ctx.beginPath();
                    ctx.arc(mx + pw - 200, cy, 105, Math.PI * 0.68, Math.PI * 1.32);
                    ctx.stroke();

                    // Corner Arcs
                    const r = 35;
                    ctx.beginPath(); ctx.arc(mx, my, r, 0, Math.PI * 0.5); ctx.stroke();
                    ctx.beginPath(); ctx.arc(mx + pw, my, r, Math.PI * 0.5, Math.PI); ctx.stroke();
                    ctx.beginPath(); ctx.arc(mx, my + ph, r, -Math.PI * 0.5, 0); ctx.stroke();
                    ctx.beginPath(); ctx.arc(mx + pw, my + ph, r, Math.PI, -Math.PI * 0.5); ctx.stroke();

                    return new THREE.CanvasTexture(pCanvas);
                }}

                if (currentState >= 9) {{
                    // Pitch sized to completely cover the container view
                    const pitchGeo = new THREE.PlaneGeometry(32, 24);
                    const pitchMat = new THREE.MeshStandardMaterial({{
                        map: createPitchTexture(),
                        roughness: 0.85,
                        metalness: 0.05
                    }});
                    const pitch = new THREE.Mesh(pitchGeo, pitchMat);
                    pitch.rotation.x = -Math.PI / 2;
                    pitch.position.set(0, 0, 0);
                    pitch.receiveShadow = true;
                    scene.add(pitch);
                }}

                // ============================================================
                // CLICK 3 (State >= 10): 3D Classic Black-and-White Soccer Ball
                // ============================================================
                let ball = null;
                const ballRadius = 2.0;
                const oPos = new THREE.Vector3(0, ballRadius, 0);

                function createSoccerBallTexture() {{
                    const bCanvas = document.createElement('canvas');
                    bCanvas.width = 2048;
                    bCanvas.height = 1024;
                    const ctx = bCanvas.getContext('2d');

                    ctx.fillStyle = '#f8fafc';
                    ctx.fillRect(0, 0, 2048, 1024);

                    ctx.fillStyle = '#111827';
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
                        ctx.strokeStyle = '#374151';
                        ctx.lineWidth = 5;
                        ctx.stroke();
                    }}

                    const rows = 4;
                    const cols = 8;
                    for (let r = 0; r < rows; r++) {{
                        for (let c = 0; c < cols; c++) {{
                            if ((r + c) % 2 === 0) {{
                                drawPentagon((c + 0.5) * (2048 / cols), (r + 0.5) * (1024 / rows), 68);
                            }}
                        }}
                    }}

                    const tex = new THREE.CanvasTexture(bCanvas);
                    tex.wrapS = THREE.RepeatWrapping;
                    tex.wrapT = THREE.ClampToEdgeWrapping;
                    return tex;
                }}

                if (currentState >= 10) {{
                    const ballGeo = new THREE.SphereGeometry(ballRadius, 64, 64);
                    const ballMat = new THREE.MeshStandardMaterial({{
                        map: createSoccerBallTexture(),
                        roughness: 0.32,
                        metalness: 0.12,
                        transparent: currentState >= 11,
                        opacity: currentState >= 11 ? 0.88 : 1.0
                    }});

                    ball = new THREE.Mesh(ballGeo, ballMat);
                    ball.position.copy(oPos);
                    ball.castShadow = true;
                    ball.receiveShadow = true;
                    scene.add(ball);
                }}

                // ============================================================
                // Helper: Crisp 2D Billboard Label Badges
                // ============================================================
                function createLabelSprite(text, bgCol, textCol) {{
                    const lCanvas = document.createElement('canvas');
                    lCanvas.width = 320;
                    lCanvas.height = 120;
                    const ctx = lCanvas.getContext('2d');

                    // Rounded Pill Badge
                    ctx.fillStyle = bgCol;
                    ctx.beginPath();
                    if (ctx.roundRect) {{
                        ctx.roundRect(10, 15, 300, 90, 20);
                    }} else {{
                        ctx.rect(10, 15, 300, 90);
                    }}
                    ctx.fill();
                    ctx.strokeStyle = '#ffffff';
                    ctx.lineWidth = 4;
                    ctx.stroke();

                    // Label Text
                    ctx.font = 'bold 40px Georgia, "Times New Roman", serif';
                    ctx.fillStyle = textCol;
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'middle';
                    ctx.fillText(text, 160, 60);

                    const tex = new THREE.CanvasTexture(lCanvas);
                    const mat = new THREE.SpriteMaterial({{
                        map: tex,
                        depthTest: false,
                        depthWrite: false
                    }});
                    const sprite = new THREE.Sprite(mat);
                    sprite.scale.set(2.4, 0.9, 1.0);
                    sprite.renderOrder = 1000;
                    return sprite;
                }}

                // ============================================================
                // CLICK 4 (State >= 11): Center O(0,0,0) and Surface Point P(x,y,z) in 1st Octant
                // ============================================================
                if (currentState >= 11) {{
                    // 1. Center O(0,0,0) Marker (Glowing Core)
                    const oGeo = new THREE.SphereGeometry(0.18, 32, 32);
                    const oMat = new THREE.MeshBasicMaterial({{
                        color: 0xdc2626, // Crimson Red
                        depthTest: false,
                        depthWrite: false
                    }});
                    const oMarker = new THREE.Mesh(oGeo, oMat);
                    oMarker.position.copy(oPos);
                    oMarker.renderOrder = 999;
                    scene.add(oMarker);

                    // Center Label O(0,0,0)
                    const oLabel = createLabelSprite('O(0, 0, 0)', '#dc2626', '#ffffff');
                    oLabel.position.set(oPos.x - 1.3, oPos.y - 0.4, oPos.z + 0.3);
                    scene.add(oLabel);

                    // 2. Surface Point P(x,y,z) in 1st Octant (x > 0, y > 0, z > 0)
                    // Unit direction vector normalized in 1st octant:
                    const pDir = new THREE.Vector3(1.1, 1.25, 1.0).normalize();
                    const pWorld = oPos.clone().add(pDir.clone().multiplyScalar(ballRadius));

                    const pGeo = new THREE.SphereGeometry(0.18, 32, 32);
                    const pMat = new THREE.MeshBasicMaterial({{
                        color: 0x2563eb, // Royal Blue
                        depthTest: false,
                        depthWrite: false
                    }});
                    const pMarker = new THREE.Mesh(pGeo, pMat);
                    pMarker.position.copy(pWorld);
                    pMarker.renderOrder = 999;
                    scene.add(pMarker);

                    // Point Label P(x,y,z)
                    const pLabel = createLabelSprite('P(x, y, z)', '#1e40af', '#ffffff');
                    pLabel.position.set(pWorld.x + 0.6, pWorld.y + 0.65, pWorld.z + 0.4);
                    scene.add(pLabel);
                }}

                // Render Loop
                function animate() {{
                    requestAnimationFrame(animate);
                    renderer.render(scene, camera);
                }}
                animate();
                window.addEventListener('resize', () => {{
                    camera.aspect = window.innerWidth / window.innerHeight;
                    camera.updateProjectionMatrix();
                    renderer.setSize(window.innerWidth, window.innerHeight);
                }});
            </script>
        </body>
        </html>
        """

        components.html(three_js_code, height=620, scrolling=False)
