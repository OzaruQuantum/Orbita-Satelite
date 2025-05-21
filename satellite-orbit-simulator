"""
Satellite Orbit Simulation
Author: David Guadalupe Esquila
Date: $(today)

This script calculates and visualizes circular and elliptical orbits for an Earth satellite
based on given physical parameters. It generates both static plots and animations.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Constants
R_earth = 6.4e6  # Earth radius [m]
M = 1000  # Satellite mass [kg]
G = 6.67430e-11  # Gravitational constant
g = 9.81  # Earth gravity [m/s²]
GM = g * R_earth**2  # Standard gravitational parameter

# Problem parameters
L = M * np.sqrt(2 * GM * R_earth)  # Angular momentum

# Part C: Circular orbit
r0 = 2 * R_earth  # Circular orbit radius
E0 = -GM * M / (2 * r0)  # Circular orbit energy

# Part D: Elliptical orbit (E = 8/9 E0)
E = (8/9) * E0
epsilon = np.sqrt(1 + (2 * E * L**2) / (GM**2 * M**3))  # Eccentricity

def radius(theta, a=2*R_earth, e=epsilon):
    """Calculate orbital radius at angle theta"""
    return a / (1 + e * np.cos(theta))

# Calculate orbit points
theta = np.linspace(0, 2*np.pi, 500)
r_circular = np.ones_like(theta) * r0
r_elliptical = radius(theta)

# Convert to Cartesian coordinates
def polar_to_cartesian(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

x_circ, y_circ = polar_to_cartesian(r_circular, theta)
x_ell, y_ell = polar_to_cartesian(r_elliptical, theta)

# Calculate velocities
v_perigee = np.sqrt(8 * g * R_earth / 9)  # At r = 1.5R
v_apogee = np.sqrt(2 * g * R_earth / 9)  # At r = 3R

# Create static plot
plt.figure(figsize=(10, 10))
ax = plt.subplot(111, aspect='equal')

# Plot Earth
earth = Circle((0, 0), R_earth, color='#1fa3ec', alpha=0.7)
ax.add_patch(earth)

# Plot orbits
ax.plot(x_circ/R_earth, y_circ/R_earth, 'r-', label='Circular orbit')
ax.plot(x_ell/R_earth, y_ell/R_earth, 'b-', label='Elliptical orbit')

# Mark special points
ax.plot([0], [2], 'ro', label='Circular')  # Circular orbit marker
ax.plot([0], [1.5], 'bo', label='Perigee')  # Perigee marker
ax.plot([0], [-3], 'bo', label='Apogee')  # Apogee marker

# Formatting
ax.set_xlabel('x (Earth radii)')
ax.set_ylabel('y (Earth radii)')
ax.set_title('Satellite Orbits Around Earth')
ax.grid(True)
ax.legend()
plt.savefig('orbitas.png')
plt.close()

# Create animation
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.grid(True)
ax.set_title('Satellite Orbital Motion')
ax.set_xlabel('x (Earth radii)')
ax.set_ylabel('y (Earth radii)')

# Earth in animation
earth_anim = Circle((0, 0), 1, color='#1fa3ec', alpha=0.7)
ax.add_patch(earth_anim)

# Orbit paths
circ_line, = ax.plot([], [], 'r-', alpha=0.5, label='Circular')
ell_line, = ax.plot([], [], 'b-', alpha=0.5, label='Elliptical')

# Satellite markers
circ_sat, = ax.plot([], [], 'ro', markersize=8, label='Circular sat')
ell_sat, = ax.plot([], [], 'bo', markersize=8, label='Elliptical sat')

def init():
    circ_line.set_data([], [])
    ell_line.set_data([], [])
    circ_sat.set_data([], [])
    ell_sat.set_data([], [])
    return circ_line, ell_line, circ_sat, ell_sat

def update(frame):
    # Update orbit paths
    circ_line.set_data(x_circ[:frame]/R_earth, y_circ[:frame]/R_earth)
    ell_line.set_data(x_ell[:frame]/R_earth, y_ell[:frame]/R_earth)
    
    # Update satellite positions
    circ_sat.set_data(x_circ[frame]/R_earth, y_circ[frame]/R_earth)
    ell_sat.set_data(x_ell[frame]/R_earth, y_ell[frame]/R_earth)
    
    return circ_line, ell_line, circ_sat, ell_sat

# Create animation
ani = FuncAnimation(fig, update, frames=len(theta),
                    init_func=init, blit=True, interval=20)

# Save animation
ani.save('orbit_animation.gif', writer='pillow', fps=30, dpi=100)
plt.close()

print("Calculations complete!")
print(f"Circular orbit radius: {r0/R_earth:.1f} Earth radii")
print(f"Perigee: {1.5:.1f} Earth radii, Apogee: {3:.1f} Earth radii")
print(f"Perigee velocity: {v_perigee:.0f} m/s, Apogee velocity: {v_apogee:.0f} m/s")
