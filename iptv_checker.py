#!/usr/bin/env python3
#====================================================
#   SCRIPT:                   IPTV List Checker - Verificador de Canales
#   DESARROLLADO POR:         Jony Rivera (Dzhoni) 
#   FECHA DE ACTUALIZACIÓN:   14-11-2024 
#   CONTACTO POR TELEGRAMA:   https://t.me/Dzhoni_dev
#   GITHUB OFICIAL:           https://github.com/AAAAAEXQOSyIpN2JZ0ehUQ/IPTV-List-Checker
#====================================================

# Importación de módulos necesarios
import requests
from concurrent.futures import ThreadPoolExecutor
import time
from colorama import Fore, Style, init
import os
import sys

# Inicializa colorama
init(autoreset=True)

# Paleta de colores
reset = Style.RESET_ALL      # Restablecer todos los estilos y colores
bold = Style.BRIGHT          # Texto en negrita
italic = ""                  # (Colorama no soporta cursiva directamente)
underline = ""               # (Colorama no soporta subrayado directamente)
blink = ""                   # (Colorama no soporta parpadeo directamente)

# Colores
white = Fore.WHITE
black = Fore.BLACK
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
magenta = Fore.MAGENTA
cyan = Fore.CYAN

# Iconos v3
checkmark = f"{white}[{green}+{white}]"
error = f"{white}[{red}-{white}]{red}"
info = f"{white}[{yellow}*{white}]{yellow}"
unknown = f"{white}[{blue}!{white}]{blue}"
process = f"{white}[{magenta}>>{white}]"
indicator = f"{red}==>{cyan}"

# Barra de separación
barra = f"{blue}|--------------------------------------------|{reset}"
bar = f"{yellow}----------------------------------------------{reset}"

# Función para mostrar el banner
def mostrar_banner():
    banner = f"""
{cyan}{bold}╔═════════════════════════════════════════════════════════════════╗
║           {green}IPTV LIST CHECKER - VERIFICADOR DE CANALES            {cyan}║
║                                                                 {cyan}║
║      {yellow}Herramienta para verificar el estado de canales IPTV       {cyan}║
║      {yellow}Activos se muestran en verde y los inactivos en rojo       {cyan}║
║                                                                 {cyan}║
║          {magenta}Versión codificada por: Jony Rivera (Dzhoni)           {cyan}║
╚═════════════════════════════════════════════════════════════════╝
"""
    print(banner)
    time.sleep(1)

# Muestra el banner al inicio
mostrar_banner()

def verificar_url(url):
    try:
        respuesta = requests.head(url, timeout=5)
        return respuesta.status_code == 200
    except requests.RequestException:
        return False

def limpiar_lista(input_file, output_file, inactive_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as archivo_entrada, \
             open(output_file, 'w', encoding='utf-8') as archivo_salida, \
             open(inactive_file, 'w', encoding='utf-8') as archivo_inactivos:
            
            mantener_seccion = True
            for linea in archivo_entrada:
                if linea.startswith("#"):
                    archivo_salida.write(linea)
                    if "EXTINF" in linea:
                        mantener_seccion = True
                elif linea.strip() and linea.startswith("http"):
                    # Usando multihilos para mejorar la velocidad en la verificación
                    with ThreadPoolExecutor() as executor:
                        futuro = executor.submit(verificar_url, linea.strip())
                        if mantener_seccion and futuro.result():
                            archivo_salida.write(linea)
                            print(f"{checkmark} Canal activo: {linea.strip()}")
                        else:
                            archivo_inactivos.write(linea)
                            print(f"{error} Canal inactivo guardado en lista de inactivos: {linea.strip()}")
                else:
                    archivo_salida.write(linea)

    except KeyboardInterrupt:
        print(f"{yellow}\n{unknown} Ejecución interrumpida por el usuario. Guardando progreso...")
        print(f"{yellow}El archivo ha sido procesado hasta el punto de la interrupción.")
        exit(0)
    except Exception as e:
        print(f"{error} Error: {str(e)}")
        exit(1)

# Llama a la función con los archivos de entrada y salida
input_file = "lista_de_canales.txt"  # Cambia este nombre por el archivo que quieras limpiar
output_file = "lista_de_canales_limpia.txt"
inactive_file = "canales_inactivos.txt"  # Archivo para canales inactivos
limpiar_lista(input_file, output_file, inactive_file)
print(f"\n{cyan}Canales activos guardados en: {output_file}")
print(f"\n{cyan}Canales inactivos guardados en: {inactive_file}")

print(f"\n{info} {white}GITHUB OFICIAL: {green}https://github.com/AAAAAEXQOSyIpN2JZ0ehUQ/IPTV-List-Checker")

# Esperar a que el usuario presione Enter para cerrar la consola
input(f"\nPresiona {bold}{cyan}Enter{yellow} para cerrar la {green}terminal.")

"""
 Fin del script
"""