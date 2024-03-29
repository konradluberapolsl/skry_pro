@echo off
title Projekt Semestralny Jezyki Skryptowe

:main
cls
echo.
echo "Program rozwiazuje ZADANIE 1 - 'SZYFROWANIE WIADOMOSCI' z konkursu Algorytmion 2015"
echo.
echo "1. Uruchom"
echo "2. Informacje"
echo "3. Wyswietl katalog BackUp"
echo "4. Wyjdz"
echo.
set /p op=">>"
if %op%==1 goto start 
if %op%==2 goto info
if %op%==3 goto backup
if %op%==4 goto koniec

:start
mkdir .\backup\backup_%date%
xcopy /Q /Y strona.html .\backup\backup_%date%
xcopy /Q /Y style.css .\backup\backup_%date%
xcopy /Q /Y strona.py .\backup\backup_%date%
xcopy /Q /Y server.py .\backup\backup_%date%
xcopy /Q /Y .\input .\backup\backup_%date%
xcopy /Q /Y .\output .\backup\backup_%date%
start server.exe
start strona.py
start strona.html
goto koniec

:info
cls 
echo "Projekt Semstralny z przedmiotu Jezyki Skryptowe"
echo " ZADANIE 1 - 'SZYFROWANIE WIADOMOSCI' z konkursu Algorytmion 2015"
echo.
echo "Konrad Lubera"
echo "Informatyka sem III grupa 1A, RMS"
pause
goto main

:backup
cls
dir .\backup /W
pause
goto main

:koniec
pause
echo on
