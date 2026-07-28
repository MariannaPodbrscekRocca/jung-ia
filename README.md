# 🎪 JUNG.AI: THE CIRCUS OF PERSONALITIES 🎪

> **Link para testear la aplicación (evidencias del despliegue):** [https://jungai.streamlit.app/](https://jungai.streamlit.app/)

> **Sistema Inteligente de Reclutamiento y Diagnóstico Psicométrico según el modelo de Carl Jung**  
> *Diseñado por Marianna Podbrscek Rocca* 

---

## 🌟 Descripción General del Proyecto

**Jung.AI: The Circus of Personalities** es un sistema inteligente, interactivo y bilingüe de reclutamiento y diagnóstico psicométrico impulsado por inteligencia artificial 🤖✨. Ambientado bajo la mágica y vibrante atmósfera de un circo digital 🎪🔮, el sistema transforma el proceso clásico de contratación de la empresa ficticia **Jung Tech Company** en una experiencia totalmente inmersiva y fuera de este mundo. 

La aplicación guía a los postulantes a través de una entrevista de trabajo virtual donde seleccionan una producción audiovisual de culto, se identifican con personajes icónicos 🎭, y exploran paso a paso sus funciones cognitivas (dominante, auxiliar, terciaria, inferior), loops cognitivos y arquetipos digitales de Carl Jung. Todo esto culmina en un análisis de compatibilidad con áreas de tecnología y el agendamiento automatizado de una entrevista de Fase 2 con envío de reportes vía correo electrónico 📩✨.

---

## ✨ Características y Funciones Innovadoras Principales

* 🧠 **Diagnóstico Psicométrico Dinámico por IA:** Evaluación automatizada de la tipología de Carl Jung y arquetipos cruzados con la personalidad del candidato, combinando un archivo Excel estructural (`matriz_personalidades.csv`) con generación en tiempo real mediante OpenAI GPT-4o-mini.
* 🤖 **Funcionamiento Inteligente por Secciones y Caja de Texto IA:**
  * **Sección 1:** El agente de IA responde integrando la descripción estática obtenida del archivo `matriz_personalidades.csv` y la cruza dinámicamente con la esencia del personaje elegido.
  * **Secciones 2 y 3:** El sistema utiliza los datos de la matriz junto con el contexto del perfil del postulante para generar análisis profundos sobre luz y sombra profesional.
  * **Caja de Texto Interactiva Personalizada:** Cada sección cuenta con una caja de texto con opción de autocompletado inteligente mediante la tecla `TAB` (utilizando preguntas sugeridas contextuales por fase), permitiendo al usuario plantear cualquier duda libre al agente inteligente y recibir respuestas únicas adaptadas al instante.
* 🌐 **Soporte Bilingüe Nativo en Tiempo Real:** Selector de idioma interactivo en la barra lateral disponible en cualquier momento de la prueba para alternar de forma fluida entre **Español** e **Inglés**.
* 🎨 **Diseño Visual Dinámico y Hover Effects:** Botones estilizados con colores fucsias y dorados vibrantes inspirados en la estética de un circo digital. El botón de **"Siguiente Sección" (Next Section)** destaca de manera prominente, y cuenta con efectos visuales *hover* interactivos al pasar el cursor por encima para mejorar la experiencia de usuario.
* 🔄 **Navegabilidad Interactiva Inteligente:** 
  * Sistema de validación de exploración mediante iconos de **Check Verde (`✅`)** en contraposición a los **Corazones Rotos (`💔`)**, indicando visualmente qué apartados obligatorios debe abrir el postulante para desbloquear el avance.
  * Botones de retroceso y opción de reinicio mediante un amigable botón de *"Oops"* para corregir datos o cambiar de producción en cualquier etapa.
* 📧 **Generación y Envío Automatizado de Reportes SMTP:** Sistema de agendamiento de fecha y hora tentativa para la Fase 2 con envío multilingüe de cartas de resultado y temario de entrevista.

---

## 🏛️ Constitución de la Prueba e Interfaz Web

La interfaz web está construida bajo una arquitectura modular y reactiva en Streamlit. A continuación, se muestra cómo interactúan los elementos visuales y lógicos dentro de la plataforma:

<p align="center">
  <img src="./Constitucion_web.png" width="90%" alt="Constitución Web">
</p>

1. **Encabezado Dinámico y Tarjetas de Identificación:** Muestran en tiempo real el nombre del postulante y el personaje de ficción seleccionado.
2. **Sistema de Pestañas y Secciones Obligatorias:** Para avanzar de sección, el postulante debe interactuar con las opciones de lectura y consulta de IA. Los botones muestran **`✅`** al ser explorados o **`💔`** si están pendientes.
3. **Caja de Preguntas Libres a la IA:** Espacio integrado con autocompletado por la tecla `TAB` para plantear inquietudes directamente al agente sabio y compasivo al estilo del Ánima/Ánimus.

---

## 🎥 Demostraciones en Video

### 1. Pantalla de Bienvenida y Selección de Idioma
* **Descripción:** Se muestra la interfaz inicial bajo la carpa del circo digital con el banner de bienvenida de Jung.AI. En la esquina superior izquierda se aprecia el selector de idioma (Español / English) que permite cambiar el idioma en cualquier momento de la prueba. Al hacer clic en el botón principal con efectos hover, se ingresa al sistema.

<p align="center">
  <video width="100%" autoplay loop muted playsinline>
    <source src="./Video_demos/00.mp4" type="video/mp4">
    Tu navegador no soporta la reproducción de video.
  </video>
</p>

---

### 2. Registro de Datos del Candidato
* **Descripción:** Formulario interactivo donde el usuario ingresa sus datos personales (nombres, apellidos, nombre preferido, género, prefijo telefónico internacional y correo electrónico con selector de dominio inteligente). El sistema valida en tiempo real los campos requeridos y muestra avisos de éxito o corrección en colores vibrantes.

<p align="center">
  <video width="100%" autoplay loop muted playsinline>
    <source src="./Video_demos/000.mp4" type="video/mp4">
    Tu navegador no soporta la reproducción de video.
  </video>
</p>

---

### 3. Selección de Producción Audiovisual y Personaje
* **Descripción:** El postulante elige entre cuatro producciones de culto (*Harry Potter*, *Arrested Development*, *South Park*, *Breaking Bad*). Posteriormente, selecciona de un banco dinámico de 16 personalidades al personaje con el que más se identifica. Incluye botones de retroceso ("Oops") en caso de querer corregir la selección o registrarse para futuras convocatorias.

<p align="center">
  <video width="100%" autoplay loop muted playsinline>
    <source src="./Video_demos/0000.mp4" type="video/mp4">
    Tu navegador no soporta la reproducción de video.
  </video>
</p>

---

### 4. Evaluación de Funciones Cognitivas, Loops y Arquetipos
* **Descripción:** El núcleo de la prueba interactiva. Se despliegan las fases cognitivas del modelo de Carl Jung. El usuario debe explorar las secciones de lectura obligatoria (controladas por los indicadores de check verde y corazones rotos). Cada sección integra tanto la información estática extraída del archivo CSV matriz como respuestas generadas dinámicamente por la IA evaluando la luz y la sombra del arquetipo.

<p align="center">
  <video width="100%" autoplay loop muted playsinline>
    <source src="./Video_demos/00000.mp4" type="video/mp4">
    Tu navegador no soporta la reproducción de video.
  </video>
</p>

---

### 5. Resultado Final, Verificación de Datos y Envío de Correo (Fase 2)
* **Descripción:** Tras completar las fases, el sistema revela el área de tecnología recomendada (*Product Management*, *Desarrollo de Software*, etc.). El postulante revisa sus datos de contacto, selecciona el idioma de su preferencia para el reporte y elige una fecha y hora tentativa para su entrevista de Fase 2. Al confirmar, el sistema se conecta mediante SMTP para enviar con éxito el reporte detallado al correo del candidato.

* **Banner de Éxito del Envío:**
<p align="center">
  <img src="./banner.png" width="90%" alt="Banner Éxito Correo">
</p>

* **Video Demostrativo:**
<p align="center">
  <video width="100%" autoplay loop muted playsinline>
    <source src="./Video_demos/email.mp4" type="video/mp4">
    Tu navegador no soporta la reproducción de video.
  </video>
</p>

---

## 🛠️ Explicación Técnica y Tecnologías Utilizadas

* **Python & Streamlit:** Base de la aplicación web reactiva y gestión de estados de sesión (`st.session_state`).
* **OpenAI API (`gpt-4o-mini`):** Motor de inteligencia artificial encargado de generar respuestas reflexivas, equilibrando la luz y la sombra de los perfiles junguianos en un solo párrafo fluido y compasivo.
* **Pandas:** Procesamiento y lectura de la matriz psicométrica estructurada en `matriz_personalidades.csv`.
* **SMTP & EmailMime:** Automatización del backend para la distribución multilingüe de correos electrónicos con plantillas HTML personalizadas.
* **HTML5 / CSS3 / JavaScript:** Estilos personalizados oscuros con temática de circo digital, animaciones fluidas, efectos *hover* en botones y un sistema de anclaje DOM dinámico que garantiza el retorno automático al tope de la página (`#top-circus-anchor`) en cada cambio de sección.
