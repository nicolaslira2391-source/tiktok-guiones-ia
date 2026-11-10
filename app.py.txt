import streamlit as st

st.set_page_config(page_title="Creador de Guiones TikTok Monetizables", page_icon="📱")

st.title("📱 Generador de Guiones para TikTok")
st.subheader("Optimizado para el Programa de Recompensas de TikTok (>60 segundos)")

idea = st.text_area("¿De qué quieres que trate tu video?", placeholder="Ej: 3 trucos psicológicos para vender más en tu tienda online...")
nicho = st.text_input("¿Cuál es tu nicho o temática?", placeholder="Ej: Marketing, Cocina, Finanzas Personales...")

if st.button("Generar Estructura de Guion"):
    if idea:
        st.success("¡Estructura generada con éxito! Copia el texto de abajo y pégalo en ChatGPT:")
        
        prompt = f"""
Actúa como un experto en virilidad y monetización de TikTok. Crea un guion de video basado en esta idea: '{idea}' para el nicho '{nicho}'.
El guion DEBE cumplir estrictamente con los requisitos del Programa de Recompensas para Creadores de TikTok:

1. DURACIÓN: Debe tener suficiente texto para durar MÁS DE 60 SEGUNDOS (aproximadamente 150-180 palabras leídas a ritmo normal).
2. LOS PRIMEROS 3 SEGUNDOS: Empieza directamente con un GANCHO IMPACTANTE. Sin saludos, sin introducciones. Una frase que detenga el scroll.
3. FILTRO DE LOS 5 SEGUNDOS: Entre el segundo 3 y el 5, genera una promesa o intriga masiva para que el usuario no se vaya (requisito de retención de TikTok).
4. CUERPO (Minuto 0:05 al 0:55): Entrega el valor prometido dividido en 3 puntos claros o pasos. Mantén el ritmo rápido.
5. CIERRE (Minuto 0:55 al 1:05): Haz un llamado a la acción sutil para que guarden el video o comenten.

Escribe el guion dividiéndolo por secciones con sus marcas de tiempo (0:00 - 0:03, 0:03 - 0:05, etc.) e incluye instrucciones de qué mostrar en pantalla.
        """
        st.code(prompt, language="text")
    else:
        st.error("Por favor, escribe una idea primero.")
