"""
Módulo: carga.py
Proyecto: GameSec Monitor - Taller de Programación I (UNAHUR)
Descripción: Carga y validación del archivo CSV de telemetría de servidores.
"""

def cargar_telemetria(ruta_archivo):
    # Verificar que el archivo exista antes de abrirlo
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"El archivo '{ruta_archivo}' no existe.")
    
    sesiones = []
    
    with open(ruta_archivo, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for nro_linea, fila in enumerate(reader, start=2):
            try:
                # Casteo de tipos para asegurar valores numéricos válidos
                sesion = {
                    "id_sesion": int(fila["id_sesion"]),
                    "servidor": fila["servidor"].strip(),
                    "jugador_id": fila["jugador_id"].strip(),
                    "tipo_partida": fila["tipo_partida"].strip(),
                    "ping_promedio": int(fila["ping_promedio"]),
                    "fps_promedio": int(fila["fps_promedio"]),
                    "duracion_minutos": float(fila["duracion_minutos"]),
                    "intentos_fallidos": int(fila["intentos_fallidos"]),
                    "reportes_trampa": int(fila["reportes_trampa"])
                }
                sesiones.append(sesion)
            except (ValueError, KeyError) as err:
                raise ValueError(f"Error en la línea {nro_linea} del CSV: {err}")
                
    if not sesiones:
        raise ValueError("El archivo CSV está vacío o no contiene registros válidos.")
        
    return sesiones


if __name__ == "__main__":
    print("--- Prueba de carga.py ---")
    ruta = "gamesec_logs.csv"
    if not os.path.exists(ruta) and os.path.exists("/workspace/knowledge/gamesec_logs.csv"):
        ruta = "/workspace/knowledge/gamesec_logs.csv"
        
    try:
        registros = cargar_telemetria(ruta)
        print(f"Cargados {len(registros)} registros correctamente.")
        print("Ejemplo primer registro:", registros[0])
    except Exception as e:
        print("Error al cargar:", e)
