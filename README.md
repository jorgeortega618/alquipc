# ALQUIPC - Facturación de alquiler de portátiles

## 📖 Descripción del Proyecto

**ALQUIPC** (Alquilamos Su PC) es una empresa de alquiler de computadores portátiles que necesita un sistema de facturación para sus servicios.

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

##  Formas de Ejecutar

### 1. Interfaz Gráfica 
```bash
python alquipc_gui.py
```
O simplemente hacer doble clic en `ejecutar_alquipc.bat` y seleccionar opción 1.

### 2. Línea de Comandos 
```bash
python alquipc_cli.py --id C-001 --telefono "3008000" --email "jorge@gmail.com" --equipos 3 --dias 2 --extra 1 --ubicacion fuera --json
```

### 3. Script Interactivo 
Hacer doble clic en `ejecutar_alquipc.bat` para menú interactivo con opciones:
- Interfaz gráfica
- Línea de comandos guiada
- Ejemplo rápido

##  Generar Ejecutables (.exe)
Hacer doble clic en `crear_ejecutable.bat` o ejecutar:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name ALQUIPC_GUI alquipc_gui.py
pyinstaller --onefile --name ALQUIPC_CLI alquipc_cli.py
```

Los ejecutables se crean en la carpeta `ejecutables/` y funcionan sin necesidad de tener Python instalado.

##  Campos Requeridos

El sistema incluye información completa del cliente:

- **ID Cliente**: Identificador único del cliente
- **Teléfono**: Número de contacto (acepta números, espacios, guiones y paréntesis)
- **Email**: Dirección de correo electrónico (validación de formato)
- **Equipos**: Número de portátiles a alquilar (mínimo 2)
- **Días iniciales**: Período base de alquiler
- **Días adicionales**: Extensión del alquiler (con 2% descuento)
- **Ubicación**: ciudad (0%), fuera (+5%), local (-5%)

## 🔄 Flujo de Trabajo

1. **Cliente llama** a la línea gratuita de ALQUIPC
2. **Operadora solicita**:
   - Información del cliente (ID, teléfono, email)
   - Número de equipos a alquilar (mínimo 2)
   - Días iniciales de alquiler
   - Ubicación del servicio
3. **Sistema calcula**:
   - Costo base (equipos × días × $35,000)
   - Ajustes por ubicación (+5% fuera, -5% local)
   - Descuentos por días adicionales (2% por día extra)
4. **Resultado**: Cotización completa enviada por email (sin impresión)
