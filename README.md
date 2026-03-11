# vehicles_env

Análisis Exploratorio de Datos: Mercado de Vehículos Usados

Este proyecto es una aplicación web interactiva desarrollada para visualizar y analizar un conjunto de datos de anuncios de venta de coches en los Estados Unidos. La herramienta permite a los usuarios finales explorar de forma gráfica variables críticas como el kilometraje y el precio.
Objetivos del Proyecto
•	Visualización Dinámica: Proporcionar una interfaz donde el usuario pueda generar gráficos a demanda (on-click).
•	Análisis de Distribución: Identificar los rangos de kilometraje más comunes mediante histogramas.
•	Análisis de Correlación: Estudiar la relación entre el uso del vehículo (odómetro) y su valor de mercado.
 
Funcionalidades de la Aplicación
1.	Carga Automática: La app lee directamente el archivo vehicles_us.csv al iniciar.
2.	Interfaz con Botones y Checkboxes: * Uso de st.button para disparar la creación de histogramas de forma instantánea.
o	Uso de st.checkbox para dar control al usuario sobre qué visualizaciones desea ver en pantalla.
3.	Gráficos de Dispersión: Generación de un Scatter Plot para visualizar cómo varía el precio a medida que aumenta el kilometraje.
Ejemplo de flujo de trabajo:
El usuario ingresa a la aplicación, selecciona la casilla de "Construir un histograma" y el sistema procesa la columna odometer del dataset para mostrar una gráfica de barras interactiva que representa la frecuencia de los vehículos según su recorrido.

Checalo en el siguiente link!:

https://vehicles-env-1i0g.onrender.com
