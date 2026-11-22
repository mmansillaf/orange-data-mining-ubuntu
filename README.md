# Orange Data Mining - Workspace Ubuntu 24.04

Entorno local aislado y configurado para Orange Data Mining 3.41+ sobre Ubuntu 24.04 LTS (Noble Numbat) con soporte nativo para Wayland y X11.

## 🚀 Inicio Rápido

### 1. Interfaz Gráfica (Orange Canvas)
Ejecutar el launcher:
```bash
./run.sh
```
O en segundo plano sin bloquear la terminal:
```bash
./run.sh > /dev/null 2>&1 &
```

También disponible desde el lanzador de aplicaciones de Ubuntu (`Super` -> buscar **Orange Data Mining**), configurado en `~/.local/share/applications/orange.desktop`.

### 2. Flujo Programático (Python Scripting)
Ejecutar el script de prueba integrado:
```bash
.venv/bin/python example.py
```

## 📦 Estructura del Proyecto

- `run.sh`: Script bash de arranque del entorno y lanzamiento de `Orange.canvas`.
- `example.py`: Pipeline básico de Machine Learning en Python (CrossValidation con Tree y RandomForest).
- `test_gui.py`: Validador automatizado de inicialización de ventanas Qt en Wayland.
- `requirements.txt`: Lista de dependencias principales.
- `pyproject.toml`: Manifiesto de empaquetado del proyecto.
- `.venv/`: Entorno virtual Python 3.12 gestionado con `uv`.
