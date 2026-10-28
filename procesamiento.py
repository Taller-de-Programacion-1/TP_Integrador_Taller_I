"""
Módulo: procesamiento.py
Descripción: Contiene las funciones puras de análisis estadístico,
             agrupamiento dinámico por servidor y clasificación heurística de incidentes.
Uso: Librería estándar de Python. Sin Pandas ni NumPy.
"""

def calcular_estadisticas_globales(sesiones: list[dict]) -> dict:
    """
    Calcula el panorama estadístico general de todas las sesiones registradas.
    
    Retorna un diccionario con las claves exactas requeridas:
    'total_sesiones', 'ping_promedio', 'duracion_promedio', 'porcentaje_competitivas'.
    """
    total = len(sesiones)
    if total == 0:
        return {
            "total_sesiones": 0,
            "ping_promedio": 0.0,
            "duracion_promedio": 0.0,
            "porcentaje_competitivas": 0.0
        }
        
    suma_ping = 0
    suma_duracion = 0
    conteo_competitivas = 0
    
    for s in sesiones:
        suma_ping += s["ping_promedio"]
        suma_duracion += s["duracion_minutos"]
        
        # Considera modalidades 'Competitiva' o 'Torneo' como alta competencia
        if s["tipo_partida"] in ["Competitiva", "Torneo"]:
            conteo_competitivas += 1
            
    ping_prom = round(suma_ping / total, 2)
    duracion_prom = round(suma_duracion / total, 2)
    porcentaje_comp = round((conteo_competitivas / total) * 100, 2)
    
    return {
        "total_sesiones": total,
        "ping_promedio": ping_prom,
        "duracion_promedio": duracion_prom,
        "porcentaje_competitivas": porcentaje_comp
    }


def analizar_por_servidor(sesiones: list[dict]) -> dict:
    """
    Agrupa los datos por región de servidor aplicando el patrón de diccionario
    acumulador dinámico (sin hardcodear nombres de servidores).
    """
    acumuladores = {}
    
    for s in sesiones:
        srv = s["servidor"]
        if srv not in acumuladores:
            acumuladores[srv] = {
                "cantidad": 0,
                "suma_ping": 0,
                "suma_fps": 0
            }
            
        acumuladores[srv]["cantidad"] += 1
        acumuladores[srv]["suma_ping"] += s["ping_promedio"]
        acumuladores[srv]["suma_fps"] += s["fps_promedio"]
        
    resultado = {}
    for srv, datos in acumuladores.items():
        cant = datos["cantidad"]
        resultado[srv] = {
            "cantidad": cant,
            "ping_promedio": round(datos["suma_ping"] / cant, 2),
            "fps_promedio": round(datos["suma_fps"] / cant, 2)
        }
        
    return resultado


def clasificar_incidentes(sesiones: list[dict]) -> tuple[dict, list[dict]]:
    """
    Motor heurístico de ciberseguridad. Evalúa cada sesión según reglas
    determinísticas para clasificarla en NORMAL, SOSPECHOSO o CRÍTICO.
    
    Retorna:
        tuple: (frecuencias_dict, lista_eventos_criticos)
    """
    frecuencias = {"Normal": 0, "Sospechoso": 0, "Crítico": 0}
    eventos_criticos = []
    
    for s in sesiones:
        reportes = s["reportes_trampa"]
        intentos = s["intentos_fallidos"]
        ping = s["ping_promedio"]
        
        # Regla 1: CRÍTICO
        if reportes >= 3 or intentos >= 4:
            frecuencias["Crítico"] += 1
            
            if reportes >= 3 and intentos >= 4:
                motivo = f"Exceso de reportes por trampa ({reportes}) e intentos fallidos ({intentos})"
            elif intentos >= 4:
                motivo = f"Ataque de fuerza bruta en login ({intentos} intentos fallidos)"
            else:
                motivo = f"Exceso de denuncias por trampas/hacks ({reportes} reportes)"
                
            eventos_criticos.append({
                "id_sesion": s["id_sesion"],
                "jugador_id": s["jugador_id"],
                "servidor": s["servidor"],
                "motivo": motivo
            })
            
        # Regla 2: SOSPECHOSO
        elif (ping > 200 and intentos >= 2) or (reportes == 2):
            frecuencias["Sospechoso"] += 1
            
        # Regla 3: NORMAL
        else:
            frecuencias["Normal"] += 1
            
    return frecuencias, eventos_criticos


# Bloque de prueba individual para ejecución en VS Code
if __name__ == "__main__":
    import carga
    print("--- Prueba unitaria de procesamiento.py ---")
    datos = carga.cargar_telemetria("gamesec_logs.csv")
    print("Métricas globales:", calcular_estadisticas_globales(datos))
    print("Análisis por servidor:", analizar_por_servidor(datos))
    frec, crit = clasificar_incidentes(datos)
    print("Distribución de incidentes:", frec)
    print("Total de eventos críticos:", len(crit))
