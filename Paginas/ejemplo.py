import streamlit as st

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

st.title("Veamos un ejemplo:")

st.markdown("Supongamos que queremos hallar los puntos máximos y mínimos de lafunción $f(x,y)=x^2+2y^2-5$")

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.linspace(-10, 10, 100)
Y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(X, Y)
Z = X**2+2*Y**2-5

ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

st.subheader("Grafica de la función $f(x,y)=x^2+2y^2-5$")
st.pyplot(fig)

st.markdown("Pero tambien, queremos limitar las valores de la entrada $(x,y)$ de tal manera que satisfagan la siguiente ecuación $x^2+y^2=1$" )

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x1 = [0, 1, 3, 4, 5, 7]
y1 = [2, 3, 3, 1, 2, 5]

st.subheader("Gráfica del círculo $x^2 + y^2 = 1$")
theta = np.linspace(0, 2 * np.pi, 500)  # Ángulos desde 0 a 2π
x3 = np.cos(theta)  # Coordenadas x
y3 = np.sin(theta)  # Coordenadas y

fig3, ax3 = plt.subplots()
ax3.plot(x3, y3, label="$x^2 + y^2 = 1$")
ax3.axhline(0, color='gray', linestyle='--', linewidth=0.5)
ax3.axvline(0, color='gray', linestyle='--', linewidth=0.5)
ax3.set_aspect('equal')  # Mantener proporciones
ax3.set_title("Círculo unitario")
ax3.grid()
ax3.legend()
st.pyplot(fig3)

st.markdown("Teniendo en cuenta las graficas anteriores, procedemos a hallar los puntos máximos y mínimos de la función sujeta a la restricción dada.")

st.markdown("Entonces:")

import streamlit as st
from sympy import *

x,y = symbols('x y')
l = symbols("l")

# leyendo f y g
f = x**2 + 2*y**2 - 5
st.markdown("La función es:")

st.latex( latex(f) )

#g = parse_expr(input("Digite la restricción: "))
g = x**2 + y**2 - 1
st.markdown("La restricción es:")

st.latex( latex(g) )

# halla las derivadas
fx = diff(f, x)
fy = diff(f,y)
gx = diff(g,x)
gy = diff(g,y)

# define las ecuaciones
eqx = fx - l*gx
eqy = fy - l*gy

# resolviendo las ecuaciones
sols = solve([eqx, eqy, g], [x, y, l], dict=True)

# evaluando en los puntos
vals = []
for punto in sols:
    px, py = punto[x], punto[y]
    val = f.subs(x, px).subs(y, py)
    vals.append(val)

# encontrando maximos y minimos
maximos = max(vals)
minimos = min(vals)

# mostrando la solución
st.markdown("Los puntos máximos y mínimos son:")
c1, c2=st.columns(2, vertical_alignment="center")

for i in range(len(vals)):
    punto = sols[i]
    px, py = punto[x], punto[y]

    if vals[i] == maximos:
        with c1:
            st.markdown(f"*El punto ({px}, {py}) es un máximo.*")
        
    elif vals[i] == minimos:
        with c2:
            st.markdown(f"*El punto ({px}, {py}) es un mínimo.*")

st.markdown("Ahora, veamoslo graficamente:")

def f(x, y):
    return x**2 + 2 * y**2 - 5

critical_points = [
    ((0, -1), f(0, -1)),  # Máximo
    ((0, 1), f(0, 1)),    # Máximo
    ((-1, 0), f(-1, 0)),  # Mínimo
    ((1, 0), f(1, 0))     # Mínimo
]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Crear una rejilla para graficar la superficie de la función
X = np.linspace(-1.5, 1.5, 100)
Y = np.linspace(-1.5, 1.5, 100)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)

ax.plot_surface(X, Y, Z, alpha=0.6, cmap='viridis', edgecolor='none')

theta = np.linspace(0, 2 * np.pi, 500)
x_circle = np.cos(theta)
y_circle = np.sin(theta)
z_circle = f(x_circle, y_circle)
ax.plot(x_circle, y_circle, z_circle, color='red', label='Restricción $x^2 + y^2 = 1$')

for (point, value) in critical_points:
    color = 'orange' if value > -5 else 'blue'  # Diferenciar máximos y mínimos
    label = f"Punto crítico ({point[0]:.2f}, {point[1]:.2f}, {value:.2f})"
    ax.scatter(point[0], point[1], value, color=color, s=100, label=label)


st.pyplot(fig)
