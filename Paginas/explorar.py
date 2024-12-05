import streamlit as st
from sympy import *

st.html("<center><h1> Exploremos </h1>")
st.html("<center><h2> ¡Es momento de que practiques! </h2>")

st.markdown("Recuerda lo siguiente al momento de escribir tanto la función como la restricción: ")

st.image("https://media.licdn.com/dms/image/v2/D4E12AQHnCUmXofwf1w/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1686628143167?e=1737590400&v=beta&t=QWZAz-EkbjtFtuOa3m9zF0YqFimwVjkjfV95b4Sua3M")

x,y = symbols('x y')
l = symbols("l")

# leyendo f y g
f = parse_expr(st.text_input("Digite la función: ", value="x**2 + 2*y**2 - 5"))

st.latex( latex(f) )

#g = parse_expr(input("Digite la restricción: "))
g = parse_expr(st.text_input("Digite la restricción: ", value="x**2 + y**2 - 1"))

st.latex( latex(g) )

st.markdown("Ahora, vemos cuales son los puntos máximos y mínimos de la funcion y la restriccion que escogiste:")

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
st.html("<center><h2> Puntos máximos y mínimos </h1>")
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
