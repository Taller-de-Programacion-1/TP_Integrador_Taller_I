"""
Módulo: procesamiento.py
Proyecto: GameSec Monitor - Taller de Programación I (UNAHUR)
Descripción: Funciones de procesamiento de datos, métricas y motor heurístico.
"""

def calcular_estadisticas_globales(sesiones):
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
    competitivas = 0
    
    for s in sesiones:
        suma_ping += s["ping_promedio"]
        suma_duracion += s["duracion_minutos"]
        if s["tipo_partida"] in ["Competitiva", "Torneo"]:
            competitivas += 1
            
    ping_prom = round(suma_ping / total, 2)
    duracion_prom = round(suma_duracion / total, 2)
    pct_comp = round((competitivas / total) * 100, 2)
    
    return {
        "total_sesiones": total,
        "ping_promedio": ping_prom,
        "duracion_promedio": duracion_prom,
        "porcentaje_competitivas": pct_comp
    }


def analizar_por_servidor(sesiones):
    # Diccionario acumulador para agrupar dinámicamente por servidor
    acum = {}
    
    for s in sesiones:
        srv = s["servidor"]
        if srv not in acum:
            acum[srv] = {
                "cantidad": 0,
                "suma_ping": 0,
                "suma_fps": 0
            }
        
        acum[srv]["cantidad"] += 1
        acum[srv]["suma_ping"] += s["ping_promedio"]
        acum[srv]["suma_fps"] += s["fps_promedio"]
        
    # Calcular promedios finales
    resultado = {}
    for srv, datos in acum.items():
        cant = datos["cantidad"]
        resultado[srv] = {
            "cantidad": cant,
            "ping_promedio": round(datos["suma_ping"] / cant, 2),
            "fps_promedio": round(datos["suma_fps"] / cant, 2)
        }
        
    return resultado


def clasificar_incidentes(sesiones):
    # Motor heurístico para clasificar eventos de seguridad
    frecuencias = {"Normal": 0, "Sospechoso": 0, "Crítico": 0}
    eventos_criticos = []
    
    for s in sesiones:
        rep = s["reportes_trampa"]
        intentos = s["intentos_fallidos"]
        ping = s["ping_promedio"]
        
        # Regla 1: Nivel Crítico
        if rep >= 3 or intentos >= 4:
            frecuencias["Crítico"] += 1
            
            if rep >= 3 and intentos >= 4:
                motivo = f"Ataque de fuerza bruta ({intentos} intentos) y reportes de trampa ({rep})"
            elif intentos >= 4:
                motivo = f"Ataque de fuerza bruta en login ({intentos} intentos fallidos)"
            else:
                motivo = f"Múltiples reportes por uso de trampas ({rep} reportes)"
                
            eventos_criticos.append({
                "id_sesion": s["id_sesion"],
                "jugador_id": s["jugador_id"],
                "servidor": s["servidor"],
                "motivo": motivo
            })
            
        # Regla 2: Nivel Sospechoso
        elif (ping > 200 and intentos >= 2) or (rep == 2):
            frecuencias["Sospechoso"] += 1
            
        # Regla 3: Nivel Normal
        else:
            frecuencias["Normal"] += 1
            
    return frecuencias, eventos_criticos


if __name__ == "__main__":
    import os
    import carga
    print("--- Prueba de procesamiento.py ---")
    ruta = "gamesec_logs.csv"
    if not os.path.exists(ruta) and os.path.exists("/workspace/knowledge/gamesec_logs.csv"):
        ruta = "/workspace/knowledge/gamesec_logs.csv"
        
    try:
        datos = carga.cargar_telemetria(ruta)
        stats = calcular_estadisticas_globales(datos)
        print("Stats globales:", stats)
        srvs = analizar_por_servidor(datos)
        print("Por servidor:", srvs)
        frec, crit = clasificar_incidentes(datos)
        print("Incidentes:", frec)
    except Exception as e:
        print("Error:", e)
