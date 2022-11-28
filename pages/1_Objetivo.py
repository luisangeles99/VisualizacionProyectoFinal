import streamlit as st

introText = 'La empresa La Roche Posay ha recolectado los datos del último año que ofrece Facebook \n\
            para obtener información de las campañas que mayor éxito han tenido en la plataforma. \n \
            El objetivo es encontrar puntos clave que permitan medir el impacto de las camapañas en \n \
            el alcance de los posts.'

problemText = 'Parte de los posts siguen campañas que son de paga, es vital conocer si esta inversión es justificable \
             y cuales son los tipos de posts que más influyen en atraer nuevos usuarios, en la interacción de los usuarios actuales y \
                y las más efectivas para que los clientes hagan click en el post.'

publicText = 'Este documento está dirigido al equipo de MARKETING del cliente.'

questionsText = 'Los puntos clave se encuentran en la página de análisis de esta aplicación. Los siguientes son los puntos claves que este estudio busca responder: '

questions = [
    'Campañas con mayor impacto a lo largo del año',
    'La relación entre el tipo de post y su alcance al pagar en Facebook',
    'Campañas que más atraen a usuarios nuevos',
    'Campañas que generan interacciones entre los usuarios',
    'Evolución en el tiempo de las interacciones',
    'Conclusiones claves'
]

st.sidebar.info('Menú de navegación')

a, b = st.columns([2, 10])

with a:
    st.text("")
    st.image("logo.jpeg")
with b:
    st.title("Objetivo de estudio")

st.subheader('Resumen')
st.write(introText)
st.write(problemText)

st.subheader('Público objetivo del estudio')
st.write(publicText)

st.subheader('Preguntas clave')
st.write(questionsText)

for q in questions:
    st.markdown('- ' + q)

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:40px;
}
</style>
''', unsafe_allow_html=True)
