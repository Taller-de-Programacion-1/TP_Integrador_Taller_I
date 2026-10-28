GameSec Monitor: Telemetría de Servidores de Videojuegos y Detección de Incidentes
Taller de Programación I (Ciclo Lectivo 2026)
Universidad Nacional de Hurlingham — Instituto de Tecnología e Ingeniería

👥 Integrantes del Equipo
Nombre y Apellido: xxx| DNI: xxx 
Nombre y Apellido: xxx| DNI: xxx 
Nombre y Apellido: xxx| DNI: xxx 
Nombre y Apellido: xxx| DNI: xxx 
Nombre y Apellido: xxx| DNI: xxx 
Nombre y Apellido: xxx| DNI: xxx 

🛠️ Arquitectura del Proyecto
El sistema está desarrollado bajo el paradigma modular en Python 3.10+, utilizando exclusivamente la librería estándar (csv, math, os, datetime), sin dependencias externas como Pandas o NumPy.

gamesec_monitor/
├── carga.py             # Lectura, casteo explícito de tipos y validación del CSV
├── procesamiento.py     # Estadísticas globales, acumuladores por servidor y motor de reglas
├── main.py              # Interfaz de consola interactiva (menú) y exportación del reporte
├── gamesec_logs.csv     # Dataset con 150 registros de telemetría
└── README.md            # Documentación y datos del grupo

🚀 Instrucciones de Ejecución
Abrir la terminal o el entorno de Visual Studio Code en la carpeta raíz del proyecto.
Ejecutar el script principal con el siguiente comando:
python main.py
Utilizar el menú interactivo para navegar por las opciones:
1: Cargar el dataset gamesec_logs.csv.
2: Consultar métricas globales del sistema.
3: Analizar rendimiento agrupado por servidor.
4: Auditar sesiones sospechosas y críticas.
5: Generar el informe reporte_gamesec.txt.
6: Salir.