import io
import os
import time
import qrcode
import streamlit as st

# 1. Configuración automática del tema azul marino
os.makedirs(".streamlit", exist_ok=True)
config_path = os.path.join(".streamlit", "config.toml")
if not os.path.exists(config_path):
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(
            '[theme]\n'
            'primaryColor = "#38bdf8"\n'
            'backgroundColor = "#0a192f"\n'
            'secondaryBackgroundColor = "#112240"\n'
            'textColor = "#e6f1ff"\n'
            'font = "sans serif"\n'
        )

# 2. Configuración responsive de la página
st.set_page_config(
    page_title="Programación y Robótica",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Encabezado principal (80% Informativo)
st.title("🚀 Portafolio de Aprendizaje: Programación y Robótica")
st.subheader("Resumen de proyectos, conceptos y prototipos desarrollados en clase")
st.divider()

# Datos de los proyectos
proyectos = [
    {
        "materia": "Programación",
        "titulo": "💻 Códigos y Términos de Programación",
        "desc": "Aprendimos la lógica detrás del software: variables, condicionales, bucles y funciones para dar instrucciones precisas a la computadora."
    },
    {
        "materia": "Programación",
        "titulo": "🌐 Creación de Páginas Web",
        "desc": "Dominamos la estructura, el diseño visual y la lógica de programación para construir sitios dinámicos e interactivos desde cero."
    },
    {
        "materia": "Programación",
        "titulo": "✨ Hovers Creativos",
        "desc": "Desarrollamos efectos visuales que reaccionan cuando el usuario pasa el cursor por encima de un elemento, aplicando transiciones, sombras y escalas."
    },
    {
        "materia": "Programación",
        "titulo": "🔴 Pelota Rebotando en Dos Computadoras",
        "desc": "Programamos la física básica de colisiones para que un objeto rebote al tocar los bordes de la pantalla, sincronizando el movimiento entre dos monitores."
    },
    {
        "materia": "Programación",
        "titulo": "🚗 Programación de Carrito",
        "desc": "Implementamos la lógica de movimiento, control de dirección y velocidad para desplazar un vehículo digital mediante comandos."
         "imagen": "foto2.jpg"
    },
    {
        "materia": "Robótica",
        "titulo": "🥊 Robots de Pelea (Mini Sumo)",
        "desc": "Diseñamos y programamos robots autónomos capaces de detectar a su oponente mediante sensores y empujarlo fuera del área de combate."
    },
    {
        "materia": "Robótica",
        "titulo": "🦾 Brazo Robótico en 3D",
        "desc": "Ensamblamos y controlamos un brazo articulado impreso en 3D, utilizando servomotores para lograr movimientos precisos de rotación y agarre.",
        "imagen": "foto.jpg"
    },
    {
        "materia": "Robótica",
        "titulo": "🖨️ Manejo de Impresora 3D",
        "desc": "Aprendimos el flujo de fabricación aditiva: preparación de modelos digitales (slicing), calibración de la cama caliente, uso de filamentos y supervisión."
    }
]

# Filtro interactivo por materia
opcion = st.radio(
    "Filtrar proyectos por área:",
    ["Todos", "Programación", "Robótica"],
    horizontal=True
)

st.write("")

# Mostrar tarjetas informativas en columnas (responsive)
filtrados = proyectos if opcion == "Todos" else [p for p in proyectos if p["materia"] == opcion]
columnas = st.columns(2)

for indice, item in enumerate(filtrados):
    with columnas[indice % 2]:
        with st.container(border=True):
            st.caption(f"ÁREA: {item['materia'].upper()}")
            st.markdown(f"### {item['titulo']}")
            st.write(item["desc"])
            if "imagen" in item:
                st.image(item["imagen"], caption="Prototipo del Brazo Robótico en 3D", use_container_width=True)

st.divider()

# Sección Interactiva (20% - Simulador en vivo de rebote)
st.header("🎮 Demo Interactiva: Simulador de Rebote en Bordes")
st.write("Ajusta la velocidad y presiona el botón para simular el rebote que programamos en clase:")

velocidad = st.slider("Velocidad de la pelota:", min_value=1, max_value=10, value=5)

if st.button("▶️ Iniciar Simulación de Rebote"):
    pista = st.empty()
    posicion = 0
    direccion = 1
    ancho_pista = 20

    for _ in range(45):
        espacios_izq = "⬜" * posicion
        espacios_der = "⬜" * (ancho_pista - posicion)
        pista.markdown(f"### |{espacios_izq}🔴{espacios_der}|")
        
        posicion += direccion
        if posicion >= ancho_pista or posicion <= 0:
            direccion *= -1
            
        time.sleep(0.15 / (velocidad * 0.4))
    st.success("¡Simulación completada!")

st.divider()

# 3. Generador de Código QR Responsive para abrir la página en cualquier celular
st.header("📱 Acceso Rápido desde Celular (Código QR)")
st.write("Escanea este código QR para abrir el portafolio en pantalla responsive desde tu dispositivo móvil:")

col_qr_info, col_qr_img = st.columns([2, 1])

with col_qr_info:
    url_actual = st.context.url if hasattr(st.context, "url") and st.context.url else ""
    url_destino = st.text_input(
        "Enlace público de la página web:",
        value=url_actual,
        placeholder="Pega aquí tu enlace de .streamlit.app"
    )
    st.caption("Al abrirse desde la nube, el enlace público se carga aquí automáticamente y genera el QR al instante.")

with col_qr_img:
    if url_destino:
        qr = qrcode.QRCode(version=1, box_size=8, border=2)
        qr.add_data(url_destino)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color="#0a192f", back_color="#e6f1ff")
        
        buffer = io.BytesIO()
        img_qr.save(buffer, format="PNG")
        st.image(buffer.getvalue(), caption="Escanea para ver en móvil", use_container_width=True)
