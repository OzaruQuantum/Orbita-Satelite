import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pathlib import Path

def ensure_dir_exists(path):
    """Crea la carpeta si no existe (soporta subdirectorios)."""
    Path(path).mkdir(exist_ok=True, parents=True)

def setup_repository():
    """Inicializa la estructura del repositorio con carpetas y archivos esenciales."""
    folders = ['scripts', 'images', 'data', 'docs']
    for folder in folders:
        ensure_dir_exists(folder)
    
    # Crear archivo requirements.txt
    with open('requirements.txt', 'w', encoding='utf-8') as f:
        f.write("""numpy==1.21.5
matplotlib==3.5.1
scipy==1.8.0
jupyterlab==3.4.0
pillow==9.0.0""")  # pillow agregado explícitamente
    
    # Crear archivo .gitignore
    with open('.gitignore', 'w', encoding='utf-8') as f:
        f.write("""__pycache__/
*.tmp
*.swp
.DS_Store
*.ipynb_checkpoints
""")

def calculate_orbit_parameters():
    """
    Calcula los parámetros principales de la órbita de un satélite alrededor de la Tierra.
    Retorna un diccionario con constantes y valores calculados.
    """
    G = 6.67430e-11  # Constante gravitacional
    M = 5.972e24     # Masa de la Tierra (kg)
    R = 6.4e6        # Radio de la Tierra (m)
    m = 1000         # Masa del satélite (kg)
    
    L = m * np.sqrt(2 * G * M * R)
    E0 = - (G * M * m) / (4 * R)
    E = (8/9) * E0
    epsilon = np.sqrt(1 + (2 * E * L**2) / (G**2 * M**2 * m**3))
    
    # Definir funciones de posición y velocidad
    def r_elliptic(theta):
        return 2 * R / (1 + epsilon * np.cos(theta))
    def velocity(r):
        return np.sqrt(2 * (E + G * M * m / r) / m)
    
    return {
        'constants': {'G': G, 'M': M, 'R': R, 'm': m},
        'calculated': {
            'angular_momentum': L,
            'circular_energy': E0,
            'elliptic_energy': E,
            'eccentricity': epsilon,
            'perigee': r_elliptic(0),
            'apogee': r_elliptic(np.pi),
            'velocity_func': velocity
        }
    }

def generate_plots(params):
    """
    Genera y guarda una visualización comparando la órbita circular y elíptica.
    """
    ensure_dir_exists("images")
    plt.style.use('seaborn-darkgrid')
    
    theta = np.linspace(0, 2*np.pi, 300)
    R = params['constants']['R']
    epsilon = params['calculated']['eccentricity']
    r_circular = 2 * R * np.ones_like(theta)
    r_elliptic = 2 * R / (1 + epsilon * np.cos(theta))
    
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, polar=True)
    ax.plot(theta, r_circular/1e6, 'r-', label='Órbita Circular (2R)')
    ax.plot(theta, r_elliptic/1e6, 'b--', label=f'Órbita Elíptica (ε={epsilon:.2f})')
    ax.set_title("Comparación de Órbitas\n(Radio en millones de metros)", pad=20)
    ax.legend(loc='upper right')
    plt.savefig('images/orbit_comparison.png', dpi=150, bbox_inches='tight')
    plt.close()

def generate_animation(params):
    """
    Crea y guarda una animación del movimiento orbital del satélite.
    """
    ensure_dir_exists("images")
    epsilon = params['calculated']['eccentricity']

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Tierra
    earth = plt.Circle((0, 0), 0.2, color='#1fa3ec', alpha=0.7)
    ax.add_patch(earth)
    
    satellite, = ax.plot([], [], 'ko', markersize=8)
    trail, = ax.plot([], [], 'k:', alpha=0.4, linewidth=1)
    
    def init():
        satellite.set_data([], [])
        trail.set_data([], [])
        return satellite, trail
    
    def update(frame):
        theta = frame * 0.05
        r = 2 / (1 + epsilon * np.cos(theta))
        x, y = r * np.cos(theta), r * np.sin(theta)
        
        old_x, old_y = trail.get_data()
        new_x = np.append(old_x[-50:], x)
        new_y = np.append(old_y[-50:], y)
        
        satellite.set_data(x, y)
        trail.set_data(new_x, new_y)
        return satellite, trail
    
    ani = FuncAnimation(fig, update, frames=200, init_func=init, blit=True)
    ani.save('images/orbit_animation.gif', writer='pillow', fps=15, dpi=120)
    plt.close()

def generate_readme(params):
    """
    Genera un README.md completo con parámetros, resultados y visualizaciones.
    """
    content = f"""\
# 🛰️ Satellite Orbital Dynamics Simulation

## 📊 Parámetros del Sistema
| Parámetro        | Valor                     |
|------------------|--------------------------|
| Radio de la Tierra | {params['constants']['R']/1e6:.1f} × 10⁶ m |
| Masa del Satélite  | {params['constants']['m']} kg      |
| Momento Angular    | {params['calculated']['angular_momentum']:.2e} kg·m²/s |
| Energía Circular   | {params['calculated']['circular_energy']:.2e} J |
| Excentricidad      | {params['calculated']['eccentricity']:.3f}     |

## 🎯 Resultados Clave
| Métrica      | Valor                     |
|--------------|---------------------------|
| Perigeo      | {params['calculated']['perigee']/1e6:.2f} × 10⁶ m |
| Apogeo       | {params['calculated']['apogee']/1e6:.2f} × 10⁶ m  |
| Velocidad en Perigeo | {params['calculated']['velocity_func'](params['calculated']['perigee'])/1e3:.2f} km/s |
| Velocidad en Apogeo  | {params['calculated']['velocity_func'](params['calculated']['apogee'])/1e3:.2f} km/s |

## 📈 Visualizaciones
![Comparación de Órbitas](images/orbit_comparison.png)
![Animación Orbital](images/orbit_animation.gif)

## 🚀 Uso
```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar simulación
python satellite_repo_automator.py
