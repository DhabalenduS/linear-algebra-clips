# Clip 01 - Eigenvalues and Eigenvectors
# Slide 1-3 Implementation (Cleaned Click 4 & 2R Slow-Motion Inflation)

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
# ADVANCE PRESENTATION
# ============================================================

if st.session_state.presentation_state < 25:
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
# STATES 8+ - SLIDE 3 (VISUALIZATION)
# ============================================================

elif 8 <= st.session_state.presentation_state <= 25:
    state = st.session_state.presentation_state

    # Render Slide 3 Base
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
                // LAYER 1 (Click 2 / State >= 9): 2D Football Pitch
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

                    const mx = 110, my = 140;
                    const pw = 2048 - (2 * mx);
                    const ph = 1536 - (2 * my);
                    const cx = 2048 / 2;
                    const cy = 1536 / 2;

                    ctx.strokeStyle = '#ffffff';
                    ctx.lineWidth = 15;
                    ctx.lineCap = 'round';

                    ctx.strokeRect(mx, my, pw, ph);

                    // Halfway Line
                    ctx.beginPath();
                    ctx.moveTo(cx, my);
                    ctx.lineTo(cx, my + ph);
                    ctx.stroke();

                    // Center Circle & Spot
                    ctx.beginPath();
                    ctx.arc(cx, cy, 185, 0, Math.PI * 2);
                    ctx.stroke();

                    ctx.fillStyle = '#ffffff';
                    ctx.beginPath();
                    ctx.arc(cx, cy, 15, 0, Math.PI * 2);
                    ctx.fill();

                    // Penalty Boxes
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

                    // Corner Arcs
                    const r = 35;
                    ctx.beginPath(); ctx.arc(mx, my, r, 0, Math.PI * 0.5); ctx.stroke();
                    ctx.beginPath(); ctx.arc(mx + pw, my, r, Math.PI * 0.5, Math.PI); ctx.stroke();
                    ctx.beginPath(); ctx.arc(mx, my + ph, r, -Math.PI * 0.5, 0); ctx.stroke();
                    ctx.beginPath(); ctx.arc(mx + pw, my + ph, r, Math.PI, -Math.PI * 0.5); ctx.stroke();
                }}
                draw2DPitch();

                // ============================================================
                // LAYER 2 (Click 3 / State >= 10): 3D Football Scene
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

                // Lighting
                const ambient = new THREE.AmbientLight(0xffffff, 0.65);
                scene.add(ambient);

                const hemiLight = new THREE.HemisphereLight(0xffffff, 0x18181b, 0.45);
                scene.add(hemiLight);

                const keyLight = new THREE.DirectionalLight(0xffffff, 1.65);
                keyLight.position.set(-10, 20, 16);
                scene.add(keyLight);

                const rimLight = new THREE.DirectionalLight(0xffffff, 0.70);
                rimLight.position.set(10, 12, -8);
                scene.add(rimLight);

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

                function createCavityTexture() {{
                    const c = document.createElement('canvas');
                    c.width = 512;
                    c.height = 512;
                    const ctx = c.getContext('2d');
                    const grad = ctx.createRadialGradient(256, 340, 30, 256, 256, 250);
                    grad.addColorStop(0, '#94a3b8');
                    grad.addColorStop(0.55, '#475569');
                    grad.addColorStop(0.85, '#1e293b');
                    grad.addColorStop(1.0, '#0f172a');
                    ctx.fillStyle = grad;
                    ctx.fillRect(0, 0, 512, 512);
                    return new THREE.CanvasTexture(c);
                }}

                function makeCleanTextSprite(text, color) {{
                    const canvas = document.createElement('canvas');
                    canvas.width = 640;
                    canvas.height = 160;
                    const ctx = canvas.getContext('2d');
                    
                    ctx.font = "bold italic 68px Georgia, serif";
                    ctx.textAlign = "center";
                    ctx.textBaseline = "middle";
                    
                    ctx.strokeStyle = "#ffffff";
                    ctx.lineWidth = 10;
                    ctx.lineJoin = "round";
                    ctx.strokeText(text, 320, 80);
                    
                    ctx.fillStyle = color || "#1e3a8a";
                    ctx.fillText(text, 320, 80);
                    
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

                const ballRadius = 1.35;
                const oPos = new THREE.Vector3(0, ballRadius, 0);
                const R = ballRadius;

                // Cartesian direction for Point P
                const pAngle = 38 * (Math.PI / 180);
                const pUnitDir = new THREE.Vector3(
                    Math.cos(pAngle),
                    Math.sin(pAngle),
                    0.15
                ).normalize();

                const pLocalInitial = pUnitDir.clone().multiplyScalar(R);

                let ballRootGroup = null;
                let expandableBallBody = null;
                let rayGroup = null;
                let rayShaft = null;
                let rayHead = null;
                let pPrimeSphere = null;
                let pPrimeLabel = null;
                let shadowMesh = null;

                // ============================================================
                // CONSTRUCT 3D SCENE
                // Click 3 (State 10): 3D Football appears
                // Click 4 (State 11): Point P(x, y, z) appears on surface
                // Click 5 (State 12): Wedge Cut + Concave Inner Bowl + Point O revealed
                // Click 6 (State 13): Ray OP appears with arrowhead
                // Click 7 (State 14): Smooth Pumping Animation (2R Scale, 6.4s)
                // ============================================================
                if (currentState >= 10) {{
                    // 1. Soft Contact Shadow
                    const shadowGeo = new THREE.PlaneGeometry(R * 2.2, R * 2.2);
                    const shadowMat = new THREE.MeshBasicMaterial({{
                        map: createContactShadowTexture(),
                        transparent: true,
                        depthWrite: false
                    }});
                    shadowMesh = new THREE.Mesh(shadowGeo, shadowMat);
                    shadowMesh.rotation.x = -Math.PI / 2;
                    shadowMesh.position.set(0, 0.02, 0);
                    scene.add(shadowMesh);

                    // 2. Root Group (Center O)
                    ballRootGroup = new THREE.Group();
                    ballRootGroup.position.copy(oPos);
                    ballRootGroup.lookAt(camera.position);
                    scene.add(ballRootGroup);

                    // 3. Expandable Ball Body
                    expandableBallBody = new THREE.Group();
                    ballRootGroup.add(expandableBallBody);

                    const isWedgeCut = currentState >= 12; // Click 5
                    const wedgeSpan = isWedgeCut ? (90 * Math.PI / 180) : 0;
                    const sphereStart = pAngle + (wedgeSpan / 2) + Math.PI;
                    const sphereArc = Math.PI * 2 - wedgeSpan;

                    const ballMat = new THREE.MeshStandardMaterial({{
                        color: 0xf8fafc,
                        roughness: 0.18,
                        metalness: 0.10,
                        side: THREE.FrontSide
                    }});

                    const wallMat = new THREE.MeshStandardMaterial({{
                        color: 0x475569,
                        roughness: 0.50,
                        metalness: 0.10,
                        side: THREE.DoubleSide
                    }});

                    const innerMat = new THREE.MeshStandardMaterial({{
                        map: createCavityTexture(),
                        roughness: 0.75,
                        metalness: 0.05,
                        side: THREE.DoubleSide
                    }});

                    if (!isWedgeCut) {{
                        const ballGeo = new THREE.SphereGeometry(R, 64, 64);
                        const whiteBall = new THREE.Mesh(ballGeo, ballMat);
                        whiteBall.rotation.x = Math.PI / 2;
                        expandableBallBody.add(whiteBall);
                    }} else {{
                        // Click 5: Upper Sliced Shell
                        const upperGeo = new THREE.SphereGeometry(R, 64, 32, sphereStart, sphereArc, 0, Math.PI / 2);
                        const upperMesh = new THREE.Mesh(upperGeo, ballMat);
                        upperMesh.rotation.x = Math.PI / 2;
                        expandableBallBody.add(upperMesh);

                        // Click 5: Concave Inner Bladder Bowl
                        const backGeo = new THREE.SphereGeometry(R, 64, 32, 0, Math.PI * 2, Math.PI / 2, Math.PI / 2);
                        const backMesh = new THREE.Mesh(backGeo, innerMat);
                        backMesh.rotation.x = Math.PI / 2;
                        expandableBallBody.add(backMesh);

                        // Click 5: Framing Wall
                        const wallGeo1 = new THREE.CircleGeometry(R, 32, 0, Math.PI / 2);
                        const wall1 = new THREE.Mesh(wallGeo1, wallMat);
                        wall1.rotation.x = Math.PI / 2;
                        wall1.rotation.z = sphereStart;
                        expandableBallBody.add(wall1);

                        // Click 5: Center Point O(0, 0, 0) & Label Revealed inside Cavity
                        const oGeo = new THREE.SphereGeometry(0.14, 32, 32);
                        const oMat = new THREE.MeshStandardMaterial({{
                            color: 0x06b6d4,
                            emissive: 0x06b6d4,
                            emissiveIntensity: 2.5
                        }});
                        const oSphere = new THREE.Mesh(oGeo, oMat);
                        oSphere.position.set(0, 0, 0);
                        ballRootGroup.add(oSphere);

                        const oLabel = makeCleanTextSprite("O (0, 0, 0)", "#dc2626");
                        oLabel.scale.set(1.3, 0.40, 1);
                        oLabel.position.set(-0.35, 0.28, 0.05);
                        ballRootGroup.add(oLabel);
                    }}

                    // Classic Pentagon Seams
                    const decoGroup = new THREE.Group();
                    expandableBallBody.add(decoGroup);

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

                    const pentagonMat = new THREE.MeshStandardMaterial({{
                        color: 0x0f172a,
                        roughness: 0.25,
                        metalness: 0.08,
                        side: THREE.DoubleSide
                    }});

                    const lineMat = new THREE.LineBasicMaterial({{
                        color: 0x64748b,
                        linewidth: 2
                    }});

                    function isInsideWedge(v) {{
                        if (!isWedgeCut) return false;
                        return (v.x > -0.1 && v.y > -0.2);
                    }}

                    const pentagonRadius = 0.39;
                    icoVerts.forEach(v => {{
                        if (!isInsideWedge(v)) {{
                            const pentGeo = new THREE.CircleGeometry(pentagonRadius, 5);
                            const pentMesh = new THREE.Mesh(pentGeo, pentagonMat);
                            pentMesh.position.copy(v.clone().multiplyScalar(R * 1.002));
                            pentMesh.lookAt(v.clone().multiplyScalar(R * 2));
                            decoGroup.add(pentMesh);
                        }}
                    }});

                    for (let i = 0; i < icoVerts.length; i++) {{
                        for (let j = i + 1; j < icoVerts.length; j++) {{
                            if (icoVerts[i].distanceTo(icoVerts[j]) < 1.1) {{
                                if (!isInsideWedge(icoVerts[i]) && !isInsideWedge(icoVerts[j])) {{
                                    const p1 = icoVerts[i].clone().multiplyScalar(R * 1.001);
                                    const p2 = icoVerts[j].clone().multiplyScalar(R * 1.001);
                                    const lineGeo = new THREE.BufferGeometry().setFromPoints([p1, p2]);
                                    const seam = new THREE.Line(lineGeo, lineMat);
                                    decoGroup.add(seam);
                                }}
                            }}
                        }}
                    }}

                    // ========================================================
                    // CLICK 4 (State >= 11): Only Fixed Point P on the Surface
                    // ========================================================
                    if (currentState >= 11) {{
                        const pGeo = new THREE.SphereGeometry(0.10, 32, 32);
                        const pMat = new THREE.MeshStandardMaterial({{
                            color: 0x06b6d4,
                            emissive: 0x06b6d4,
                            emissiveIntensity: 2.5
                        }});
                        const pSphere = new THREE.Mesh(pGeo, pMat);
                        pSphere.position.copy(pLocalInitial);
                        ballRootGroup.add(pSphere);

                        const pLabel = makeCleanTextSprite("P (x, y, z)", "#dc2626");
                        pLabel.scale.set(1.5, 0.38, 1);
                        pLabel.position.copy(pLocalInitial).add(new THREE.Vector3(-0.05, 0.42, 0.05));
                        ballRootGroup.add(pLabel);
                    }}

                    // ========================================================
                    // CLICK 6 (State >= 13): Ray OP with Arrowhead Appears
                    // ========================================================
                    if (currentState >= 13) {{
                        rayGroup = new THREE.Group();
                        rayGroup.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), pUnitDir);
                        ballRootGroup.add(rayGroup);

                        const headLength = 0.26;
                        const initialShaftLength = R - headLength;

                        // Ray Shaft
                        const shaftGeo = new THREE.CylinderGeometry(0.032, 0.032, 1, 16);
                        const rayMat = new THREE.MeshStandardMaterial({{
                            color: 0x06b6d4,
                            emissive: 0x06b6d4,
                            emissiveIntensity: 2.0,
                            roughness: 0.25
                        }});
                        rayShaft = new THREE.Mesh(shaftGeo, rayMat);
                        rayShaft.scale.set(1, initialShaftLength, 1);
                        rayShaft.position.set(0, initialShaftLength / 2, 0);
                        rayGroup.add(rayShaft);

                        // Ray Arrowhead
                        const headGeo = new THREE.ConeGeometry(0.09, headLength, 16);
                        rayHead = new THREE.Mesh(headGeo, rayMat);
                        rayHead.position.set(0, initialShaftLength + (headLength / 2), 0);
                        rayGroup.add(rayHead);
                    }}

                    // ========================================================
                    // CLICK 7 (State >= 14): Dynamic Destination Point P'
                    // ========================================================
                    if (currentState >= 14) {{
                        const pPrimeGeo = new THREE.SphereGeometry(0.10, 32, 32);
                        const pPrimeMat = new THREE.MeshStandardMaterial({{
                            color: 0x10b981,
                            emissive: 0x10b981,
                            emissiveIntensity: 2.5
                        }});
                        pPrimeSphere = new THREE.Mesh(pPrimeGeo, pPrimeMat);
                        pPrimeSphere.position.copy(pLocalInitial);
                        ballRootGroup.add(pPrimeSphere);

                        pPrimeLabel = makeCleanTextSprite("P' (x', y', z')", "#dc2626");
                        pPrimeLabel.scale.set(1.9, 0.44, 1);
                        pPrimeLabel.position.copy(pLocalInitial).add(new THREE.Vector3(0.76, 0.32, 0.0));
                        ballRootGroup.add(pPrimeLabel);
                    }}
                }}

                // ============================================================
                // ANIMATION LOOP (Click 7: Majestic 2R Slow-Motion Inflation)
                // ============================================================
                let animStartTime = null;
                const animDuration = 9000; // 9.0s ultra-calm lecture pace
                const targetLambda = 2.0;  // Full 2R radial scaling factor

                function easeInOutCubic(t) {{
                    return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
                }}

                function animate(timestamp) {{
                    requestAnimationFrame(animate);

                    if (currentState >= 14 && expandableBallBody) {{
                        if (!animStartTime) animStartTime = timestamp;
                        const elapsed = timestamp - animStartTime;
                        const progress = Math.min(1.0, elapsed / animDuration);
                        const eased = easeInOutCubic(progress);

                        const currentLambda = 1.0 + (targetLambda - 1.0) * eased;

                        // 1. Expand Football Body
                        expandableBallBody.scale.set(currentLambda, currentLambda, currentLambda);

                        // 2. Expand Contact Shadow
                        if (shadowMesh) {{
                            shadowMesh.scale.set(currentLambda, currentLambda, currentLambda);
                        }}

                        // 3. Extend Ray OP & Arrowhead
                        if (rayShaft && rayHead) {{
                            const headLength = 0.26;
                            const newTotalDist = R * currentLambda;
                            const newShaftLength = newTotalDist - headLength;

                            rayShaft.scale.set(1, newShaftLength, 1);
                            rayShaft.position.set(0, newShaftLength / 2, 0);
                            rayHead.position.set(0, newShaftLength + (headLength / 2), 0);
                        }}

                        // 4. Move Destination Point P' & Label along ray
                        if (pPrimeSphere && pPrimeLabel) {{
                            const currentPPos = pLocalInitial.clone().multiplyScalar(currentLambda);
                            pPrimeSphere.position.copy(currentPPos);
                            pPrimeLabel.position.copy(currentPPos).add(new THREE.Vector3(0.76, 0.32, 0.0));
                        }}
                    }}

                    renderer.render(scene, camera);
                }}
                requestAnimationFrame(animate);

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
