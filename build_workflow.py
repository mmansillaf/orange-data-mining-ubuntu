#!/usr/bin/env python3
"""
Orange Workflow Builder & Validator (MVP)
Genera y valida flujos visuales .ows de forma determinista para Orange Canvas.
"""
import io
import os
import sys
from pathlib import Path
from orangecanvas.scheme.readwrite import parse_ows_stream

def generate_classification_pipeline_ows(title: str = "Pipeline Clasificación Auto-Generado") -> str:
    """Genera el XML de un flujo canónico: File -> Table, Distributions, Tree -> Tree Viewer."""
    return f"""<?xml version='1.0' encoding='utf-8'?>
<scheme version="2.0" title="{title}">
\t<nodes>
\t\t<node id="0" name="File" qualified_name="Orange.widgets.data.owfile.OWFile" project_name="Orange3" version="" title="File" position="(80.0, 180.0)" />
\t\t<node id="1" name="Data Table" qualified_name="Orange.widgets.data.owtable.OWTable" project_name="Orange3" version="" title="Data Table" position="(260.0, 80.0)" />
\t\t<node id="2" name="Distributions" qualified_name="Orange.widgets.visualize.owdistributions.OWDistributions" project_name="Orange3" version="" title="Distributions" position="(260.0, 180.0)" />
\t\t<node id="3" name="Tree" qualified_name="Orange.widgets.model.owtree.OWTree" project_name="Orange3" version="" title="Tree" position="(260.0, 280.0)" />
\t\t<node id="4" name="Tree Viewer" qualified_name="Orange.widgets.visualize.owtreeviewer.OWTreeViewer" project_name="Orange3" version="" title="Tree Viewer" position="(440.0, 280.0)" />
\t</nodes>
\t<links>
\t\t<link id="0" source_node_id="0" sink_node_id="1" source_channel="Data" sink_channel="Data" enabled="true" />
\t\t<link id="1" source_node_id="0" sink_node_id="2" source_channel="Data" sink_channel="Data" enabled="true" />
\t\t<link id="2" source_node_id="0" sink_node_id="3" source_channel="Data" sink_channel="Data" enabled="true" />
\t\t<link id="3" source_node_id="3" sink_node_id="4" source_channel="Tree" sink_channel="Tree" enabled="true" />
\t</links>
</scheme>"""

def validate_and_save(xml_content: str, output_path: str) -> bool:
    """Valida el esquema con orangecanvas parser y lo persiste a disco."""
    stream = io.BytesIO(xml_content.encode("utf-8"))
    try:
        parsed = parse_ows_stream(stream)
        path = Path(output_path).resolve()
        path.write_text(xml_content, encoding="utf-8")
        print(f"[OK] Flujo válido generado en: {path}")
        print(f"     Nodos: {len(parsed.nodes)} | Enlaces: {len(parsed.links)}")
        return True
    except Exception as e:
        print(f"[ERROR] Error de validación de esquema: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "/home/usuario/Descargas/pycode/orange-project/pipeline_mvp.ows"
    xml = generate_classification_pipeline_ows()
    if not validate_and_save(xml, target):
        sys.exit(1)
