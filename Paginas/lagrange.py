import streamlit as st

st.html("<center><h1> Joseph Louis Lagrange </h1>")

c1, c2=st.columns(2, vertical_alignment="center", gap="large")

with c1:  
    st.markdown("""<p style="text-align: justify;"> <b> Joseph-Louis Lagrange</b> (1736-1813) fue un matemático y físico nacido en Turín, considerado uno de los más influyentes del siglo XVIII. Desarrolló el cálculo de variaciones y reformuló la mecánica clásica en su obra <b>Mécanique Analytique</b>, sentando las bases de la mecánica lagrangiana. También destacó en teoría de números, álgebra y optimización, introduciendo los multiplicadores de Lagrange. Fue director de la Academia de Berlín y participó en la reforma del sistema métrico en Francia. Su legado perdura en conceptos fundamentales de las matemáticas y la física moderna. </p>""", unsafe_allow_html=True)

with c2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/%D0%9B%D0%B0%D0%B3%D1%80%D0%B0%D0%BD%D0%B6.jpg/220px-%D0%9B%D0%B0%D0%B3%D1%80%D0%B0%D0%BD%D0%B6.jpg")