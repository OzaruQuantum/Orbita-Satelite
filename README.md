# 🛰️ Problema del Satélite Terrestre

Análisis dinámico de un satélite en órbita terrestre con cambio de energía específica. Incluye:
- Modelado matemático completo
- Soluciones analíticas verificadas
- Visualizaciones interactivas
- Animaciones profesionales

## 📚 Contenido
1. [Problema Físico](#-problema-físico)
2. [Modelo Matemático](#-modelo-matemático)
3. [Resultados Clave](#-resultados-clave)
4. [Visualizaciones](#-visualizaciones)
5. [Cómo Usar](#-cómo-usar)
6. [Dependencias](#-dependencias)

## 🌍 Problema Físico
Estudio de un satélite de masa:
- `m = 1000 kg`
- Momento angular inicial: `L = m√(2GMR)`
- Radio terrestre: `R = 6.4×10⁶ m`

Se analiza:
1. Órbita circular inicial
2. Transición a órbita elíptica con `E = (8/9)E₀`
3. Cálculo de ápsides y velocidades extremas

## 📐 Modelo Matemático
### Ecuaciones Fundamentales
```math
\begin{aligned}
L &= m\sqrt{2GMR} \\
E_0 &= -\frac{GMm}{4R} \\
\epsilon &= \sqrt{1 + \frac{2EL^2}{G^2M^2m^3}}
\end{aligned}


