import streamlit as st
import openai

# Configuración de la página
st.set_page_config(page_title="Creador de Guiones Pro", page_icon="🎬", layout="centered")

st.title("🎬 Generador de Guiones Automático para TikTok")
st.write("Escribe tu idea en bruto y la IA se encargará de estructurar un guion optimizado para el Programa de Recompensas (Más de 60 segundos).")

# Entradas del usuario
idea_bruta = st.text_area("¿De qué quieres hablar hoy? (Cuéntalo a tu manera):", 
                          placeholder="Ej: Dejé mi pega por un proyecto familiar, me cambié de ciudad, quedé pato, caí en depresión y perdí a mi familia...")

nicho_tematica = st.text_input("Nicho o Temática del canal:", 
                               placeholder="Ej: Humor de resiliencia y comedia de desahogo real al estilo chileno")

# Botón de ejecución
if st.button("Generar Guion Completo"):
    if idea_bruta and nicho_tematica:
        with st.spinner("Estructurando tu guion al hueso..."):
            
            # Construcción automática del súper prompt con los criterios de viralidad y retención
            prompt_final = f"""
            Actúa como un experto en viralidad y monetización de TikTok. Crea un guion de video basado exactamente en esta idea:
            '{idea_bruta}'
            
            Para el siguiente nicho/temática:
            '{nicho_tematica}'
            
            El guion DEBE cumplir estrictamente con los requisitos del Programa de Recompensas para Creadores de TikTok:
            1. DURACIÓN: Debe tener suficiente texto para durar MÁS DE 60 SEGUNDOS (mínimo 150-180 palabras narradas a ritmo normal). Evita modismos que no sean chilenos como 'laburo', 'limpio' (para decir sin dinero); usa términos correctos y naturales como 'pega', 'pobre' o 'pato'.
            2. LOS PRIMEROS 3 SEGUNDOS: Empieza directamente con un GANCHO IMPACTANTE. Sin saludos, sin introducciones. Una frase que detenga el scroll de inmediato.
            3. FILTRO DE LOS 5 SEGUNDOS: Entre el segundo 3 y el 5, genera una promesa o intriga masiva para retener al usuario.
            4. CUERPO (0:05 al 0:55): Entrega el valor del relato dividido en 3 puntos claros o pasos. Mantén el ritmo rápido, directo y al hueso.
            5. CIERRE (0:55 al 1:05): Haz un llamado a la acción sutil y orgánico, enfocado en generar cercanía y construir una comunidad de apoyo mutuo donde los usuarios se sientan invitados a desahogarse y apoyarse entre todos en los comentarios.
            
            Escribe el guion dividiéndolo explícitamente por secciones con sus marcas de tiempo (0:00 - 0:03, 0:03 - 0:05, etc.) e incluye instrucciones claras entre paréntesis de qué mostrar en pantalla o b-roll.
            """
            
            # Caja de texto final para que el usuario copie el prompt directo a ChatGPT/Gemini
            st.success("¡Instrucción optimizada generada con éxito!")
            st.write("### Copia el siguiente texto y pégalo en tu IA de confianza:")
            st.text_area("Instrucción para copiar:", prompt_final, height=450)
            
    else:
        st.warning("Por favor, completa ambos campos para poder armar la estructura.")
