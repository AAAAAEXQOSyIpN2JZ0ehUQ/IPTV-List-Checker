# Abrir el archivo M3U y leer el contenido
with open("lista_de_canales_limpia.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

# Lista para almacenar las líneas que contienen URLs
canales_con_url = []

# Iterar sobre las líneas del archivo
for i in range(len(lineas)):
    # Si la línea comienza con #EXTINF y la siguiente línea tiene una URL, la guardamos
    if lineas[i].startswith("#EXTINF") and i + 1 < len(lineas) and lineas[i + 1].startswith("http"):
        canales_con_url.append(lineas[i].strip())  # Agregar #EXTINF
        canales_con_url.append(lineas[i + 1].strip())  # Agregar la URL correspondiente

# Guardar las líneas filtradas en un nuevo archivo
with open("lista_de_canales_limpia_filtrada.txt", "w", encoding="utf-8") as archivo_salida:
    archivo_salida.write("\n".join(canales_con_url))

print("El proceso ha terminado, solo se guardaron las entradas con URL.")
