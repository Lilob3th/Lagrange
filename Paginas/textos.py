import streamlit as st

st.title("Multiplicadores de Lagrange")



st.header("¿Que son los **multiplicadores de Lagrange**?")


#textos
st.markdown("""
Los multiplicadores de Lagrange son una técnica matemática utilizada en cálculo para resolver problemas de **optimización con restricciones**. Su objetivo es encontrar los puntos máximos y mínimos de una función $f(x,y,...)$ sujeta a una o más restricciones dadas por ecuaciones como $g(x,y,...)$.

""")

with st.container(border=True):
    st.header(":violet[Concepto clave]")
    st.markdown("""
La idea central es que en los puntos óptimos, el gradiente de la funcion objetivo $(\u2207 f)$ es paralelo al gradiente de las restricciones $(\u2207 g)$, es decir, existe un escalar (multiplicador de Lagrange, $(\u03BB)$ tal que:

""")

#ecuaciones 
    st.latex("\u2207 f = \u03BB*\u2207 g")

st.header("Joseph Louis Lagrange")
c1, c2=st.columns(2, vertical_alignment="center")

with c1:  
    st.markdown("*Joseph-Louis Lagrange* (1736-1813) fue un matemático y físico nacido en Turín, considerado uno de los más influyentes del siglo XVIII. Desarrolló el cálculo de variaciones y reformuló la mecánica clásica en su obra **Mécanique Analytique**, sentando las bases de la mecánica lagrangiana. También destacó en teoría de números, álgebra y optimización, introduciendo los multiplicadores de Lagrange. Fue director de la Academia de Berlín y participó en la reforma del sistema métrico en Francia. Su legado perdura en conceptos fundamentales de las matemáticas y la física moderna.")


with c2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/%D0%9B%D0%B0%D0%B3%D1%80%D0%B0%D0%BD%D0%B6.jpg/220px-%D0%9B%D0%B0%D0%B3%D1%80%D0%B0%D0%BD%D0%B6.jpg")

st.header(":violet[Conceptos importantes]")

with st.container(border=True):    

    st.subheader("Gradiente:")
    st.markdown(r""" 
Es un vector que apunta en la direccion de mayor tasa de cambio de una función. Matemáticamente, para una función $f(x,y,...)$, su gradiante es: 
$\nabla f=[df/dx,df/dy,...]&
""")

with st.container(border=True):    

    st.subheader("Máximos:")
    st.markdown(""" 
Hace referencia a un punto en el dominio de la función objetivo donde la función alcanza su valor más alto bajo una restricción.
""")

with st.container(border=True):    

    st.subheader("Mínimos:")
    st.markdown(""" 
Hace referencia a un punto donde la función objetivo alcanza su valor más bajo, bajo una restricción.
""")

with st.container(border=True):    

    st.subheader("Multiplicador de Lagrange:")
    st.markdown(""" 
Es un escalar que aparece en la ecuación que relaciona los gradienres de la funcion objetivo $f(x,y,...)$ y la restricción $g(x,y,...)$. Este multiplicador juega un papel clave en la optimización de funciones sujetas a restricciones y simbolicamente se representa con la letra: \u03BB.
""")