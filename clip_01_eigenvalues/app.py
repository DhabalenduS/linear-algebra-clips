# Clip 01 - Eigenvalues and Eigenvectors
# Slides 1-3 Complete Implementation (True TV-Grade WebGL 3D Visualization)

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
# ADVANCE PRESENTATION (Clicks state 0 through 19)
# ============================================================

if st.session_state.presentation_state < 19:
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
# STATES 8-19 - SLIDE 3 (VISUALIZATION, OBSERVATION & CONCLUSION)
# ============================================================

elif 8 <= st.session_state.presentation_state <= 19:
    state = st.session_state.presentation_state

    # Construct Left Panel step-by-step
    left_panel_html = '<div class="slide3-left-panel">'

    # Observation Header & Points (States 15-17)
    if state >= 15:
        left_panel_html += '<div class="panel-section-title">Observation:</div>'
        left_panel_html += """
        <div class="panel-bullet">
            <span class="panel-bullet-icon">&#9679;</span>
            <span>Throughout the pumping process, the point <span class="math-term">P</span> is moving in the direction <span class="math-term">OP&#8407;</span> and finally reaches a point <span class="math-term">P'</span>.</span>
        </div>
        """

    if state >= 16:
        left_panel_html += """
        <div class="panel-bullet">
            <span class="panel-bullet-icon">&#9679;</span>
            <span>The point <span class="math-term">P</span> is scaled by a factor of <span class="math-term">&lambda; = OP' / OP</span>.</span>
        </div>
        """

    if state >= 17:
        left_panel_html += """
        <div class="panel-bullet">
            <span class="panel-bullet-icon">&#9679;</span>
            <span>The point <span class="math-term">P</span> is <strong>non-zero</strong> (<span class="math-term">P &ne; O</span>).</span>
        </div>
        """

    # Conclusion Header & Points (States 18-19)
    if state >= 18:
        left_panel_html += '<div class="panel-section-title" style="margin-top: 2.2vh; color: #991b1b; border-bottom: 2px solid #fecaca;">Conclusion:</div>'
        left_panel_html += """
        <div class="panel-bullet">
            <span class="panel-bullet-icon" style="color: #dc2626;">&#9679;</span>
            <span>The non-zero point <span class="math-term">P</span> does not change its direction while moving towards <span class="math-term">P'</span>, and is therefore defined as an <span class="highlight-keyword">eigenvector</span> corresponding to the <span class="highlight-keyword">eigenvalue &lambda;</span>.</span>
        </div>
        """

    if state >= 19:
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
                    position: relative;
                }}
                #pitch2d {{
                    position: absolute;
                    inset: 0;
                    width: 100%;
                    height: 100%;
                    z-index: 1;
                    display: block;
                }}
                #canvas3d {{
                    position: absolute;
                    inset: 0;
                    width: 100%;
                    height: 100%;
                    z-index: 2;
                    display: block;
                    pointer-events: none;
                }}
            </style>
        </head>
        <body>
            <canvas id="pitch2d"></canvas>
            <canvas id="canvas3d"></canvas>

            <script>
                const currentState = {state};

                // ============================================================
                // LAYER 1: Locked 2D Football Pitch
                // ============================================================
                function draw2DPitch() {{
                    const pCanvas = document.getElementById('pitch2d');
                    pCanvas.width = 2048;
                    pCanvas.height = 1536;
                    const ctx = pCanvas.getContext('2d');

                    const stripes = 10;
                    const sh = 1536 / stripes;
                    for (let i = 0; i < stripes; i++) {{
                        ctx.fillStyle = (i % 2 === 0) ? '#28792c' : '#308e36';
                        ctx.fillRect(0, i * sh, 2048, sh);
                    }}

                    const mx = 110;
                    const my = 140;
                    const pw = 2048 - (2 * mx);
                    const ph = 1536 - (2 * my);
                    const cx = 2048 / 2;
                    const cy = 1536 / 2;

                    ctx.strokeStyle = '#ffffff';
                    ctx.lineWidth = 15;
                    ctx.lineCap = 'round';

                    ctx.strokeRect(mx, my, pw, ph);

                    ctx.beginPath();
                    ctx.moveTo(cx, my);
                    ctx.lineTo(cx, my + ph);
                    ctx.stroke();

                    ctx.beginPath();
                    ctx.arc(cx, cy, 185, 0, Math.PI * 2);
                    ctx.stroke();

                    ctx.fillStyle = '#ffffff';
                    ctx.beginPath();
                    ctx.arc(cx, cy, 15, 0, Math.PI * 2);
                    ctx.fill();

                    ctx.strokeRect(mx, cy - 275, 270, 550);
                    ctx.strokeRect(mx, cy - 110, 100, 220);
                    ctx.beginPath();
                    ctx.arc(mx + 200, cy, 105, -Math.PI * 0.32, Math.PI * 0.32);
                    ctx.stroke();

                    ctx.strokeRect(mx + pw - 270, cy - 275, 270, 550);
                    ctx.strokeRect(mx + pw - 100, cy - 110, 100, 220);
                    ctx.beginPath();
                    ctx.arc(mx + pw - 200, cy, 105, Math.PI * 0.68, Math.PI * 1.32);
                    ctx.stroke();

                    const r = 35;
                    ctx.beginPath(); ctx.arc(mx, my, r, 0, Math.PI * 0.5); ctx.stroke();
                    ctx.beginPath(); ctx.arc(mx + pw, my, r, Math.PI * 0.5, Math.PI); ctx.stroke();
                    ctx.beginPath(); ctx.arc(mx, my + ph, r, -Math.PI * 0.5, 0); ctx.stroke();
                    ctx.beginPath(); ctx.arc(mx + pw, my + ph, r, Math.PI, -Math.PI * 0.5); ctx.stroke();
                }}
                draw2DPitch();

                // ============================================================
                // LAYER 2: 3D Football Broadcast Stage
                // ============================================================
                const canvas3d = document.getElementById('canvas3d');
                const scene = new THREE.Scene();

                const w = window.innerWidth;
                const h = window.innerHeight;

                const camera = new THREE.PerspectiveCamera(36, w / h, 0.1, 1000);
                camera.position.set(0, 7.5, 18);
                camera.lookAt(0, 0.6, 0);

                const renderer = new THREE.WebGLRenderer({{
                    canvas: canvas3d,
                    antialias: true,
                    alpha: true,
                    powerPreference: "high-performance"
                }});
                renderer.setSize(w, h);
                renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
                renderer.shadowMap.enabled = true;
                renderer.shadowMap.type = THREE.PCFSoftShadowMap;
                renderer.toneMapping = THREE.ACESFilmicToneMapping;
                renderer.toneMappingExposure = 1.15;
                renderer.localClippingEnabled = true;

                const ambient = new THREE.AmbientLight(0xffffff, 0.55);
                scene.add(ambient);

                const hemiLight = new THREE.HemisphereLight(0xffffff, 0x1e293b, 0.40);
                scene.add(hemiLight);

                const keyLight = new THREE.DirectionalLight(0xffffff, 1.65);
                keyLight.position.set(-10, 20, 16);
                scene.add(keyLight);

                const rimLight = new THREE.DirectionalLight(0xdbeafe, 0.70);
                rimLight.position.set(10, 12, -8);
                scene.add(rimLight);

                function makeMathTextSprite(text, dotColor) {{
                    const canvas = document.createElement('canvas');
                    canvas.width = 640;
                    canvas.height = 200;
                    const ctx = canvas.getContext('2d');

                    const x = 30, y = 25, w = 580, h = 150, r = 75;

                    ctx.fillStyle = 'rgba(255, 255, 255, 0.98)';
                    ctx.beginPath();
                    ctx.moveTo(x + r, y);
                    ctx.lineTo(x + w - r, y);
                    ctx.arc(x + w - r, y + r, r, -Math.PI / 2, Math.PI / 2);
                    ctx.lineTo(x + r, y + h);
                    ctx.arc(x + r, y + r, r, Math.PI / 2, -Math.PI / 2);
                    ctx.closePath();
                    ctx.fill();

                    ctx.strokeStyle = '#64748b';
                    ctx.lineWidth = 6;
                    ctx.stroke();

                    ctx.fillStyle = dotColor || '#2563eb';
                    ctx.beginPath();
                    ctx.arc(x + 65, y + r, 24, 0, Math.PI * 2);
                    ctx.fill();

                    ctx.font = "bold italic 60px Georgia, serif";
                    ctx.textAlign = "left";
                    ctx.textBaseline = "middle";
                    ctx.fillStyle = "#0f172a";
                    ctx.fillText(text, x + 115, y + r + 2);

                    const texture = new THREE.CanvasTexture(canvas);
                    const spriteMat = new THREE.SpriteMaterial({{
                        map: texture,
                        depthTest: false,
                        depthWrite: false
                    }});
                    const sprite = new THREE.Sprite(spriteMat);
                    sprite.renderOrder = 999;
                    return sprite;
                }}

                // ============================================================
                // SHARED SCOPED VARIABLES
                // ============================================================
                let ballGroup = null;
                let ballMat = null;
                let pentagonMat = null;
                let lineMat = null;
                let pLocal = null;

                const ballRadius = 1.35;
                const oPos = new THREE.Vector3(0, ballRadius, 0);

                function createContactShadowTexture() {{
                    const sCanvas = document.createElement('canvas');
                    sCanvas.width = 256;
                    sCanvas.height = 256;
                    const sCtx = sCanvas.getContext('2d');
                    const grad = sCtx.createRadialGradient(128, 128, 15, 128, 128, 120);
                    grad.addColorStop(0, 'rgba(10, 25, 10, 0.75)');
                    grad.addColorStop(0.5, 'rgba(15, 35, 15, 0.35)');
                    grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
                    sCtx.fillStyle = grad;
                    sCtx.fillRect(0, 0, 256, 256);
                    return new THREE.CanvasTexture(sCanvas);
                }}

                // ============================================================
                // CLICK 3 (State >= 10): 3D Soccer Ball
                // ============================================================
                if (currentState >= 10) {{
                    const shadowGeo = new THREE.PlaneGeometry(ballRadius * 2.2, ballRadius * 2.2);
                    const shadowMat = new THREE.MeshBasicMaterial({{
                        map: createContactShadowTexture(),
                        transparent: true,
                        depthWrite: false
                    }});
                    const shadowMesh = new THREE.Mesh(shadowGeo, shadowMat);
                    shadowMesh.rotation.x = -Math.PI / 2;
                    shadowMesh.position.set(0, 0.02, 0);
                    scene.add(shadowMesh);

                    ballGroup = new THREE.Group();
                    ballGroup.position.copy(oPos);

                    const ballGeo = new THREE.SphereGeometry(ballRadius, 64, 64);
                    ballMat = new THREE.MeshStandardMaterial({{
                        color: 0xf8fafc,
                        roughness: 0.18,
                        metalness: 0.10
                    }});
                    const whiteBall = new THREE.Mesh(ballGeo, ballMat);
                    ballGroup.add(whiteBall);

                    const phi = (1 + Math.sqrt(5)) / 2;
                    const rawVerts = [
                        [-1, phi, 0], [1, phi, 0], [-1, -phi, 0], [1, -phi, 0],
                        [0, -1, phi], [0, 1, phi], [0, -1, -phi], [0, 1, -phi],
                        [phi, 0, -1], [phi, 0, 1], [-phi, 0, -1], [-phi, 0, 1]
                    ];

                    const icoVerts = rawVerts.map(v => {{
                        const len = Math.hypot(v[0], v[1], v[2]);
                        return new THREE.Vector3(v[0] / len, v[1] / len, v[2] / len);
                    }});

                    pentagonMat = new THREE.MeshStandardMaterial({{
                        color: 0x0f172a,
                        roughness: 0.25,
                        metalness: 0.08,
                        side: THREE.DoubleSide
                    }});

                    const pentagonRadius = 0.39;
                    icoVerts.forEach(v => {{
                        const pentGeo = new THREE.CircleGeometry(pentagonRadius, 5);
                        const pentMesh = new THREE.Mesh(pentGeo, pentagonMat);
                        pentMesh.position.copy(v.clone().multiplyScalar(ballRadius * 1.002));
                        pentMesh.lookAt(v.clone().multiplyScalar(ballRadius * 2));
                        ballGroup.add(pentMesh);
                    }});

                    lineMat = new THREE.LineBasicMaterial({{ color: 0x64748b, linewidth: 2 }});
                    for (let i = 0; i < icoVerts.length; i++) {{
                        for (let j = i + 1; j < icoVerts.length; j++) {{
                            if (icoVerts[i].distanceTo(icoVerts[j]) < 1.1) {{
                                const p1 = icoVerts[i].clone().multiplyScalar(ballRadius * 1.001);
                                const p2 = icoVerts[j].clone().multiplyScalar(ballRadius * 1.001);
                                const lineGeo = new THREE.BufferGeometry().setFromPoints([p1, p2]);
                                const seam = new THREE.Line(lineGeo, lineMat);
                                ballGroup.add(seam);
                            }}
                        }}
                    }}

                    ballGroup.rotation.set(0.38, -0.75, 0.0);
                    scene.add(ballGroup);
                }}

                // ========================================================
                // CLICK 4 (State >= 11): Point P, Origin O, Badges
                // ========================================================
                if (currentState >= 11 && ballGroup) {{
                    const R = ballRadius;

                    const oGeo = new THREE.SphereGeometry(0.10, 32, 32);
                    const oMat = new THREE.MeshStandardMaterial({{
                        color: 0xf59e0b,
                        emissive: 0xf59e0b,
                        emissiveIntensity: 2.0
                    }});
                    const oSphere = new THREE.Mesh(oGeo, oMat);
                    oSphere.renderOrder = 100;
                    oSphere.position.set(0, 0, 0);
                    ballGroup.add(oSphere);

                    const cTopGeo = new THREE.SphereGeometry(0.10, 32, 32);
                    const cTopMat = new THREE.MeshStandardMaterial({{
                        color: 0xe11d48,
                        emissive: 0xe11d48,
                        emissiveIntensity: 2.0
                    }});
                    const cTopSphere = new THREE.Mesh(cTopGeo, cTopMat);
                    cTopSphere.position.set(0, R, 0);
                    ballGroup.add(cTopSphere);

                    const camDir = new THREE.Vector3().subVectors(camera.position, oPos).normalize();
                    const camRight = new THREE.Vector3(1, 0, 0);
                    const camUp = new THREE.Vector3().crossVectors(camDir, camRight).normalize();

                    const alpha = 45 * (Math.PI / 180);
                    const pWorldOffset = new THREE.Vector3()
                        .addScaledVector(camRight, R * Math.cos(alpha))
                        .addScaledVector(camUp, R * Math.sin(alpha));

                    const pWorld = new THREE.Vector3().addVectors(oPos, pWorldOffset);
                    
                    ballGroup.updateMatrixWorld(true);
                    pLocal = ballGroup.worldToLocal(pWorld.clone());

                    const pGeo = new THREE.SphereGeometry(0.11, 32, 32);
                    const pMat = new THREE.MeshStandardMaterial({{
                        color: 0x06b6d4,
                        emissive: 0x06b6d4,
                        emissiveIntensity: 2.5
                    }});
                    const pSphere = new THREE.Mesh(pGeo, pMat);
                    pSphere.position.copy(pLocal);
                    ballGroup.add(pSphere);

                    const axisMat = new THREE.LineDashedMaterial({{
                        color: 0xe11d48,
                        dashSize: 0.1,
                        gapSize: 0.05
                    }});
                    const axisGeo = new THREE.BufferGeometry().setFromPoints([
                        new THREE.Vector3(0, 0, 0),
                        new THREE.Vector3(0, R * 1.15, 0)
                    ]);
                    const axisLine = new THREE.Line(axisGeo, axisMat);
                    axisLine.computeLineDistances();
                    axisLine.renderOrder = 99;
                    ballGroup.add(axisLine);

                    const oLabel = makeMathTextSprite("O (0, 0, 0)", "#f59e0b");
                    oLabel.scale.set(1.4, 0.44, 1);
                    oLabel.position.set(-1.35, 0.2, 0.2);
                    ballGroup.add(oLabel);

                    const cLabel = makeMathTextSprite("C' (0, R, 0)", "#e11d48");
                    cLabel.scale.set(1.4, 0.44, 1);
                    cLabel.position.set(0.0, R + 0.35, 0.0);
                    ballGroup.add(cLabel);

                    const pLabel = makeMathTextSprite("P (x, y, z)", "#06b6d4");
                    pLabel.scale.set(1.4, 0.44, 1);
                    pLabel.position.copy(pLocal).add(new THREE.Vector3(0.75, 0.35, 0.0));
                    ballGroup.add(pLabel);
                }}

                // ============================================================
                // CLICK 5 (State >= 12): 3-Point Robust Coplanar Wedge Cut
                // ============================================================
                if (currentState >= 12 && ballGroup && ballMat && pentagonMat) {{
                    const R = ballRadius;
                    const oWorld = oPos.clone(); // (0, 1.35, 0)
                    const cWorld = oWorld.clone().add(new THREE.Vector3(0, R, 0)); // Top Apex

                    // 1. Vector from O to P in World Space
                    const camDir = new THREE.Vector3().subVectors(camera.position, oPos).normalize();
                    const camRight = new THREE.Vector3(1, 0, 0);
                    const camUp = new THREE.Vector3().crossVectors(camDir, camRight).normalize();

                    const alpha = 45 * (Math.PI / 180);
                    const vOP = new THREE.Vector3()
                        .addScaledVector(camRight, R * Math.cos(alpha))
                        .addScaledVector(camUp, R * Math.sin(alpha));

                    const pWorld = oWorld.clone().add(vOP);

                    // 2. Flanking Points P1 (left of P) and P2 (right of P)
                    const halfAngle = 25 * (Math.PI / 180);
                    const yAxis = new THREE.Vector3(0, 1, 0);

                    const p1World = oWorld.clone().add(vOP.clone().applyAxisAngle(yAxis, -halfAngle));
                    const p2World = oWorld.clone().add(vOP.clone().applyAxisAngle(yAxis, halfAngle));

                    // 3. Define Planes directly from 3 points: (O, C', P1) and (O, C', P2)
                    const plane1 = new THREE.Plane().setFromCoplanarPoints(oWorld, cWorld, p1World);
                    const plane2 = new THREE.Plane().setFromCoplanarPoints(oWorld, cWorld, p2World);

                    // Ensure both planes point into the wedge containing P
                    if (plane1.distanceToPoint(pWorld) > 0) plane1.negate();
                    if (plane2.distanceToPoint(pWorld) > 0) plane2.negate();

                    const cutPlanes = [plane1, plane2];

                    // 4. Apply to Ball Leather, Pentagons, and Seams
                    ballMat.clippingPlanes = cutPlanes;
                    ballMat.clipIntersection = true;
                    ballMat.needsUpdate = true;

                    pentagonMat.clippingPlanes = cutPlanes;
                    pentagonMat.clipIntersection = true;
                    pentagonMat.needsUpdate = true;

                    if (lineMat) {{
                        lineMat.clippingPlanes = cutPlanes;
                        lineMat.clipIntersection = true;
                        lineMat.needsUpdate = true;
                    }}
                }}
                function animate() {{
                    requestAnimationFrame(animate);
                    renderer.render(scene, camera);
                }}
                animate();

                window.addEventListener('resize', () => {{
                    draw2DPitch();
                    camera.aspect = window.innerWidth / window.innerHeight;
                    camera.updateProjectionMatrix();
                    renderer.setSize(window.innerWidth, window.innerHeight);
                }});
            </script>
        </body>
        </html>
        """

        components.html(three_js_code, height=620, scrolling=False)
