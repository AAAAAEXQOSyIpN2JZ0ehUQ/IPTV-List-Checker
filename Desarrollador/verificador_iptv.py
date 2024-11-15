import requests
import concurrent.futures
import re
from datetime import datetime

# Colores para la terminal
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"

# Íconos para el reporte
ICON_ACTIVE = "✔️"
ICON_INACTIVE = "❌"

# Archivo de salida para canales activos
output_file = "lista_de_canales_limpia.txt"

# Extrae los canales del archivo m3u y verifica el estado de cada uno
def check_channel_status(channel_url):
    try:
        response = requests.head(channel_url, timeout=5)
        if response.status_code == 200:
            return channel_url, True
        else:
            return channel_url, False
    except requests.RequestException:
        return channel_url, False

def generate_html_report(channels):
    # Hora de generación de reporte
    report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Comienza la estructura HTML
    html = f"""
    <html>
    <head>
        <title>Reporte de Canales IPTV</title>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            .active {{ color: green; font-weight: bold; }}
            .inactive {{ color: red; font-weight: bold; }}
            h2 {{ color: #2c3e50; }}
            p {{ font-size: 1.1em; }}
        </style>
    </head>
    <body>
        <h1>Reporte de Canales IPTV</h1>
        <p>Generado el {report_time}</p>
        <table border="1" cellpadding="10" cellspacing="0">
            <tr>
                <th>Canal</th>
                <th>Estado</th>
            </tr>
    """
    
    # Itera sobre los canales y añade filas al HTML
    for url, status in channels:
        if status:
            html += f"""
                <tr class="active">
                    <td>{url}</td>
                    <td>{ICON_ACTIVE} Activo</td>
                </tr>
            """
        else:
            html += f"""
                <tr class="inactive">
                    <td>{url}</td>
                    <td>{ICON_INACTIVE} Inactivo</td>
                </tr>
            """
    
    html += """
        </table>
    </body>
    </html>
    """
    
    # Guarda el reporte en un archivo HTML
    with open("reporte_iptv.html", "w") as file:
        file.write(html)
    print(f"{CYAN}Reporte HTML generado: reporte_iptv.html{RESET}")

# Filtra URLs del archivo M3U y crea una lista
def extract_channels(file_path):
    with open(file_path, "r") as file:
        content = file.readlines()
    channels = [line.strip() for line in content if line.strip() and not line.startswith("#")]
    return channels

# Guarda los canales activos en un archivo de salida
def save_active_channels(channels):
    with open(output_file, "w") as file:
        for url, status in channels:
            if status:
                file.write(url + "\n")
    print(f"{CYAN}Canales activos guardados en: {output_file}{RESET}")

# Función principal
def main():
    print(f"{CYAN}Iniciando verificación de canales...{RESET}")
    
    # Extrae canales
    channels = extract_channels("lista.m3u")
    print(f"{YELLOW}Canales extraídos: {len(channels)}{RESET}")
    
    # Verificación concurrente con hilos
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {executor.submit(check_channel_status, url): url for url in channels}
        for future in concurrent.futures.as_completed(future_to_url):
            url, status = future.result()
            results.append((url, status))
            icon = ICON_ACTIVE if status else ICON_INACTIVE
            color = GREEN if status else RED
            print(f"{color}{icon} {url}{RESET}")
    
    # Genera reporte HTML y guarda canales activos
    generate_html_report(results)
    save_active_channels(results)

if __name__ == "__main__":
    main()
