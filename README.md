# 💻 ALQUIPC - Facturación de Alquiler de Portátiles

## 📖 Descripción del Proyecto

**ALQUIPC** (Alquilamos Su PC) es una empresa de alquiler de computadores portátiles que necesita un sistema de facturación para sus servicios.

### 🛠️ Tecnología
Aplicación web desarrollada con **Streamlit**, un framework de Python diseñado para crear aplicaciones web interactivas de forma rápida y sencilla.

### ✨ Características
- ✅ **Aplicación Web Moderna** - Accesible desde cualquier navegador
- ✅ **Despliegue en la nube GRATIS** - Streamlit Cloud, Railway, Render
- ✅ **Interfaz responsiva** - Funciona en móvil, tablet y desktop
- ✅ **Sin instalación requerida** - Solo necesitas un navegador web
- ✅ **Validación en tiempo real** - Verificación automática de datos
- ✅ **Descarga de cotizaciones** - Exporta en TXT y JSON

### 🏢 Sobre la Empresa
La empresa **ALQUIPC** presta el servicio de alquiler de equipos de cómputo portátiles por días (no por horas). Los clientes llaman a la línea gratuita para solicitar equipos, y la operadora les asigna un ID-cliente único para la facturación.

### 💰 Tarifas y Condiciones
- **Tarifa base**: $35,000 COP por equipo por día
- **Mínimo de equipos**: 2 equipos por alquiler
- **Modalidades de servicio**:
  1. **Dentro de la ciudad**: Sin recargo adicional (0%)
  2. **Fuera de la ciudad**: Incremento del 5% por servicio a domicilio
  3. **Dentro del establecimiento**: Descuento del 5%

### 🎯 Beneficios Adicionales
- **Días adicionales**: 2% de descuento por cada día extra de alquiler
- **Compromiso ambiental**: Sin impresión de recibos (solo envío por email)
- **Información completa**: El sistema muestra todos los detalles del alquiler, descuentos/incrementos y valor total

## 🚀 Inicio Rápido

### Ejecución Local

**Opción 1: Script Automático (Windows)**
```bash
ejecutar_streamlit.bat
```

**Opción 2: Línea de Comandos**
```bash
# 1. Instalar dependencias (solo la primera vez)
pip install -r requirements.txt

# 2. Ejecutar la aplicación
streamlit run alquipc_streamlit.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

##  Campos Requeridos

El sistema incluye información completa del cliente:

- **ID Cliente**: Identificador único del cliente
- **Teléfono**: Número de contacto (acepta números, espacios, guiones y paréntesis)
- **Email**: Dirección de correo electrónico (validación de formato)
- **Equipos**: Número de portátiles a alquilar (mínimo 2)
- **Días iniciales**: Período base de alquiler
- **Días adicionales**: Extensión del alquiler (con 2% descuento)
- **Ubicación**: ciudad (0%), fuera (+5%), local (-5%)

## 🌐 Despliegue en Línea

### Streamlit Cloud (Recomendado - GRATIS)

**Requisitos:**
- Cuenta de GitHub
- Repositorio público con tu código

**Pasos:**

1. **Sube tu código a GitHub**
   ```bash
   git add .
   git commit -m "Deploy ALQUIPC"
   git push origin main
   ```

2. **Configura Streamlit Cloud**
   - Ve a [share.streamlit.io](https://share.streamlit.io)
   - Inicia sesión con GitHub y autoriza el acceso
   - Clic en "New app"
   - Selecciona tu repositorio: `jorgeortega618/alquipc`
   - Branch: `main`
   - Main file: `alquipc_streamlit.py`
   - Clic en "Deploy"

3. **¡Listo! 🎉**
   - Tu app estará en: `https://[tu-usuario]-alquipc.streamlit.app`
   - Se actualiza automáticamente con cada push

### Alternativas de Despliegue Gratuito

**Railway** (railway.app)
- Conecta tu GitHub y selecciona el repositorio
- Railway detecta automáticamente Streamlit
- Usa el archivo `Procfile` incluido en el proyecto

**Render** (render.com)
- Conecta GitHub → "New Web Service"
- Build Command: `pip install -r requirements.txt`
- Start Command: `streamlit run alquipc_streamlit.py --server.port=$PORT --server.address=0.0.0.0`

## 📂 Estructura del Proyecto

```
alquipc/
├── core.py                    # Lógica del negocio
├── alquipc_streamlit.py       # Aplicación web
├── requirements.txt           # Dependencias Python
├── Procfile                   # Configuración para despliegue
├── ejecutar_streamlit.bat     # Script de inicio (Windows)
├── .streamlit/
│   └── config.toml            # Configuración de tema
└── README.md                  # Documentación
```

## 🔄 Flujo de Trabajo

1. **Cliente llama** a la línea gratuita de ALQUIPC
2. **Operadora ingresa**:
   - Información del cliente (ID, teléfono, email)
   - Número de equipos a alquilar (mínimo 2)
   - Días iniciales de alquiler
   - Ubicación del servicio
3. **Sistema calcula**:
   - Costo base (equipos × días × $35,000)
   - Ajustes por ubicación (+5% fuera, -5% local)
   - Descuentos por días adicionales (2% por día extra)
4. **Resultado**: Cotización completa con opción de descarga (sin impresión)

## 🔧 Solución de Problemas

### Error: "streamlit no encontrado"
```bash
pip install streamlit
```

### Error: "ModuleNotFoundError: No module named 'core'"
Asegúrate de estar en el directorio correcto:
```bash
cd ruta/al/proyecto/alquipc
```

### La app no se abre en el navegador
Abre manualmente: http://localhost:8501

### Puerto ocupado
```bash
streamlit run alquipc_streamlit.py --server.port=8502
```

## 🎨 Características de la Interfaz

- **Formularios intuitivos** - Layout en dos columnas
- **Selector visual de ubicación** - Con iconos descriptivos
- **Tabs organizadas** - Resumen, Detalles, JSON
- **Métricas visuales** - Cards con valores destacados
- **Descarga de archivos** - TXT y JSON
- **Validación automática** - Mensajes de error claros
- **Diseño responsivo** - Funciona en móvil, tablet y desktop

## 🛠️ Requisitos Técnicos

- Python 3.8 o superior
- Streamlit 1.28.0 o superior
- Navegador web moderno (Chrome, Firefox, Safari, Edge)

---

**🌱 Compromiso ambiental: Sin impresión de recibos**

ALQUIPC © 2025 - Sistema de Facturación de Alquiler de Portátiles
