@echo off
title ALQUIPC - Cotizador de Alquiler de Portatiles
color 0A
echo.
echo ===============================================
echo    ALQUIPC - Cotizador de Alquiler
echo ===============================================
echo.

:menu
echo Seleccione una opcion:
echo.
echo 1. Ejecutar interfaz grafica (GUI)
echo 2. Ejecutar version de linea de comandos
echo 3. Ejemplo rapido
echo 4. Salir
echo.
set /p opcion="Ingrese su opcion (1-4): "

if "%opcion%"=="1" goto gui
if "%opcion%"=="2" goto cli
if "%opcion%"=="3" goto ejemplo
if "%opcion%"=="4" goto salir
goto menu

:gui
echo.
echo Iniciando interfaz grafica...
python alquipc_gui.py
pause
goto menu

:cli
echo.
echo === Cotizador por Linea de Comandos ===
echo.
set /p id_cliente="ID Cliente: "
set /p telefono_cliente="Telefono Cliente: "
set /p email_cliente="Email Cliente: "
set /p equipos="Numero de equipos (min 2): "
set /p dias="Dias iniciales: "
set /p extra="Dias adicionales (0 si no hay): "
echo.
echo Ubicaciones disponibles:
echo   ciudad - Dentro de la ciudad (sin recargo)
echo   fuera  - Fuera de la ciudad (+5%%)
echo   local  - En el establecimiento (-5%%)
echo.
set /p ubicacion="Ubicacion (ciudad/fuera/local): "
echo.
echo Calculando...
python alquipc_cli.py --id "%id_cliente%" --telefono "%telefono_cliente%" --email "%email_cliente%" --equipos %equipos% --dias %dias% --extra %extra% --ubicacion %ubicacion% --json
echo.
pause
goto menu

:ejemplo
echo.
echo === Ejecutando ejemplo de prueba ===
echo Cliente: C-001, telefono: 3008000, email: jorge@gmail.com
echo 3 equipos, 2 dias + 1 extra, fuera de ciudad
echo.
python alquipc_cli.py --id C-001 --telefono "3008000" --email "jorge@gmail.com" --equipos 3 --dias 2 --extra 1 --ubicacion fuera --json
echo.
pause
goto menu

:salir
echo.
echo Gracias por usar ALQUIPC!
timeout /t 2 >nul
exit
