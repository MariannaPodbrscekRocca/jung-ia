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
* ⚓ **Sistema de Anclaje DOM Dinámico:** Implementación de un mecanismo avanzado en HTML5/JavaScript que garantiza el retorno automático al tope de la página (`#top-circus-anchor`) en cada cambio de sección o navegación del usuario.

---

## 🏛️ Constitución de la Prueba e Interfaz Web

La interfaz web está construida bajo una arquitectura modular y reactiva en Streamlit. A continuación, se muestra cómo interactúan los elementos visuales y lógicos dentro de la plataforma:

<p align="center">
  <img src="https://raw.githubusercontent.com/MariannaPodbrscekRocca/jung-ia/main/Constitucion_web.png" width="90%" alt="Constitución Web">
</p>

1. **Encabezado Dinámico y Tarjetas de Identificación:** Muestran en tiempo real el nombre del postulante y el personaje de ficción seleccionado.
2. **Sistema de Pestañas y Secciones Obligatorias:** Para avanzar de sección, el postulante debe interactuar con las opciones de lectura y consulta de IA. Los botones muestran **`✅`** al ser explorados o **`💔`** si están pendientes.
3. **Caja de Preguntas Libres a la IA:** Espacio integrado con autocompletado por la tecla `TAB` para plantear inquietudes directamente al agente sabio y compasivo al estilo del Ánima/Ánimus.

---

## 🎥 Demostraciones de Flujo (Video Demos)

### 1. Pantalla de Bienvenida, Idioma y Colores Vibrantes
* **Descripción:** Se muestra la interfaz inicial bajo la carpa del circo digital con el banner de bienvenida de Jung.AI. Los botones cuentan con colores vibrantes y efectos de realce visual al pasar el cursor (*hover effects*). Se incluye también el selector de idioma para cambiar dinámicamente entre español e inglés.

https://github.com/MariannaPodbrscekRocca/jung-ia/raw/main/Video_demos/botones_colores_vibrantes.mp4
https://github.com/MariannaPodbrscekRocca/jung-ia/raw/main/Video_demos/English_Spanish_Menu%20(1).mp4

---

### 2. Registro de Datos del Candidato
* **Descripción:** Formulario interactivo de validación de credenciales. Aquí el usuario ingresa sus datos personales. Las demostraciones muestran la captura de nombres, apellidos opcionales y género, así como la configuración del número de teléfono y del correo electrónico con selector inteligente de dominios.

https://github.com/MariannaPodbrscekRocca/jung-ia/raw/main/Video_demos/nombre_apellido_opcional_sexo.mp4
https://github.com/MariannaPodbrscekRocca/jung-ia/raw/main/Video_demos/telefono_mail.mp4

---

### 3. Selección de Producción Audiovisual, Personaje y Botones de Retorno ("Oops")
* **Descripción:** Selección de series y películas (*Harry Potter*, *Breaking Bad*, etc.) con un banco dinámico de 16 arquetipos de personalidad. Se aprecian en acción los botones de retroceso o redirección "Oops" para corregir datos o registrarse ante producciones no disponibles.

https://github.com/MariannaPodbrscekRocca/jung-ia/raw/main/Video_demos/botones_de_regreso.mp4
https://github.com/MariannaPodbrscekRocca/jung-ia/raw/main/Video_demos/oops_no_me_identifico.mp4

---

### 4. Evaluación de Funciones Cognitivas, Loops, Arquetipos y Controles Interactivos
* **Descripción:** El núcleo de la prueba interactiva. Se detalla el uso de las opciones 1, 2 y 3, cómo la Opción 1 extrae información directamente de la matriz en Excel (`matriz_personalidades.csv`), y cómo las secciones combinan respuestas anteriores de forma controlada y fluida. Asimismo, se evidencia la diferencia visual entre los checks verdes y los corazones rotos con titileo que exigen completar la exploración antes de avanzar.

https://github.com/MariannaPodbrscekRocca/jung-ia/raw/main/Video_demos/opciones_1_2_y_3.mp4
https://github.com/MariannaPodbrscekRocca/jung-ia/raw/main/Video_demos/opcion_1.mp4
https://github.com/MariannaPodbrscekRocca/jung-ia/raw/main/Video_demos/check_vs_corazones.mp4
https://github.com/MariannaPodbrscekRocca/jung-ia/raw/main/Video_demos/Ingles_en_cualquier_momento.mp4

---

### 5. Resultado Final, Verificación de Datos y Envío Automatizado por Correo
* **Descripción:** Revelación del área tecnológica recomendada, verificación final de los datos del postulante, selección de horario para la entrevista de Fase 2, opción de resetear ante desacuerdo con el perfil, y el proceso de envío SMTP del reporte multilingüe.

* **Banner y Vistas de Éxito del Envío:**
<p align="center">
  <img src="https://raw.githubusercontent.com/MariannaPodbrscekRocca/jung-ia/main/banner.png" width="90%" alt="Banner Éxito Correo">
</p>

https://github.com/MariannaPodbrscekRocca/jung-ia/raw/main/Video_demos/explicacion_final.mp4
https://github.com/MariannaPodbrscekRocca/jung-ia/raw/main/Video_demos/email.mp4
https://github.com/MariannaPodbrscekRocca/jung-ia/raw/main/Video_demos/no_conforme_resultado.png

---

## 🛠️ Explicación Técnica y Tecnologías Utilizadas

* **Python & Streamlit:** Base de la aplicación web reactiva y gestión robusta de estados de sesión (`st.session_state`).
* **OpenAI API (`gpt-4o-mini`):** Motor de inteligencia artificial encargado de generar respuestas reflexivas, equilibrando la luz y la sombra de los perfiles junguianos en un solo párrafo fluido y compasivo.
* **Pandas:** Procesamiento y lectura de la matriz psicométrica estructurada en `matriz_personalidades.csv`.
* **SMTP & EmailMime:** Automatización del backend para la distribución multilingüe de correos electrónicos con plantillas HTML personalizadas.
* **HTML5 / CSS3 / JavaScript:** Estilos personalizados oscuros con temática de circo digital, animaciones fluidas, efectos *hover* en botones y un sistema de anclaje DOM dinámico que garantiza el retorno automático al tope de la página en cada cambio de sección.
