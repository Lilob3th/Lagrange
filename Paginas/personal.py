import streamlit as st

st.html("<center><h1> Lilibeth Andrea Correa Ramírez </h1>")


with st.container(border=True):    

    st.markdown("""Lilibeth, es oriunda del municipio del Cerrito Santander. Tiene 19 años, hija de Edgar Correa y Miryam Ramírez, la segunda de tres hermanas. Anyi Jimena, su hermana mayor, es su inspiración y ejemplo a seguir; y Maria Isabel, su hermana menor, es el pilar fundamental de toda su familia.""")
    st.image("imagenes/familia.jpeg")

c1, c2=st.columns(2, gap="large")

with c1:
    with st.container(border=True):      
        st.markdown("""Los números se han convertido en su pasatiempo favorito, es estudiante de Licenciatura en Matemáticas en la Universidad Industrial de Santander; considera que este a sido uno de sus mas grandes retos, pero ama lo que hace y en el lugar que esta.""", unsafe_allow_html=True)
        st.image("imagenes/profe.jpeg")

with c2:
    with st.container(border=True):      
        st.markdown("""Aparte de los números, es apasionada por la apicultura, un arte que desde pequeña su padre le ha enseñado y ella a aprendido a amar. Ve con amor el trabajar con las abejas y conocer un poco mas de ellas.""")
        st.image("imagenes/avejas.jpeg")


st.markdown("Su mayor inspiración es lograr culminar su carrera, para quizás volver a su pueblo y ejercer su profesión en la Escuela Normal Superior \"Sady Tóbon Calle\", lugar donde realizo sus estudios desde preescolar hasta undecimo, y del cual se siente orgullosa.")
st.image("imagenes/normal.jpeg")
