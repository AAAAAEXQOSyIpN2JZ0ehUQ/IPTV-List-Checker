#!/usr/bin/env python3
#====================================================
#   SCRIPT:                   IPTV List Checker - Verificador de Canales
#   DESARROLLADO POR:         Jony Rivera (Dzhoni) 
#   FECHA DE ACTUALIZACIÃ“N:  14-11-2024 
#   CONTACTO POR TELEGRAMA:   https://t.me/Dzhoni_dev
#   GITHUB OFICIAL:           https://github.com/AAAAAEXQOSyIpN2JZ0ehUQ/IPTV-List-Checker
#====================================================

# Importación de módulos necesarios
import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Style
import time

# Inicializa colorama
init(autoreset=True)

# Función para mostrar el banner
def mostrar_banner():
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}╔═════════════════════════════════════════════════════════════════╗
║           {Fore.GREEN}IPTV LIST CHECKER - VERIFICADOR DE CANALES            {Fore.CYAN}║
║                                                                 {Fore.CYAN}║
║      {Fore.YELLOW}Herramienta para verificar el estado de canales IPTV       {Fore.CYAN}║
║      {Fore.YELLOW}Activos se muestran en verde y los inactivos en rojo       {Fore.CYAN}║
║                                                                 {Fore.CYAN}║
║       {Fore.MAGENTA}Versión codificada por: Jony Rivera (Dzhoni)              {Fore.CYAN}║
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
                            print(Fore.GREEN + f"✔️ Canal activo: {linea.strip()}")
                        else:
                            archivo_inactivos.write(linea)
                            print(Fore.RED + f"❌ Canal inactivo guardado en lista de inactivos: {linea.strip()}")
                else:
                    archivo_salida.write(linea)

    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[!] Ejecución interrumpida por el usuario. Guardando progreso...")
        print(Fore.YELLOW + "El archivo ha sido procesado hasta el punto de la interrupción.")
        exit(0)
    except Exception as e:
        print(Fore.RED + f"Error: {str(e)}")
        exit(1)

# Llama a la función con los archivos de entrada y salida
input_file = "lista_de_canales.txt"  # Cambia este nombre por el archivo que quieras limpiar
output_file = "lista_de_canales_limpia.txt"
inactive_file = "canales_inactivos.txt"  # Archivo para canales inactivos
limpiar_lista(input_file, output_file, inactive_file)
print(Fore.CYAN + f"\nCanales activos guardados en: {output_file}")
print(Fore.CYAN + f"Canales inactivos guardados en: {inactive_file}")

print(Fore.CYAN + f"\nGITHUB OFICIAL: https://github.com/AAAAAEXQOSyIpN2JZ0ehUQ/IPTV-List-Checker")
