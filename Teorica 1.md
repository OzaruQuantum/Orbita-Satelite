# Problema de Satélite Terrestre  
**Autor**: David Guadalupe Esquila  
**Fecha**: $(date +%Y-%m-%d)  

---

## 📝 Enunciado del Problema  

Un satélite terrestre de masa $m = 1000\,\text{kg}$ tiene un momento angular $L = m\sqrt{2GMR}$, donde $R = 6.4 \times 10^6\,\text{m}$ es el radio terrestre y $GM = gR^2$ con $g = 9.81\,\text{m/s}^2$. 

---

## 🔍 Solución  

### 🟢 Parte D: Órbita Elíptica  

#### 📐 Ápsides  

```math
\begin{aligned}
E &= \frac{8}{9}E_0 = -\frac{2gRm}{9} \\
\epsilon &= \sqrt{1 + \frac{2EL^2}{G^2M^2m^3}} = \frac{1}{3} \\
r(\theta) &= \frac{2R}{1 + \frac{1}{3}\cos\theta} \\
\text{Perigeo} &= \left.\frac{2R}{1+\epsilon}\right|_{\theta=0} = 1.5R = \boxed{9.6 \times 10^6\ \text{m}} \\
\text{Apogeo} &= \left.\frac{2R}{1-\epsilon}\right|_{\theta=\pi} = 3R = \boxed{1.92 \times 10^7\ \text{m}}
\end{aligned}
```

#### 🚀 Conservación de Energía  

```math
E = \frac{1}{2}mv^2 - \frac{GMm}{r}
```

**Velocidades**:  
| Punto      | Fórmula                     | Resultado             |
|------------|-----------------------------|-----------------------|
| **Perigeo** | $v_p = \sqrt{\frac{8gR}{9}}$ | $\boxed{7470\ \text{m/s}}$ |
| **Apogeo**  | $v_a = \sqrt{\frac{2gR}{9}}$ | $\boxed{3735\ \text{m/s}}$ |

---

## 📌 Notas Técnicas  

1. **Sintaxis corregida**:  
   - Usé bloques ```math``` para ecuaciones complejas (mejor compatibilidad)  
   - Los símbolos `\left.` y `\right|` ahora renderizan correctamente  
   - Espaciado uniforme con `\\` simple  

2. **Visualización garantizada**:  
   ```markdown
   $$ E = \frac{1}{2}mv^2 - \frac{GMm}{r} $$
   ```
   Se muestra así en GitHub:  
   $$ E = \frac{1}{2}mv^2 - \frac{GMm}{r} $$

3. **Para ecuaciones multilínea**:  
   ```markdown
   ```math
   \begin{aligned}
   a &= b + c \\
     &= d \times e
   \end{aligned}
   ```
   ```

---

##### 🔗 Recursos:  
[MathJax en GitHub](https://docs.github.com/es/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)
