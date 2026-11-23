# Checkpoint de Estado: Proyecto Orange Data Mining

**Fecha de guardado**: 2026-11-23 11:44:00  
**Ruta del proyecto**: `/home/usuario/Descargas/pycode/orange-project`  
**Entorno Virtual**: `/home/usuario/Descargas/pycode/orange-project/.venv`

---

## 1. Inventario de Archivos y Estado Actual

| Archivo | Tipo | Propósito / Descripción |
| :--- | :--- | :--- |
| `banco_colas.csv` | Dataset | 1,200 registros de transacciones bancarias simuladas. |
| `banco_colas.tab` | Dataset | Formato nativo de Orange con tipado (`continuous`/`discrete`) y metadatos de clase. |
| `banco_pipeline.ows` | Flujo Orange | Pipeline visual completo (`File` -> `Data Table`, `Distributions`, `Box Plot`, `Tree` -> `Tree Viewer`) con ruta absoluta embebida. |
| `pipeline_mvp.ows` | Flujo Orange | Flujo canónico MVP de clasificación validado. |
| `infografia_banco.png` | Imagen | Panel de diagnóstico 2x2 en 150 DPI (esperas horarias, fuga, tiempos por trámite y reglas). |
| `generar_caso_banco.py` | Script | Generador determinista del dataset bancario, entrenamiento de árbol en Orange y render de infografía. |
| `build_workflow.py` | Script | Validador y generador de esquemas XML `.ows` usando `orangecanvas.scheme.readwrite`. |
| `actualizar_ows.py` | Script | Inyector de configuración para pre-cargar datasets en nodos `File` de Orange. |
| `run.sh` | Shell Script | Lanzador del entorno virtual y de Orange Canvas. |

---

## 2. Instrucciones para Reanudar tras el Reinicio

### A. Abrir Orange Canvas con el Flujo Bancario Directamente
```bash
/home/usuario/Descargas/pycode/orange-project/run.sh /home/usuario/Descargas/pycode/orange-project/banco_pipeline.ows
```

### B. Ejecutar el Entorno Virtual Manualmente
```bash
source /home/usuario/Descargas/pycode/orange-project/.venv/bin/activate
orange-canvas /home/usuario/Descargas/pycode/orange-project/banco_pipeline.ows
```

### C. Re-generar o Re-entrenar Modelos
```bash
/home/usuario/Descargas/pycode/orange-project/.venv/bin/python /home/usuario/Descargas/pycode/orange-project/generar_caso_banco.py
```

---

## 3. Artefactos del Sistema
- Informe y análisis ejecutivo: `/home/usuario/.gemini/antigravity-cli/brain/64a0ce6e-4e18-4940-8f9a-a75543b5c2e1/informe_colas_banco.md`
- Imagen de infografía respaldada: `/home/usuario/.gemini/antigravity-cli/brain/64a0ce6e-4e18-4940-8f9a-a75543b5c2e1/infografia_banco.png`
