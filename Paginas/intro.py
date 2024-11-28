import streamlit as st

st.title("Multiplicadores de Lagrange")

st.header("¿Que son los **multiplicadores de Lagrange**?")


#textos
st.markdown("""
Los multiplicadores de Lagrange son una técnica matemática utilizada en cálculo para resolver problemas de **optimización con restricciones**. Su objetivo es encontrar los puntos máximos y mínimos de una función $f(x,y,...)$ sujeta a una o más restricciones dadas por ecuaciones como $g(x,y,...)$.

""")

with st.container(border=True):
    st.header("Concepto clave")
    st.markdown("""
La idea central es que en los puntos óptimos, el gradiente de la funcion objetivo $(\u2207 f)$ es paralelo al gradiente de las restricciones $(\u2207 g)$, es decir, existe un escalar (multiplicador de Lagrange, $(\u03BB)$ tal que:

""")

#ecuaciones 
    st.latex("\u2207 f = \u03BB*\u2207 g")
