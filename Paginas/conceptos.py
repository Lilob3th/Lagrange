import streamlit as st

st.html("<center><h1> Conceptos importantes </h1>")

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


