import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parámetros
R = 6.4e6  # Radio terrestre (m)
g = 9.81   # Aceleración gravitacional (m/s²)
m = 1000   # Masa del satélite (kg)

# Configuración de colores
EARTH_COLOR = '#1fa3ec'
CIRCULAR_COLOR = 'red'
ELLIPTICAL_COLOR = 'blue'
SAT_COLOR = 'black'

# Órbita circular
theta = np.linspace(0, 2*np.pi, 100)
r_circular = 2 * R * np.ones_like(theta)

# Órbita elíptica
epsilon = 1/3
r_elliptical = 2 * R / (1 + epsilon * np.cos(theta))

# Gráfico estático con la Tierra
plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)

# Dibujar la Tierra
earth = Circle((0, 0), 1, transform=ax.transData._b, color=EARTH_COLOR, alpha=0.7)
ax.add_patch(earth)

# Dibujar órbitas
ax.plot(theta, r_circular/R, color=CIRCULAR_COLOR, linestyle='-', label='Órbita circular')
ax.plot(theta, r_elliptical/R, color=ELLIPTICAL_COLOR, linestyle='-', label='Órbita elíptica')

# Configuración del gráfico
ax.set_rmax(4)
ax.set_title("Órbitas del satélite (en radios terrestres)", pad=20)
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('orbitas.png', dpi=150)
plt.close()

# Animación con la Tierra
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(10, 10))

# Dibujar la Tierra (fondo)
earth_anim = Circle((0, 0), 1, transform=ax.transData._b, color=EARTH_COLOR, alpha=0.7)
ax.add_patch(earth_anim)

# Inicializar elementos de la animación
line_circ, = ax.plot([], [], color=CIRCULAR_COLOR, linestyle='-', label='Circular')
line_ell, = ax.plot([], [], color=ELLIPTICAL_COLOR, linestyle='-', label='Elíptica')
point, = ax.plot([], [], 'o', color=SAT_COLOR, markersize=8, label='Satélite')

# Configuración del gráfico animado
ax.set_rmax(4)
ax.set_title("Animación de órbitas satelitales", pad=20)
ax.legend(loc='upper right')

def init():
    line_circ.set_data([], [])
    line_ell.set_data([], [])
    point.set_data([], [])
    return line_circ, line_ell, point

def update(frame):
    t = np.linspace(0, 2*np.pi, 100)
    r_circ = 2 * np.ones_like(t)
    r_ell = 2 / (1 + epsilon * np.cos(t - frame/10))
    
    line_circ.set_data(t, r_circ)
    line_ell.set_data(t, r_ell)
    point.set_data([t[frame]], [r_ell[frame]])
    return line_circ, line_ell, point

# Crear animación
ani = FuncAnimation(fig, update, frames=60, init_func=init, 
                    blit=True, interval=100)

# Guardar como GIF
ani.save('orbit_animation.gif', writer='pillow', fps=10, dpi=100)

# Guardar frames individuales para LaTeX
for i in range(60):
    update(i)
    plt.savefig(f'orbit_animation/frame-{i:02d}.png', dpi=150)
plt.close()

print("Visualizaciones generadas exitosamente!")