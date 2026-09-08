# Clip 01 - Eigenvalues and Eigenvectors
# Slides 1-3 Complete Implementation (Aligned Click 5 Wedge Cut)

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
# STATES 8+ - SLIDE 3 (VISUALIZATION)
# ============================================================

elif 8 <= st.session_state.presentation_state <= 18:
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
                /* LAYER 1: Permanent 2D Pitch Background */
                #pitch2d {{
                    position: absolute;
                    inset: 0;
                    width: 100%;
                    height: 100%;
                    z-index: 1;
                    display: block;
                }}
                /* LAYER 2: Transparent 3D Foreground */
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

                    // Turf Stripes
                    const stripes = 10;
                    const sh = 1536 / stripes;
                    for (let i = 0; i < stripes; i++) {{
                        ctx.fillStyle = (i % 2 === 0) ? '#28792c' : '#308e36';
                        ctx.fillRect(0, i * sh, 2048, sh);
                    }}

                    // Outer Boundary & Lines
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

                // Lights
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

                // Helper: Soft Contact Shadow
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

                // Helper: Compact TV-Grade Math Pill Badge
                function makeMathTextSprite(text, dotColor) {{
                    const canvas = document.createElement('canvas');
                    canvas.width = 640;
                    canvas.height = 200;
                    const ctx = canvas.getContext('2d');

                    const x = 30, y = 25, w = 580, h = 150, r = 75;

                    // 1. Crisp White Pill Badge
                    ctx.fillStyle = 'rgba(255, 255, 255, 0.98)';
                    ctx.beginPath();
                    ctx.moveTo(x + r, y);
                    ctx.lineTo(x + w - r, y);
                    ctx.arc(x + w - r, y + r, r, -Math.PI / 2, Math.PI / 2);
                    ctx.lineTo(x + r, y + h);
                    ctx.arc(x + r, y + r, r, Math.PI / 2, -Math.PI / 2);
                    ctx.closePath();
                    ctx.fill();

                    // 2. Slate Border
                    ctx.strokeStyle = '#64748b';
                    ctx.lineWidth = 6;
                    ctx.stroke();

                    // 3. Vibrant Indicator Dot
                    ctx.fillStyle = dotColor || '#2563eb';
                    ctx.beginPath();
                    ctx.arc(x + 65, y + r, 24, 0, Math.PI * 2);
                    ctx.fill();

                    // 4. Bold Typography
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

                const ballRadius = 1.35;
                const oPos = new THREE.Vector3(0, ballRadius, 0);
                const R = ballRadius;
                let ballGroup = null;

                // ============================================================
                // CLICK 3, 4, 5: Corrected Screen-Space Geometry
                // ============================================================
                if (currentState >= 10) {{
                    // 1. Soft Contact Shadow on Pitch
                    const shadowGeo = new THREE.PlaneGeometry(R * 2.2, R * 2.2);
                    const shadowMat = new THREE.MeshBasicMaterial({{
                        map: createContactShadowTexture(),
                        transparent: true,
                        depthWrite: false
                    }});
                    const shadowMesh = new THREE.Mesh(shadowGeo, shadowMat);
                    shadowMesh.rotation.x = -Math.PI / 2;
                    shadowMesh.position.set(0, 0.02, 0);
                    scene.add(shadowMesh);

                    // 2. Ball Root Group
                    ballGroup = new THREE.Group();
                    ballGroup.position.copy(oPos);
                    ballGroup.lookAt(camera.position);
                    scene.add(ballGroup);

                    // Wedge Cut Math (Click 5 / State >= 12)
                    const isWedgeCut = currentState >= 12;
                    const wedgeSpan = isWedgeCut ? (50 * Math.PI / 180) : 0;
                    const sphereArc = Math.PI * 2 - wedgeSpan;
                    const pAngle = 38 * (Math.PI / 180); // Point P is at +38 deg
                    const sphereStart = pAngle + (wedgeSpan / 2);

                    // 3. White Ball Base
                    const ballGeo = new THREE.SphereGeometry(
                        R, 
                        64, 
                        64, 
                        sphereStart, 
                        sphereArc
                    );
                    const ballMat = new THREE.MeshStandardMaterial({{
                        color: 0xf8fafc,
                        roughness: 0.18,
                        metalness: 0.10,
                        side: THREE.DoubleSide
                    }});
                    const whiteBall = new THREE.Mesh(ballGeo, ballMat);
                    // Align sphere equator with the camera view plane
                    whiteBall.rotation.x = Math.PI / 2;
                    ballGroup.add(whiteBall);

                    // 4. Click 5: Dark Charcoal Matte Interior Cut-Walls & Bored Core
                    if (isWedgeCut) {{
                        const wallMat = new THREE.MeshStandardMaterial({{
                            color: 0x1e293b,
                            roughness: 0.6,
                            metalness: 0.1,
                            side: THREE.DoubleSide
                        }});

                        // Two planar cut-face walls
                        const wallGeo = new THREE.CircleGeometry(R, 64, 0, Math.PI);

                        const wall1 = new THREE.Mesh(wallGeo, wallMat);
                        wall1.rotation.z = pAngle - (wedgeSpan / 2);
                        wall1.rotation.y = Math.PI / 2;
                        ballGroup.add(wall1);

                        const wall2 = new THREE.Mesh(wallGeo, wallMat);
                        wall2.rotation.z = pAngle + (wedgeSpan / 2);
                        wall2.rotation.y = Math.PI / 2;
                        ballGroup.add(wall2);

                        // Bored Center Recessed Cylinder (Negative Space Stage)
                        const coreRadius = 0.15;
                        const coreHeight = R * 1.8;
                        const coreGeo = new THREE.CylinderGeometry(coreRadius, coreRadius, coreHeight, 32, 1, true);
                        const coreMesh = new THREE.Mesh(coreGeo, wallMat);
                        coreMesh.rotation.x = Math.PI / 2;
                        ballGroup.add(coreMesh);

                        // 5. Origin O(0, 0, 0) Reveal in Center Stage
                        const oGeo = new THREE.SphereGeometry(0.09, 32, 32);
                        const oMat = new THREE.MeshStandardMaterial({{
                            color: 0xf59e0b, // Amber Gold
                            emissive: 0xf59e0b,
                            emissiveIntensity: 2.2
                        }});
                        const oSphere = new THREE.Mesh(oGeo, oMat);
                        oSphere.position.set(0, 0, 0);
                        ballGroup.add(oSphere);

                        const oLabel = makeMathTextSprite("O (0, 0, 0)", "#f59e0b");
                        oLabel.scale.set(1.4, 0.44, 1);
                        oLabel.position.set(-0.75, -0.25, 0.2);
                        ballGroup.add(oLabel);
                    }}

                    // 6. Pentagons and Seams
                    const decoGroup = new THREE.Group();
                    decoGroup.rotation.set(0.35, -0.65, 0.2);
                    ballGroup.add(decoGroup);

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

                    const pentagonRadius = 0.39;
                    icoVerts.forEach(v => {{
                        const pentGeo = new THREE.CircleGeometry(pentagonRadius, 5);
                        const pentMesh = new THREE.Mesh(pentGeo, pentagonMat);
                        pentMesh.position.copy(v.clone().multiplyScalar(R * 1.002));
                        pentMesh.lookAt(v.clone().multiplyScalar(R * 2));
                        decoGroup.add(pentMesh);
                    }});

                    for (let i = 0; i < icoVerts.length; i++) {{
                        for (let j = i + 1; j < icoVerts.length; j++) {{
                            if (icoVerts[i].distanceTo(icoVerts[j]) < 1.1) {{
                                const p1 = icoVerts[i].clone().multiplyScalar(R * 1.001);
                                const p2 = icoVerts[j].clone().multiplyScalar(R * 1.001);
                                const lineGeo = new THREE.BufferGeometry().setFromPoints([p1, p2]);
                                const seam = new THREE.Line(lineGeo, lineMat);
                                decoGroup.add(seam);
                            }}
                        }}
                    }}
                }}

                // ============================================================
                // CLICK 4 (State >= 11): Surface Points C' and P(x, y, z)
                // ============================================================
                if (currentState >= 11 && ballGroup) {{
                    const cTopGeo = new THREE.SphereGeometry(0.09, 32, 32);
                    const cTopMat = new THREE.MeshStandardMaterial({{
                        color: 0xe11d48,
                        emissive: 0xe11d48,
                        emissiveIntensity: 2.0
                    }});
                    const cTopSphere = new THREE.Mesh(cTopGeo, cTopMat);
                    cTopSphere.position.set(0, 0, R);
                    ballGroup.add(cTopSphere);

                    const pAngle = 38 * (Math.PI / 180);
                    const pLocal = new THREE.Vector3(
                        R * Math.cos(pAngle),
                        R * Math.sin(pAngle),
                        0.15 * R
                    );

                    const pGeo = new THREE.SphereGeometry(0.10, 32, 32);
                    const pMat = new THREE.MeshStandardMaterial({{
                        color: 0x06b6d4,
                        emissive: 0x06b6d4,
                        emissiveIntensity: 2.5
                    }});
                    const pSphere = new THREE.Mesh(pGeo, pMat);
                    pSphere.position.copy(pLocal);
                    ballGroup.add(pSphere);

                    const cLabel = makeMathTextSprite("C'(0, R, 0)", "#e11d48");
                    cLabel.scale.set(1.4, 0.44, 1);
                    cLabel.position.set(-0.55, 0.32, R);
                    ballGroup.add(cLabel);

                    const pLabel = makeMathTextSprite("P (x, y, z)", "#06b6d4");
                    pLabel.scale.set(1.4, 0.44, 1);
                    pLabel.position.copy(pLocal).add(new THREE.Vector3(0.72, 0.32, 0.0));
                    ballGroup.add(pLabel);
                }}
                // Render Loop
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
