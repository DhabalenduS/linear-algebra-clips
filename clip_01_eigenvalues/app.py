#1st commit for the clip_01_eigenvalues dated 30th August at 2:20 pm  
import numpy as np
import plotly.graph_objects as go
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="The Essence of Eigenvalues - Slide 3", layout="wide"
)

st.title("Slide 3: Visualization of Soccer Match & Eigenvectors")
st.write(
    "Interactive simulation demonstrating the scaling of a football and eigenvectors."
)

# Sidebar controls for interactive switch cases
st.sidebar.header("Simulation Control Panel")
action = st.sidebar.selectbox(
    "Select Simulation State:",
    [
        "None",
        "ground",
        "ball",
        "P",
        "pumping",
    ],
)

# Lambda scaling factor for pumping
lambda_factor = st.sidebar.slider(
    "Scaling Factor ($\lambda$)", 1.0, 1.5, 1.3, 0.05
)

# Create 3D figure using Plotly
fig = go.Figure()

# 1. Base / Ground logic ("ground" case)
if action in ["ground", "ball", "P", "pumping"]:
  # Create a green ground plane (X-Y plane)
  xx, yy = np.meshgrid(np.linspace(-3, 3, 10), np.linspace(-3, 3, 10))
  zz = np.zeros_like(xx)
  fig.add_trace(
      go.Surface(
          x=xx,
          y=yy,
          z=zz,
          colorscale=[[0, "#2ecc71"], [1, "#27ae60"]],
          showscale=False,
          name="Football Ground",
      )
  )

# 2. Football logic ("ball", "P", "pumping" cases)
# Current radius scales based on action state
current_radius = 1.0
if action == "pumping":
  current_radius = lambda_factor

if action in ["ball", "P", "pumping"]:
  # Generate sphere for football
  phi = np.linspace(0, np.pi, 20)
  theta = np.linspace(0, 2 * np.pi, 20)
  phi, theta = np.meshgrid(phi, theta)

  fx = current_radius * np.sin(phi) * np.cos(theta)
  fy = current_radius * np.sin(phi) * np.sin(theta)
  fz = current_radius * np.cos(phi)

  fig.add_trace(
      go.Surface(
          x=fx,
          y=fy,
          z=fz,
          colorscale=[[0, "white"], [1, "black"]],
          showscale=False,
          opacity=0.9,
          name="Football",
      )
  )

# 3. Point P and vector OP in the First Octant ("P" and "pumping" cases)
if action in ["P", "pumping"]:
  # Define a point P in the first octant on the unit sphere surface
  # Angles chosen so x>0, y>0, z>0
  p_theta = np.pi / 4  # 45 degrees
  p_phi = np.pi / 4  # 45 degrees

  # Initial point P on radius 1.0
  px_init = np.sin(p_phi) * np.cos(p_theta)
  py_init = np.sin(p_phi) * np.sin(p_theta)
  pz_init = np.cos(p_phi)

  # Final point P' scaled by current_radius
  px_final = px_init * current_radius
  py_final = py_init * current_radius
  pz_final = pz_init * current_radius

  # Draw vector OP or OP'
  fig.add_trace(
      go.Scatter3d(
          x=[0, px_final],
          y=[0, py_final],
          z=[0, pz_final],
          mode="lines+markers+text",
          line=dict(color="red", width=6),
          marker=dict(size=[4, 8], color=["blue", "red"]),
          text=["O (Origin)", f"P' ({px_final:.2f}, {py_final:.2f}, {pz_final:.2f})"],
          textposition="top right",
          name="Vector OP'",
      )
  )

# Layout and camera settings for 3D plot
fig.update_layout(
    scene=dict(
        xaxis_title="X Axis",
        yaxis_title="Y Axis",
        zaxis_title="Z Axis",
        xaxis=dict(range=[-3, 3]),
        yaxis=dict(range=[-3, 3]),
        zaxis=dict(range=[-1, 3]),
        aspectratio=dict(x=1, y=1, z=0.8),
    ),
    margin=dict(l=0, r=0, b=0, t=0),
    height=600,
)

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Display descriptive observations/conclusions based on state
col1, col2 = st.columns(2)

with col1:
  st.subheader("Observations")
  if action == "None":
    st.info("Select a state from the sidebar to begin the simulation.")
  elif action == "ground":
    st.write(
        "- A beautiful and green football ground is displayed on the field."
    )
  elif action == "ball":
    st.write("- A football (black and white combination) is placed at the center.")
  elif action == "P":
    st.write(
        "- Point P(x,y,z) is located in the **first octant** on the surface of"
        " the football."
    )
    st.write("- Directed line segment OP connects the origin O to P.")
  elif action == "pumping":
    st.write(
        f"- Air is pumped; point P moves along direction OP and reaches P'."
    )
    st.write(f"- Point P is scaled by a factor of $\\lambda = {current_radius:.2f}$.")

with col2:
  st.subheader("Conclusion")
  if action == "pumping":
    st.success(
        "The non-zero point P does not change its direction while moving towards"
        " P', and is therefore defined as an eigenvector corresponding to the"
        f" eigenvalue $\\lambda = {current_radius:.2f}$."
    )
    st.info(
        "All other points on the surface maintain their direction and scale by"
        " $\\lambda$."
    )
  else:
    st.write(
        "- Complete the pumping step to observe the eigenvector property."
    )
