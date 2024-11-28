import streamlit as st
from sympy import *

st.title("Exploremos")


x,y = symbols('x y')
l = symbols("l")

# leyendo f y g
f = parse_expr(st.text_input("Digite la función: ", value="x**2 + 2*y**2 - 5"))

st.latex( latex(f) )

#g = parse_expr(input("Digite la restricción: "))
g = parse_expr(st.text_input("Digite la restricción: ", value="x**2 + y**2 - 1"))

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
st.header("PUNTOS MÁXIMOS Y MÍNIMOS")
c1, c2=st.columns(2, vertical_alignment="center")

for i in range(len(vals)):
    punto = sols[i]
    px, py = punto[x], punto[y]

    
    if vals[i] == maximos:
        with c1:
            st.markdown(f"**El punto ({px}, {py}) es un máximo.**")
        
    elif vals[i] == minimos:
        with c2:
            st.markdown(f"**El punto ({px}, {py}) es un mínimo.**")
