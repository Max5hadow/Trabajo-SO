Requisitos
- Windows 10/11 x64.
- Sin Python necesario para el usuario final.
- Permisos admin para PATH.

Instalación
1. Descargar desde Release:
   - AdivinaElNumero-Setup.exe
   - AdivinaElNumero-Setup.exe.sha256.txt
2. Verificar integridad opcional:
   Get-FileHash .\AdivinaElNumero-Setup.exe -Algorithm SHA256
3. Ejecutar instalador y seguir asistente.
4. Post instalación:
   Se ejecuta mi_algoritmo_version.bat en modo silencioso.
   Manualmente:
   mi_algoritmo_version.bat
   -> AdivinaElNumero-CLI version 1.0.0

Uso
- Abrir CMD/PowerShell.
- Ejecutar:
  adivina
- Jugar ingresando números hasta acertar o escribir “salir”.

Desinstalación
- Panel de control -> Agregar/Quitar programas -> AdivinaElNumero-CLI -> Desinstalar.
- Se eliminan binario, bat y accesos directos.

Actualización
- Descargar nuevo instalador y ejecutarlo.
- Verificar versión con mi_algoritmo_version.bat.
