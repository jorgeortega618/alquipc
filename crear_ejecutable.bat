@echo off
title ALQUIPC - Generador de Ejecutables
color 0B
echo.
echo ===============================================
echo    ALQUIPC - Generador de Ejecutables
echo ===============================================
echo.

echo Verificando si PyInstaller esta instalado...
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo PyInstaller no encontrado. Instalando...
    pip install pyinstaller
    if errorlevel 1 (
        echo Error: No se pudo instalar PyInstaller
        pause
        exit /b 1
    )
) else (
    echo PyInstaller ya esta instalado.
)

echo.
echo Seleccione que ejecutable crear:
echo.
echo 1. Ejecutable de linea de comandos (alquipc_cli.py)
echo 2. Ejecutable con interfaz grafica (alquipc_gui.py)
echo 3. Ambos ejecutables
echo 4. Cancelar
echo.
set /p opcion="Ingrese su opcion (1-4): "

if "%opcion%"=="1" goto cli_exe
if "%opcion%"=="2" goto gui_exe
if "%opcion%"=="3" goto ambos_exe
if "%opcion%"=="4" goto cancelar

:cli_exe
echo.
echo Creando ejecutable de linea de comandos...
pyinstaller --onefile --name ALQUIPC_CLI --icon=none --distpath=./ejecutables alquipc_cli.py
echo.
echo Ejecutable creado en: ./ejecutables/ALQUIPC_CLI.exe
goto fin

:gui_exe
echo.
echo Creando ejecutable con interfaz grafica...
pyinstaller --onefile --windowed --name ALQUIPC_GUI --icon=none --distpath=./ejecutables alquipc_gui.py
echo.
echo Ejecutable creado en: ./ejecutables/ALQUIPC_GUI.exe
goto fin

:ambos_exe
echo.
echo Creando ambos ejecutables...
echo.
echo 1/2 - Creando ejecutable CLI...
pyinstaller --onefile --name ALQUIPC_CLI --icon=none --distpath=./ejecutables alquipc_cli.py
echo.
echo 2/2 - Creando ejecutable GUI...
pyinstaller --onefile --windowed --name ALQUIPC_GUI --icon=none --distpath=./ejecutables alquipc_gui.py
echo.
echo Ambos ejecutables creados en: ./ejecutables/
goto fin

:cancelar
echo Operacion cancelada.
goto fin

:fin
echo.
echo Proceso completado.
echo.
echo NOTA: Los ejecutables son independientes y no requieren Python instalado.
echo Puedes distribuir los archivos .exe a otros usuarios de Windows.
echo.
pause
