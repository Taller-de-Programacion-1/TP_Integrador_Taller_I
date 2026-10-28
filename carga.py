"""
Módulo: carga.py
Descripción: Encargado de la lectura, tipado explícito y validación
             del archivo CSV de telemetría de servidores (gamesec_logs.csv).
Uso: Librería estándar de Python (csv, os). Sin librerías externas.
"""

import csv
import os

def cargar_telemetria(ruta_archivo: str) -> list[dict]:
    """
    Lee el archivo CSV de registros de telemetría y convierte cada campo
    a su tipo de dato correspondiente.
    
    Parámetros:
        ruta_archivo (str): Ruta relativa o absoluta del archivo CSV.
        
    Retorna:
        list[dict]: Lista de diccionarios donde cada elemento es una sesión.
        
    Excepciones:
        FileNotFoundError: Si la ruta especificada no existe.
        ValueError: Si el archivo está vacío o tiene formato inválido.
    """
    # 1. Validación de existencia del archivo
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"Error: El archivo '{ruta_archivo}' no existe.")
    
    sesiones = []
    
    # 2. Apertura segura con 'with' en codificación UTF-8
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo_csv:
        lector_dict = csv.DictReader(archivo_csv)
        
        # 3. Recorrido fila por fila con conversión explícita de tipos (casteo)
        for num_fila, fila in enumerate(lector_dict, start=2):
            try:
                sesion_convertida = {
                    "id_sesion": int(fila["id_sesion"]),
                    "servidor": str(fila["servidor"]).strip(),
                    "jugador_id": str(fila["jugador_id"]).strip(),
                    "tipo_partida": str(fila["tipo_partida"]).strip(),
                    "ping_promedio": int(fila["ping_promedio"]),
                    "fps_promedio": int(fila["fps_promedio"]),
                    "duracion_minutos": float(fila["duracion_minutos"]),
                    "intentos_fallidos": int(fila["intentos_fallidos"]),
                    "reportes_trampa": int(fila["reportes_trampa"])
                }
                sesiones.append(sesion_convertida)
                
            except (ValueError, KeyError) as e:
                raise ValueError(f"Error de formato en la línea {num_fila} del CSV: {e}")
                
    # 4. Validación de contenido no vacío
    if not sesiones:
        raise ValueError("Error: El archivo CSV está vacío o no contiene registros válidos.")
        
    return sesiones


# Bloque de prueba individual para ejecución en VS Code
if __name__ == "__main__":
    print("--- Prueba unitaria de carga.py ---")
    try:
        datos = cargar_telemetria("gamesec_logs.csv")
        print(f"Carga exitosa. Total de registros cargados: {len(datos)}")
        print("Ejemplo del primer registro:", datos)
    except Exception as err:
        print("Error en la carga:", err)