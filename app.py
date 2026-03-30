

import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import pandas as pd
import streamlit as st
import plotly.express as px


car_data = pd.read_csv('vehicles_us.csv')
# ===== SECCIÓN DE INFORMACIÓN DEL DATASET =====
st.header('📋 Información del Dataset')

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de vehículos", len(car_data))
    
with col2:
    st.metric("Columnas disponibles", len(car_data.columns))
    
with col3:
    st.metric("Datos faltantes", car_data.isnull().sum().sum())

# Mostrar primeras filas del dataset
if st.checkbox('Ver muestra de los datos'):
    st.dataframe(car_data.head())

st.markdown("---")

# ===== SECCIÓN DE VISUALIZACIONES =====
st.header('📊 Análisis Visual de los Datos')

# Crear pestañas para organizar mejor las visualizaciones
tab1, tab2, tab3 = st.tabs(["🚗 Distribuciones", "💰 Precios", "📈 Comparaciones"])

with tab1:
    st.subheader("Distribución de Vehículos")
    
    # Tu histograma existente mejorado
    fig_hist = px.histogram(car_data, 
                           x='model_year', 
                           title='Distribución de Vehículos por Año del Modelo',
                           color_discrete_sequence=['#1f77b4'])
    
    fig_hist.update_layout(
        title_font_size=16,
        xaxis_title="Año del Modelo",
        yaxis_title="Cantidad de Vehículos",
        showlegend=False
    )
    
    st.plotly_chart(fig_hist, use_container_width=True)

with tab2:
    st.subheader("Análisis de Precios")
    
    # Tu gráfico de dispersión mejorado
    fig_scatter = px.scatter(car_data, 
                            x='odometer', 
                            y='price',
                            title='Relación entre Kilometraje y Precio',
                            color_discrete_sequence=['#ff7f0e'])
    
    fig_scatter.update_layout(
        title_font_size=16,
        xaxis_title="Kilometraje",
        yaxis_title="Precio ($)",
    )
    
    st.plotly_chart(fig_scatter, use_container_width=True)

with tab3:
    st.subheader("Comparaciones por Categorías")
    
  
  # ===== SECCIÓN DE CONCLUSIONES =====
st.header('🎯 Conclusiones del Análisis')

# Crear columnas para organizar las conclusiones
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Hallazgos Principales")
    
    # Calcular estadísticas clave
    filtered_data = car_data.copy()
    avg_price = filtered_data['price'].mean()
    avg_mileage = filtered_data['odometer'].mean()
    most_common_condition = filtered_data['condition'].mode()[0]
    
    st.write("**Basado en el análisis de los datos:**")
    
    st.write(f"• **Precio promedio:** ${avg_price:,.0f}")
    st.write(f"• **Kilometraje promedio:** {avg_mileage:,.0f} millas")
    st.write(f"• **Condición más común:** {most_common_condition}")
    
    # Insight sobre correlación
    correlation = filtered_data['price'].corr(filtered_data['odometer'])
    st.write(f"• **Correlación precio-kilometraje:** {correlation:.2f}")
    
    if correlation < -0.3:
        st.write("  → Existe una relación negativa moderada")
    elif correlation < -0.1:
        st.write("  → Existe una relación negativa débil")
    else:
        st.write("  → La relación es muy débil")

with col2:
    st.subheader("💡 Recomendaciones")
    
    st.write("**Para compradores:**")
    st.write("• Considera vehículos con mayor kilometraje para mejores precios")
    st.write("• Los vehículos más nuevos mantienen mejor su valor")
    st.write("• La condición del vehículo es un factor importante")
    
    st.write("**Para vendedores:**")
    st.write("• Mantén el kilometraje bajo para maximizar el precio")
    st.write("• La condición 'excelente' puede justificar precios más altos")
    st.write("• Considera el año del modelo al fijar precios")

# Sección de metodología
st.markdown("---")
st.subheader("🔬 Metodología del Análisis")

with st.expander("Ver detalles técnicos"):
    st.write("""
    **Herramientas utilizadas:**
    - Python con pandas para manipulación de datos
    - Plotly Express para visualizaciones interactivas
    - Streamlit para la aplicación web
    
    **Análisis realizados:**
    - Distribución temporal de vehículos
    - Análisis de correlación precio-kilometraje
    - Segmentación por condición del vehículo
    - Filtrado interactivo por año del modelo
    """)