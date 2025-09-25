[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7IRjtlNy)
# Presentación final del curso de Programación I

Este repositorio tiene como propósito servir de contenedor para los archivos de la presentación final del curso. Se deben guardar todos los archivos utilizados para la presentación (vea las condiciones de entrega más adelante). 

*Banco de Guatemala*  
*Maestría en Economía y Finanzas Aplicadas*  
*Programación I*  
*Fecha: Septiembre de 2025*

## Objetivos

El presente proyecto tiene como objetivo que el estudiante conozca nuevos paquetes del lenguaje de Python o que desarrolle lógica de programación necesaria para realizar alguna aplicación interesante utilizando programación científica o métodos de simulación de Monte Carlo. 


## Rúbrica de evaluación 

| Aspecto a evaluar                                                                             |  Punteo |
|:----------------------------------------------------------------------------------------------|--------:|
| Definición y delimitación del proyecto                                                        |      10 |
| El proyecto requiere conocimientos/esfuerzo adicional al ganado/realizado en el curso         |      10 |
| Participantes del grupo colaboraron cada uno con confirmaciones (*commits*) en el repositorio |      10 |
| Exposición clara, interacción con el público y manejo de los límites de tiempo (5-10 minutos) |      20 |
| El proyecto utiliza conceptos, paquetes, algoritmos o herramientas no vistas en clase         |      20 |
| Dominio del código y manejo de preguntas de los estudiantes o del profesor                    |      30 |
| **Total**                                                                                     | **100** |


## Formato de entrega 

- El proyecto debe entregarse utilizando la plataforma de GitHub, a través de las confirmaciones (*commits*) necesarios por los miembros de cada equipo. 
  - Tomar en cuenta que el repositorio será público. Evitar compartir datos personales, contraseñas u otra información sensible. Los repositorios pueden ser visitados nuevamente en el sitio de la organización `PES-BG-2025` para futuras consultas de parte de todos los estudiantes. 
- Los archivos finales del proyecto se pueden guardar en el directorio raíz del repositorio utilizando cualquier estructura deseada. Sin embargo, si se utilizan archivos de prueba que puedan servir como muestra del procedimiento realizado, pero que no formen parte del proyecto final, se deben guardar en un directorio especial denominado `deprecated`. 
- No cargar archivos al repositorio que sean demasiado grandes (>10MB) como fotografías o vídeos. Utilizar recursos o plataformas web específicamente diseñadas para estos propósitos. La única excepción a esta regla es para el archivo de presentación. 
- Un archivo de presentación es opcional. Si se utiliza una presentación en PowerPoint o PDF, esta debe ser adjuntada en la raíz del proyecto. 
- Al final de la presentación, se dará un tiempo para realizar preguntas, tanto del profesor o de los estudiantes.
- Atender a otras indicaciones adicionales por parte del instructor al inicio y durante la presentación. 
- La fecha de entrega máxima para realizar las confirmaciones será el **jueves 25 de septiembre de 2025 a las 23:59 horas**.

- ## Uso de inteligencia artificial

- En cada presentación, los profesores medirán un índice de uso de inteligencia artifical (IA) de 0 a 10 con base en el dominio del código y preguntas que puedan surgir. 
- Si se detecta el uso de ChatGPT o chatbots para realizar partes significativas del código, se aplicará un factor de descuento con base en este índice:

| Índice de uso (0 - 10)    |  % descuento |
|:-------|--------:|
| 0 - 3  |      0% |
| 4 - 6  |     30% |
| 7 - 8  |     60% |
| 9 - 10 |     90% |

**El uso de IA está permitido, pero su mal uso está prohibido.**

- Ejemplos de buen uso:
  - Explicación de piezas de código o sentencias del lenguaje.
  - Depuración de errores.
  - Elaboración de casos de pruebas.
  - Generación de ideas o mejoras en un programa.
  - Elaborar los docstrings de las funciones.
  - Consulta sobre flujos de trabajo en VSCode, GitHub, etc.
  - Pedir ejemplos sobre cómo utilizar una librería en Python. 
 
- Ejemplos de mal uso: 
  - Pedir a los chatbots que elaboren funciones o clases completas.
  - No entender el código brindado por los chatbots (uso ciego).
  - No entender la organización del código porque todo fue elaborado por el chatbot.





  # 📈 Simulador Interactivo de Modelos Macroeconómicos de Economía Abierta

Este proyecto es una herramienta educativa interactiva, desarrollada en un Jupyter Notebook, que visualiza los modelos macroeconómicos clave para una economía abierta: el **Modelo Mundell-Fleming** y el **Modelo DD-AA** de Krugman.

El objetivo es permitir a estudiantes y entusiastas de la economía explorar de manera dinámica cómo las políticas fiscales y monetarias afectan la renta, el tipo de cambio y otras variables económicas.



---

## ## 📚 Modelos Incluidos

El cuaderno `EconDynamics.ipynb` presenta una secuencia lógica de modelos que construyen la intuición de la macroeconomía abierta:

1.  **Mercado de Bienes (Cruz Keynesiana):** Visualización del equilibrio entre el gasto agregado y la producción.
2.  **Mercado de Dinero (Modelo LM):** Equilibrio entre la oferta y la demanda de dinero para determinar la tasa de interés.
3.  **Mercado de Divisas (Paridad de Intereses):** Muestra cómo se determina el tipo de cambio spot a través de los rendimientos de los activos nacionales y extranjeros.
4.  **Modelo DD-AA (Equilibrio General):** El modelo central que combina el equilibrio del mercado de bienes (curva DD) y el mercado de activos (curva AA) para encontrar simultáneamente la renta y el tipo de cambio de equilibrio.

---

## ## 🛠️ Tecnologías Utilizadas

* **Python 3.x**
* **Jupyter Notebook:** Para la presentación interactiva de la teoría y las visualizaciones.
* **Matplotlib:** Para la creación de las gráficas estáticas y dinámicas.
* **ipympl (Jupyter Matplotlib):** Para mejorar la interactividad de los gráficos en el notebook.
* **ipywidgets:** Para la creación de los sliders y controles interactivos.
* **NumPy:** Para los cálculos numéricos y la manipulación de arreglos.

---

# 📈 Simulador Interactivo de Macroeconomía Abierta

Este proyecto es una herramienta de aprendizaje visual diseñada para desmitificar los modelos teóricos de la macroeconomía de economía abierta. A través de un Jupyter Notebook interactivo, los conceptos abstractos del **Modelo Mundell-Fleming** y el **Modelo DD-AA** de Paul Krugman cobran vida, permitiendo a los usuarios ver de forma tangible cómo las decisiones de política económica impactan a una nación en el escenario global.

El objetivo principal es transformar las complejas interacciones entre tasas de interés, tipos de cambio y renta nacional en una experiencia intuitiva y exploratoria.



---

## ##  Propósito:

Este simulador fue creado como un puente entre la comunidad que se dedica a la investigación. Está dirigido a:

* **Investigadores:** Que buscan nuevas formas de publicar sus hallazgos.
* **Entusiastas y Autodidactas:** Interesados en explorar las mecánicas de la economía internacional sin necesidad de complejos modelos matemáticos.
* **Instructores y Profesores:** Que pueden utilizar esta herramienta como un recurso dinámico en sus clases para demostrar los efectos de distintos shocks económicos.

---

## ##  Los Modelos: Una introducción

El cuaderno está estructurado como un recorrido lógico, donde cada modelo construye sobre el anterior para pintar un cuadro completo de la economía abierta según el libro de Paul Krugman. 

### ### 1. El Mercado de Bienes (La Cruz Keynesiana)
Esta visualización muestra la relación fundamental entre el **gasto total** (consumo, inversión, gasto público y exportaciones netas) y el **ingreso nacional (Y)**. Permite explorar el concepto del **multiplicador keynesiano**, observando cómo un cambio inicial en el gasto genera un impacto amplificado en la producción total de equilibrio.

### ### 2. El Mercado de Dinero (Equilibrio LM)
Este modelo se adentra en el sector financiero, mostrando cómo se determina la **tasa de interés (i)**. La gráfica representa el equilibrio entre la **oferta de dinero**, controlada por el banco central, y la **demanda de dinero** por parte del público. Al manipular la oferta monetaria o el nivel de ingreso, se puede observar directamente cómo estas acciones presionan al alza o a la baja la tasa de interés de equilibrio, el "precio" del dinero.

### ### 3. El Mercado de Divisas (La Paridad de Intereses)
Este gráfico es crucial, pues visualiza la **condición de paridad de intereses**, el mecanismo que determina el **tipo de cambio (E)**. Muestra que el tipo de cambio se ajusta hasta que el rendimiento esperado de los depósitos en moneda nacional es igual al de los depósitos en moneda extranjera. Es el eslabón que une las decisiones de política monetaria interna con el valor internacional de la moneda.

### ### 4. El Modelo DD-AA (El Equilibrio General)
Este es el modelo culminante del proyecto. Integra los tres mercados anteriores en una sola visualización para determinar simultáneamente el **ingreso de equilibrio (Y)** y el **tipo de cambio de equilibrio (E)**.
* La **Curva DD** representa todos los puntos de equilibrio del mercado de bienes.
* La **Curva AA** representa todos los puntos de equilibrio del mercado de activos (dinero y divisas).

La intersección de ambas curvas muestra el equilibrio macroeconómico general. Moviendo los sliders, se pueden simular políticas fiscales o monetarias y observar el poderoso resultado final: cómo estas políticas afectan tanto la producción interna como la posición del país en el escenario internacional.

---

## ##  Requisitos para su Uso

Para ejecutar el proyecto, se requiere necesitas un entorno de Python con Jupyter Notebook y las siguientes librerías instaladas: `matplotlib`, `ipywidgets`, `numpy` y `ipympl`.

Una vez instalado el entorno, simplemente inicia Jupyter y abre el archivo `EconDynamics.ipynb`. Al ejecutar las celdas, podrás interactuar con cada uno de los modelos económicos descritos.