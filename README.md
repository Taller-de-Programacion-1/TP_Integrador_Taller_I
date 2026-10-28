# 🎮 GAME SEC MONITOR v1.0

> **Plataforma de Telemetría de Servidores & Motor Heurístico de Ciberseguridad**  
> *Universidad Nacional de Hurlingham (UNAHUR) — Taller de Programación I*

```text
   ______ ___    __  ___ ______ _____ ______ ______
  / ____//   |  /  |/  // ____// ___// ____// ____/
 / / __ / /| | / /|_/ // __/   \__ \/ __/  / /     
/ /_/ // ___ |/ /  / // /___  ___/ / /___ / /___   
\____//_/  |_/_/  /_//_____/ /____/_____/ \____/   

          [ SYSTEM STATUS: ONLINE // THREAT ENGINE: ACTIVE ]

---

🛰️**Visión General del Sistema**

GameSec Monitor es una plataforma de consola desarrollada en Python puro diseñada para auditar la salud operativa de la infraestructura de servidores multijugador y detectar amenazas cibernéticas en tiempo real (como ataques de fuerza bruta en inicio de sesión o uso indebido de trampas/hacks).
El sistema opera bajo la restricción estricta de cero librerías externas, procesando directamente la telemetría enviada por los nodos distribuidos (gamesec_logs.csv).

⚙️ **Arquitectura Modular**

La solución está construida sobre una arquitectura desacoplada de 3 capas:
carga.py: Motor de ingesta con validación de archivos y casteo explícito de tipos (int, float, str).
procesamiento.py: Núcleo analítico. Incluye diccionario acumulador dinámico para servidores y el motor heurístico de ciberseguridad.
main.py: Interfaz de línea de comandos (CLI) interactiva y generador del informe de auditoría consolidado.

Arquitectura desacoplada de 3 capas:

              ┌────────────────────────┐
              │    gamesec_logs.csv    │
              └───────────┬────────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │       carga.py       │ ──► Parseo & Casteo
               └──────────┬───────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │   procesamiento.py   │ ──► Métricas & Heurística
               └──────────┬───────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │       main.py        │ ──► Menu CLI & Exportación
               └──────────┬───────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │  reporte_gamesec.txt   │
              └────────────────────────┘
---

## 🛡️ Motor Heurístico de Ciberseguridad

Cada sesión de juego procesada por **GameSec Monitor** es analizada mediante un árbol de decisión heurístico para categorizar el nivel de amenaza:

| Nivel de Alerta | Criterio de Activación Heurística | Diagnóstico Operativo |
| :--- | :--- | :--- |
| 🔴 **CRÍTICO** | `reportes_trampa >= 3` **O** `intentos_fallidos >= 4` | Detección de cheats/hacks o ataque de fuerza bruta |
| 🟡 **SOSPECHOSO** | (`ping > 200` **Y** `intentos_fallidos >= 2`) **O** (`reportes_trampa == 2`) | Inestabilidad de red anómala o comportamiento atípico |
| 🟢 **NORMAL** | No cumple las condiciones de sospechoso ni crítico | Sesión operativa limpia |

---


🚀**Instalación y Ejecución**

Prerrequisitos
Python 3.10 o superior (sin necesidad de pip install, requiere únicamente la librería estándar).
Git y Visual Studio Code.

Despliegue Local

# 1. Clonar el repositorio
git clone https://github.com/Taller-de-Programacion-1/TP_Integrador_Taller_I.git

# 2. Ingresar al directorio del proyecto
cd TP_Integrador_Taller_I

# 3. Ejecutar el sistema principal

python main.

🧪 **Pruebas Unitarias de Módulos**

Para auditar componentes individuales antes de la compilación final:

# Probar ingesta y validación CSV
python carga.py

# Probar algoritmos de procesamiento y seguridad
python procesamiento.py

📊 **Dataset & Telemetría Analizada**

Registros Procesados: 150 sesiones de juego.
Servidores Monitoreados: SA-BuenosAires, EU-Frankfurt, NA-Virginia, SA-SaoPaulo.
Métricas Principales: Ping Promedio (ms), FPS Promedio, Duración de Partida (min), Intentos de Login Fallidos, Reportes por Trampa.

👨‍💻 **Escuadrón de Desarrollo (UNAHUR)**

* Karina Parra, Licenciatura en Ciberseguridad
* Integrante 2
* Integrante 3
* Integrante 4
* Integrante 5
* Integrante 6

*GameSec Monitor v1.0 — Proyecto Integrador Taller de Programación I (UNAHUR)*