# ?? IPTV List Checker - Verificador de Canales

### Herramienta para verificar el estado de canales IPTV en listas m3u
Este script permite verificar r�pidamente si los enlaces de canales IPTV en una lista m3u est�n activos o inactivos. Los canales activos se guardan en un archivo separado, mientras que los inactivos se listan en otro archivo.

## :information_source: Descripci�n
Este verificador de IPTV revisa cada enlace en una lista de canales m3u y determina si est� activo o inactivo:
- Los **canales activos** se guardan en un archivo limpio para ser usados.
- Los **canales inactivos** se registran en un archivo de canales ca�dos para revisi�n.

## :computer: Instalaci�n
```python3
pip install -r requirements.txt
git clone https://github.com/tu_usuario/IPTV-List-Checker.git
cd IPTV-List-Checker
echo "requests\ncolorama" > requirements.txt
pip install -r requirements.txt
```

## :rocket: Modo de Uso
Ejecuta el script de la siguiente manera:

```python3
python3 iptv_checker.py
```

Archivo de entrada: lista_de_canales.txt

Archivos de salida:
- lista_de_canales_limpia.txt - Contiene los canales activos.
- canales_inactivos.txt - Contiene los canales inactivos.

## ? Ejemplo de Salida

Al ejecutar el script, ver�s algo similar a lo siguiente en la consola:

```plaintext
+-----------------------------------------------------------------+
�           IPTV LIST CHECKER - VERIFICADOR DE CANALES           �
�                                                                 �
�      Herramienta para verificar el estado de canales IPTV       �
�      Activos se muestran en verde y los inactivos en rojo       �
+-----------------------------------------------------------------+

?? Canal activo: http://example.com/canal1.m3u8
? Canal inactivo eliminado: http://example.com/canal2.m3u8
...
Canales activos guardados en: lista_de_canales_limpia.txt
Canales inactivos guardados en: canales_inactivos.txt
```

## ?? Ejemplo de Formato de Entrada 
```plaintext
#EXTM3U
#EXTINF:-1, Canal Ejemplo
http://example.com/stream.m3u8
```

## ?? Archivos de Configuraci�n

Entrada: lista_de_canales.txt

Salida:
- lista_de_canales_limpia.txt - Lista limpia de canales activos.
- canales_inactivos.txt - Lista de canales ca�dos.


## :star2: Caracter�sticas

- **Verificaci�n concurrente** de canales usando `ThreadPoolExecutor` para mayor velocidad.
- Colores en la consola para una visualizaci�n f�cil: los canales activos aparecen en verde y los inactivos en rojo.
- **Interrupci�n segura** con `Ctrl + C`, que guarda el progreso al momento de interrumpir la ejecuci�n.
- Muestra un **banner elegante** al inicio.

## :bookmark_tabs: Notas

- Aseg�rate de que los enlaces en lista_de_canales.txt sean v�lidos y contengan http.
- Puedes interrumpir la ejecuci�n en cualquier momento con Ctrl + C; el progreso se guardar�.

## :hammer_and_wrench: Requisitos 

- **Python 3.6+**
- Librer�as:
  - `requests` para realizar las verificaciones HTTP.
  - `colorama` para los colores en la consola.

## :memo: Personalizaci�n

Puedes ajustar los comandos y configuraciones del script seg�n tus necesidades modificando el archivo `   `

## :open_file_folder: Estructura del Repositorio

| Icono            | Nombre                      | Descripci�n                                              |
|------------------|-----------------------------|----------------------------------------------------------|
| :file_folder:    | Desarrollador               | Carpeta de Desarrollador del proyecto                    |
| :file_folder:    | Herramientas                | Carpeta de herramientas extras                           |
| :file_folder:    | Im�genes                    | Carpeta para im�genes del proyecto                       |
| :page_facing_up: | .gitattributes              | Archivo para configuraci�n de Git                        |
| :page_facing_up: | LICENSE                     | Archivo de licencia del proyecto                         |
| :page_facing_up: | iptv_checker.py             | Script principal para verificar enlaces de canales IPTV  |
| :page_facing_up: | lista_de_canales.txt        | Archivo de entrada con enlaces de canales en formato m3u |
| :page_facing_up: | lista_de_canales_limpia.txt | Archivo de salida con canales activos                    |
| :page_facing_up: | canales_inactivos.txt       | Archivo de salida con canales inactivos                  |
| :page_facing_up: | requirements.txt            | Archivo con las dependencias necesarias para el script   |
| :book:           | README.md                   | Archivo de documentaci�n principal                       |

| :package:        | install.sh          | Script de instalaci�n automatizada        |
| :page_facing_up: | menu.sh             | Herramienta de utilidades                 |

## :star2: Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar este script o encuentras alg�n problema, si�ntete libre de abrir un *pull request* o *issue*.

## :warning: Advertencias

- Uso Responsable: Este script est� dise�ado para ser utilizado en dispositivos y redes que te pertenecen o para las que tienes permiso de uso. No lo utilices para actividades no autorizadas.

## :email: Contacto 
* :busts_in_silhouette: **Dzhoni**: [GitHub](https://github.com/AAAAAEXQOSyIpN2JZ0ehUQ/Hacking-Wifi) - Desarrollador Hacking-Wifi

? https://t.me/AAAAAEXQOSyIpN2JZ0ehUQ [  ???? ] ?
