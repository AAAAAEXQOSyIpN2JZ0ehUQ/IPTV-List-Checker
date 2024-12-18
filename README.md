﻿# :tv: IPTV List Checker - Verificador de Canales :octocat:

### Herramienta para verificar el estado de canales IPTV en listas m3u
Este script permite verificar rápidamente si los enlaces de canales IPTV en una lista m3u están activos o inactivos. Los canales activos se guardan en un archivo separado, mientras que los inactivos se listan en otro archivo.

## :information_source: Descripción
Este verificador de IPTV revisa cada enlace en una lista de canales m3u y determina si está activo o inactivo:
- Los **canales activos** se guardan en un archivo limpio para ser usados.
- Los **canales inactivos** se registran en un archivo de canales caídos para revisión.

## :computer: Instalación

### En Windows:

![logo](https://github.com/AAAAAEXQOSyIpN2JZ0ehUQ/IPTV-List-Checker/blob/main/Imagenes/IPTV-List-Checker_Windows.png)

Para instalar y ejecutar el script IPTV List Checker, sigue estos pasos:

1. Descarga el archivo ZIP del repositorio:

   [Descargar el repositorio](https://github.com/AAAAAEXQOSyIpN2JZ0ehUQ/IPTV-List-Checker/archive/refs/heads/main.zip)

2. Extrae el contenido del archivo ZIP:

   Descomprime el archivo descargado en una carpeta de tu elección. Esto creará una carpeta con todos los archivos necesarios.

## :rocket: Modo de Uso

Sigue estos pasos para ejecutar el script.

1. Navega al directorio del script Windows.

   Navega hasta la carpeta donde descomprimiste el archivo ZIP. 

2. Ejecuta el script:

   Dentro de la carpeta descomprimida, haz doble clic en uno de los siguientes archivos para ejecutar el script:

   - `RunGet-iptv_checker.cmd` 
   - `RunGet-iptv_checker.bat` 

3. **Visualiza los resultados:**

   - El script mostrará el progreso y resultados en la consola.
   - Los canales se guardarán en un archivo de texto llamado `lista_de_canales_limpia.txt` y en el canales eliminados `canales_inactivos.txt`.

### En Linux:

![logo](https://github.com/AAAAAEXQOSyIpN2JZ0ehUQ/IPTV-List-Checker/blob/main/Imagenes/IPTV-List-Checker_Linux.png)

```python3
git clone https://github.com/AAAAAEXQOSyIpN2JZ0ehUQ/IPTV-List-Checker.git
cd IPTV-List-Checker
pip install -r requirements.txt
ls -ltha
```

1. Navega al directorio del script Linux:

  Accede a la carpeta donde descargaste el script.

## :rocket: Modo de Uso

2. Ejecuta el script:

  Abre una terminal y ejecuta el script usando el siguiente comando:

```bash
python3 iptv_checker.py
```

3. **Visualiza los resultados:**

   - El script mostrará el progreso y resultados en la consola.
   - Los canales se guardarán en un archivo de texto llamado `lista_de_canales_limpia.txt` y en el canales eliminados `canales_inactivos.txt`.

## :sparkles: Ejemplo de Salida

Al ejecutar el script, verás algo similar a lo siguiente en la consola:

```plaintext
╔═════════════════════════════════════════════════════════════════╗
║           IPTV LIST CHECKER - VERIFICADOR DE CANALES            ║
║                                                                 ║
║      Herramienta para verificar el estado de canales IPTV       ║
║      Activos se muestran en verde y los inactivos en rojo       ║
║                                                                 ║
║       Versión codificada por: Jony Rivera (Dzhoni)              ║
╚═════════════════════════════════════════════════════════════════╝

[+] Canal activo: http://example.com/canal1.m3u8
[-] Canal inactivo eliminado: http://example.com/canal2.m3u8

Canales activos guardados en: lista_de_canales_limpia.txt

Canales inactivos guardados en: canales_inactivos.txt

[*] GITHUB OFICIAL: https://github.com/AAAAAEXQOSyIpN2JZ0ehUQ/IPTV-List-Checker

Presiona Enter para cerrar la terminal.
```

Archivos de salida:
- lista_de_canales_limpia.txt - Contiene los canales activos.
- canales_inactivos.txt - Contiene los canales inactivos.


## :clipboard: Ejemplo de Formato de Entrada 

Archivo de entrada: lista_de_canales.txt

```plaintext
#EXTM3U
#EXTINF:-1, Canal Ejemplo
http://example.com/stream.m3u8
```

## :wrench: Archivos de Configuración

Entrada: lista_de_canales.txt

Salida:
- lista_de_canales_limpia.txt - Lista limpia de canales activos.
- canales_inactivos.txt - Lista de canales caídos.


## :star2: Características

- **Verificación concurrente** de canales usando `ThreadPoolExecutor` para mayor velocidad.
- Colores en la consola para una visualización fácil: los canales activos aparecen en verde y los inactivos en rojo.
- **Interrupción segura** con `Ctrl + C`, que guarda el progreso al momento de interrumpir la ejecución.
- Muestra un **banner elegante** al inicio.

## :bookmark_tabs: Notas

- Asegúrate de que los enlaces en lista_de_canales.txt sean válidos y contengan http.
- Puedes interrumpir la ejecución en cualquier momento con Ctrl + C; el progreso se guardará.

## :hammer_and_wrench: Requisitos 

- **Python 3.6+**
- Librerías:
  - `requests` para realizar las verificaciones HTTP.
  - `colorama` para los colores en la consola.

## :memo: Personalización

Puedes ajustar los comandos y configuraciones del script según tus necesidades modificando el archivo `IPTV-List-Checker/verificar_iptv.py`

## :open_file_folder: Estructura del Repositorio

| Icono            | Nombre                      | Descripción                                              |
|------------------|-----------------------------|----------------------------------------------------------|
| :file_folder:    | Desarrollador               | Carpeta de Desarrollador del proyecto                    |
| :file_folder:    | Herramientas                | Carpeta de herramientas extras                           |
| :file_folder:    | Imágenes                    | Carpeta para imágenes del proyecto                       |
| :page_facing_up: | .gitattributes              | Archivo para configuración de Git                        |
| :book:           | README.md                   | Archivo de documentación principal                       |
| :package:        | install.sh                  | Script de instalación automatizada                       |
| :page_facing_up: | LICENSE                     | Archivo de licencia del proyecto                         |
| :page_facing_up: | iptv_checker.py             | Script principal para verificar enlaces de canales IPTV  |
| :page_facing_up: | lista_de_canales.txt        | Archivo de entrada con enlaces de canales en formato m3u |
| :page_facing_up: | lista_de_canales_limpia.txt | Archivo de salida con canales activos                    |
| :page_facing_up: | canales_inactivos.txt       | Archivo de salida con canales inactivos                  |
| :page_facing_up: | requirements.txt            | Archivo con las dependencias necesarias para el script   |
| :page_facing_up: | RunGet-iptv_checker.bat     | Script de batch para ejecutar el script en Windows       |
| :page_facing_up: | RunGet-iptv_checker.cmd     | Script de bat para ejecutar el script en Windows         |

## :star2: Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar este script o encuentras algún problema, siéntete libre de abrir un *pull request* o *issue*.

## :warning: Advertencias

- Uso Responsable: Este script está diseñado para ser utilizado en dispositivos y redes que te pertenecen o para las que tienes permiso de uso. No lo utilices para actividades no autorizadas.

## :email: Contacto 
* :busts_in_silhouette: **Dzhoni**: [GitHub](https://github.com/AAAAAEXQOSyIpN2JZ0ehUQ/IPTV-List-Checker) - Desarrollador IPTV-List-Checker

☆ https://t.me/AAAAAEXQOSyIpN2JZ0ehUQ [  ⃘⃤꙰✰ ] ☆
