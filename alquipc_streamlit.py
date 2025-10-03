#!/usr/bin/env python3
"""
ALQUIPC - Aplicación Web con Streamlit
Sistema de facturación para alquiler de portátiles
"""
import streamlit as st
import json
from core import QuoteInput, cotizar, formato_resumen, to_dict, ValidationError

# Configuración de la página
st.set_page_config(
    page_title="ALQUIPC - Cotizador",
    page_icon="💻",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Título y descripción
st.title("💻 ALQUIPC - Cotizador de Alquiler de Portátiles")
st.markdown("---")
st.markdown("""
**ALQUIPC** - Sistema de cotización para alquiler de equipos portátiles
- Tarifa base: **$35,000 COP** por equipo/día
- Mínimo: **2 equipos**
- Descuento: **2%** por días adicionales
- Ajustes por ubicación: Ciudad (0%), Fuera (+5%), Local (-5%)
""")
st.markdown("---")

# Crear dos columnas para el formulario
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Información del Cliente")
    id_cliente = st.text_input(
        "ID Cliente *",
        value="C-001",
        help="Identificador único del cliente"
    )
    
    telefono_cliente = st.text_input(
        "Teléfono *",
        value="3008000",
        help="Número de contacto del cliente"
    )
    
    email_cliente = st.text_input(
        "Email *",
        value="jorge@gmail.com",
        help="Correo electrónico del cliente"
    )

with col2:
    st.subheader("🖥️ Detalles del Alquiler")
    n_equipos = st.number_input(
        "Número de Equipos *",
        min_value=2,
        max_value=50,
        value=3,
        step=1,
        help="Mínimo 2 equipos"
    )
    
    dias_iniciales = st.number_input(
        "Días Iniciales *",
        min_value=1,
        max_value=365,
        value=2,
        step=1,
        help="Período base de alquiler"
    )
    
    dias_adicionales = st.number_input(
        "Días Adicionales",
        min_value=0,
        max_value=365,
        value=0,
        step=1,
        help="Días extra con 2% de descuento"
    )

# Ubicación del servicio
st.markdown("---")
ubicacion = st.radio(
    "📍 Ubicación del Servicio",
    options=["ciudad", "fuera", "local"],
    format_func=lambda x: {
        "ciudad": "🏙️ Dentro de la ciudad (0%)",
        "fuera": "🚗 Fuera de la ciudad (+5%)",
        "local": "🏢 Dentro del establecimiento (-5%)"
    }[x],
    horizontal=True
)

st.markdown("---")

# Botones de acción
col_btn1, col_btn2, col_btn3 = st.columns([2, 1, 1])

with col_btn1:
    calcular = st.button("💰 Calcular Cotización", type="primary", use_container_width=True)

with col_btn2:
    limpiar = st.button("🗑️ Limpiar", use_container_width=True)

with col_btn3:
    mostrar_json = st.checkbox("JSON", help="Mostrar salida en formato JSON")

# Lógica del botón limpiar
if limpiar:
    st.rerun()

# Calcular cotización
if calcular:
    try:
        # Crear entrada
        entrada = QuoteInput(
            n_equipos=int(n_equipos),
            dias_iniciales=int(dias_iniciales),
            dias_adicionales=int(dias_adicionales),
            ubicacion=ubicacion,
            id_cliente=id_cliente.strip(),
            telefono_cliente=telefono_cliente.strip(),
            email_cliente=email_cliente.strip()
        )
        
        # Calcular cotización
        resultado = cotizar(entrada)
        
        # Mostrar resultado
        st.markdown("---")
        st.success("✅ Cotización calculada exitosamente")
        
        # Crear tabs para diferentes vistas
        tab1, tab2, tab3 = st.tabs(["📄 Resumen", "💵 Detalles", "📊 Datos JSON"])
        
        with tab1:
            st.markdown("### Resumen de Cotización")
            resumen = formato_resumen(resultado)
            st.text(resumen)
            
            # Botón para copiar
            st.download_button(
                label="📥 Descargar Resumen",
                data=resumen,
                file_name=f"cotizacion_{resultado.id_cliente}.txt",
                mime="text/plain"
            )
        
        with tab2:
            st.markdown("### Detalles del Cálculo")
            
            # Cliente
            st.markdown("**👤 Información del Cliente**")
            col_d1, col_d2, col_d3 = st.columns(3)
            with col_d1:
                st.metric("ID Cliente", resultado.id_cliente)
            with col_d2:
                st.metric("Teléfono", resultado.telefono_cliente)
            with col_d3:
                st.metric("Email", resultado.email_cliente)
            
            st.markdown("---")
            
            # Equipos y días
            st.markdown("**🖥️ Detalles del Alquiler**")
            col_d4, col_d5, col_d6 = st.columns(3)
            with col_d4:
                st.metric("Equipos", resultado.n_equipos)
            with col_d5:
                st.metric("Días Iniciales", resultado.dias_iniciales)
            with col_d6:
                st.metric("Días Adicionales", resultado.dias_adicionales)
            
            st.markdown("---")
            
            # Costos
            st.markdown("**💰 Desglose de Costos**")
            col_d7, col_d8 = st.columns(2)
            with col_d7:
                st.metric("Precio Base/Día", f"${resultado.precio_base_diario:,.0f}")
                st.metric("Total Días Iniciales", f"${resultado.total_inicial:,.0f}")
                st.metric("Total Días Adicionales", f"${resultado.total_adicional:,.0f}")
            with col_d8:
                st.metric("Subtotal", f"${resultado.subtotal:,.0f}")
                st.metric("Ajuste Ubicación", 
                         f"${resultado.ajuste_ubicacion_valor:,.0f}",
                         delta=f"{resultado.ajuste_ubicacion_pct*100:.0f}%")
                st.metric("**TOTAL A PAGAR**", f"${resultado.total_pagar:,.0f}", delta=None)
            
            # Descuentos e incrementos
            if resultado.descuentos_aplicados:
                st.success("**✅ Descuentos Aplicados:**")
                for key, desc in resultado.descuentos_aplicados.items():
                    st.write(f"- {desc}")
            
            if resultado.incrementos_aplicados:
                st.warning("**⚠️ Incrementos Aplicados:**")
                for key, inc in resultado.incrementos_aplicados.items():
                    st.write(f"- {inc}")
        
        with tab3:
            st.markdown("### Datos en Formato JSON")
            datos_json = to_dict(resultado)
            st.json(datos_json)
            
            # Botón para descargar JSON
            st.download_button(
                label="📥 Descargar JSON",
                data=json.dumps(datos_json, ensure_ascii=False, indent=2),
                file_name=f"cotizacion_{resultado.id_cliente}.json",
                mime="application/json"
            )
        
    except ValidationError as e:
        st.error(f"❌ **Error de Validación:** {str(e)}")
    except ValueError as e:
        st.error(f"❌ **Error de Entrada:** Verifica que todos los campos numéricos sean válidos.")
    except Exception as e:
        st.error(f"❌ **Error Inesperado:** {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9em;'>
    <p>🌱 Compromiso ambiental: Sin impresión de recibos</p>
    <p>ALQUIPC © 2025 - Sistema de Facturación de Alquiler de Portátiles</p>
</div>
""", unsafe_allow_html=True)
