import streamlit as st
from PIL import Image

st.set_page_config(page_title = 'Tutorial para Ailén',
                    layout='wide')

st.markdown("<h1 style='text-align: center;'>Tutorial para Ailén<br><br></h1>", unsafe_allow_html=True)

apertura1 = Image.open('apertura1.jpeg')
apertura2 = Image.open('apertura2.jpeg')
machete1 = Image.open('machete1.jpeg')
stats = Image.open('stats.jpeg')

c1, c2, c3 = st.columns([0.1,0.8,0.1])

with c2:
    st.subheader("Pasos a seguir")
    with st.expander("Apertura de Sistema"):
        st.write(" <br> 1) Ir al logo de windows abajo a la derecha. Clickear en adición. El usuario es SUPERVISOR. No tiene contraseña <br> 2) Elegir si es turno mediodía o noche y darle aceptar.", unsafe_allow_html=True)
        st.image(apertura1)
        st.image(apertura2)
    with st.expander("Apertura de Caja"):
        st.write("1) Agarrar caja azul. Poner billetes en la caja registradora <br> 2) Ver en el papelito de la caja azul cuanta plata hay en la caja. Cargar ese importe como entrada en el sistema.<br> 3) Vas arriba a la derecha, clickeas en adición, clickeás en Caja y en la parte de Entradas clickeás Ajuste de Caja y pones el importe. De nombre ponele Caja Inicial. <br> 4) Hacerte listas con los gastos/sobres/sueldos que vas a pagar. Tambien ya el machete para anotar cubiertos, mesas, pedidos, promedios. Tambien para contar la plata en el cierre.", unsafe_allow_html=True)
        st.image(machete1)
        st.video('https://www.youtube.com/watch?v=agqEvA1oM9Q')
    with st.expander("Cierre de Caja"):
        st.write("<br> **ESTADISTICAS** <br> PONER HOJAS A4 EN LA IMPRESORA. Vas a Adicion, clickeas en estadisticas. Te anotas en el machete lo siguiente:<br> 1) Anotas cantidad de pedidos y cantidad de mesas que hubo. Esto lo sabes porque es lo que esta entre parentesis. Para cantidad de mesas sumas lo de Salon y lo de Afuera. <br> 2) **Promedio por mesa**: Sumas los importes de salon y afuera. Eso lo dividis por la cantidad de mesas que hubo. <br> 3) **Promedio por pedido**: Dividis el importe de pedidos por la cantidad de pedidos. <br> 4) **PROMEDIO GENERAL**: Sumas los tres importes (salon, mostrador, afuera) y lo dividis por la cantidad de mesas y pedidos sumados. <br><br>", unsafe_allow_html=True)
        st.write("<br> **CHEQUEAR IMPORTE TARJETAS Y MP CON ESTADISTICAS** <br> Haces el cierre de tarjetas en el PosNet. Sumas eso mas lo que tengas de MercadoPago. Ese numero tiene que coincidir con el que aparece en Tarjetas en Estadisticas. Si coincide: IMPRIMIS LA VENTANA DE SUBTOTALES Y LA DE VENTAS POR FORMA DE COBRO", unsafe_allow_html=True)
        st.image(stats)
        st.write("<br><br> **IMPRIMIR CONSUMOS:** <br> Si lo anterior te da bien, vas a la M, vas a Informes y vas a Articulos venta/ranking. Imprimis el turno actual. ", unsafe_allow_html=True)
        #st.video('https://www.youtube.com/watch?v=4E0DoDXGZZ0')
        st.write('<br> **CONTAR PLATA Y CHEQUEAR QUE DE BIEN:** <br> Contas la plata. Vas anotando cuanta plata hay de cada billete. Todos los fajos son de 10 billetes. Solo los de 500 son de 20 billetes. Cuando tenes el total de caja azul, lo anotas en el papelito. Despues a eso le sumas el total de tarjetas (tarjetas + MP). Esa suma te da un numero. Vas a Adicion, clickeas en Caja y ves el Saldo De Caja. Ese numero deberia coincidir o estar mas o menos cerca. Si esta cerca vas a Adicion y clickeas en fin de turno. Se cierra el programa. Vas al logo de windows, abris MaxiRest, vas a la M, vas a caja y vas a Consulta adicion caja. Imprimis eso en el turno y fecha correspondiente. Tiene que tener una columna eso nomas. Despues lo muestro en un video.', unsafe_allow_html=True)

    

    st.subheader("Preguntas frecuentes")
    with st.expander("Pasar gastos y sueldos. Ingresos/Egresos"):
        st.video('https://www.youtube.com/watch?v=agqEvA1oM9Q')
    with st.expander("Transferir mesa"):
        st.video('https://www.youtube.com/watch?v=bTZkVAuZi_M')
    with st.expander("Invitar cubiertos"):
        st.video('https://www.youtube.com/watch?v=fpf6fR42uic')
    with st.expander("Cambiar precio de un plato en el listado"):
        st.video('https://www.youtube.com/watch?v=JKrtPJpzAy4')
    with st.expander("Crear item/plato nuevo para una mesa"):
        st.video('https://www.youtube.com/watch?v=pKtBrKLjEcA')
    with st.expander("Cambiar nombre o precio de un plata en una mesa"):
        st.video('https://www.youtube.com/watch?v=H6aEPVdG4Bg')
    with st.expander("Anular mesa cobrada. Regenerar mesa cobrada"):
        st.write('Si quizas cobras mal una mesa. Tipo cobras la 9 cuando tenias que cobrar la 20. O si cobras la mesa con efectivo en vez de con credito o debito. Algun error asi. Si pasa algo asi podes buscar la mesa (si te acordas de cuanto fue el importe cobrado), anularla y ahi te da la opcion de regenerar la mesa y cobrarla de forma correcta.')
        st.video('https://www.youtube.com/watch?v=GIpoeCrBEjY')
    with st.expander("CLAVE: Imprimir consumos del cierre y gastos de la caja. Nota: esto es un ej. Los pasos estan mal. En cierre de caja se muestra bien en que orden imprimir estas cosas."):
        st.video('https://www.youtube.com/watch?v=4E0DoDXGZZ0')
    with st.expander("Imprimir pedidos de carne o verdura o planilla con stock de vinos"):
        st.video('https://www.youtube.com/watch?v=rEFca6B9wHg')
