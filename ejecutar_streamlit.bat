@echo off
chcp 65001 > nul
echo ═══════════════════════════════════════════════
echo   🌐 ALQUIPC - Aplicación Web con Streamlit
echo ═══════════════════════════════════════════════
echo.

REM Verificar si streamlit está instalado
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo ⚠️ Streamlit no está instalado.
    echo.
    echo 📦 Instalando dependencias...
    pip install -r requirements.txt
    echo.
    if errorlevel 1 (
        echo ❌ Error al instalar dependencias.
        echo Por favor ejecuta manualmente: pip install -r requirements.txt
        pause
        exit /b 1
    )
)

echo ✅ Iniciando aplicación web...
echo.
echo 🌐 La aplicación se abrirá en tu navegador
echo 📍 URL: http://localhost:8501
echo.
echo 💡 Para detener el servidor, presiona Ctrl+C
echo.
echo ═══════════════════════════════════════════════
echo.

streamlit run alquipc_streamlit.py

pause
