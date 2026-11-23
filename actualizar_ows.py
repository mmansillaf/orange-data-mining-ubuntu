#!/usr/bin/env python3
"""
Actualiza banco_pipeline.ows con la ruta absoluta pre-cargada en el widget File
"""
import base64
import io
import pickle
from pathlib import Path
from orangewidget.utils.filedialogs import RecentPath
from orangecanvas.scheme.readwrite import parse_ows_stream

OWS_PATH = Path("/home/usuario/Descargas/pycode/orange-project/banco_pipeline.ows")
TAB_PATH = Path("/home/usuario/Descargas/pycode/orange-project/banco_colas.tab").resolve()

# Serializar RecentPath para OWFile
rp = RecentPath(
    abspath=str(TAB_PATH),
    prefix="",
    relpath=TAB_PATH.name,
    title=TAB_PATH.name,
    file_format=None
)
node_props = {
    "recent_paths": [rp],
    "controlAreaVisible": True,
    "__version__": 1
}
pickled = pickle.dumps(node_props)
b64_props = base64.b64encode(pickled).decode("ascii")

xml_content = f"""<?xml version='1.0' encoding='utf-8'?>
<scheme version="2.0" title="Analisis Colas Banco">
\t<nodes>
\t\t<node id="0" name="File" qualified_name="Orange.widgets.data.owfile.OWFile" project_name="Orange3" version="" title="File" position="(60.0, 180.0)" />
\t\t<node id="1" name="Data Table" qualified_name="Orange.widgets.data.owtable.OWTable" project_name="Orange3" version="" title="Data Table" position="(260.0, 60.0)" />
\t\t<node id="2" name="Distributions" qualified_name="Orange.widgets.visualize.owdistributions.OWDistributions" project_name="Orange3" version="" title="Distributions" position="(260.0, 160.0)" />
\t\t<node id="3" name="Box Plot" qualified_name="Orange.widgets.visualize.owboxplot.OWBoxPlot" project_name="Orange3" version="" title="Box Plot" position="(260.0, 260.0)" />
\t\t<node id="4" name="Tree" qualified_name="Orange.widgets.model.owtree.OWTree" project_name="Orange3" version="" title="Tree" position="(260.0, 360.0)" />
\t\t<node id="5" name="Tree Viewer" qualified_name="Orange.widgets.visualize.owtreeviewer.OWTreeViewer" project_name="Orange3" version="" title="Tree Viewer" position="(440.0, 360.0)" />
\t</nodes>
\t<links>
\t\t<link id="0" source_node_id="0" sink_node_id="1" source_channel="Data" sink_channel="Data" enabled="true" />
\t\t<link id="1" source_node_id="0" sink_node_id="2" source_channel="Data" sink_channel="Data" enabled="true" />
\t\t<link id="2" source_node_id="0" sink_node_id="3" source_channel="Data" sink_channel="Data" enabled="true" />
\t\t<link id="3" source_node_id="0" sink_node_id="4" source_channel="Data" sink_channel="Data" enabled="true" />
\t\t<link id="4" source_node_id="4" sink_node_id="5" source_channel="Tree" sink_channel="Tree" enabled="true" />
\t</links>
\t<node_properties>
\t\t<properties node_id="0" format="pickle">{b64_props}</properties>
\t</node_properties>
</scheme>"""

stream = io.BytesIO(xml_content.encode("utf-8"))
parse_ows_stream(stream)
OWS_PATH.write_text(xml_content, encoding="utf-8")
print(f"[OK] banco_pipeline.ows actualizado con dataset pre-cargado: {TAB_PATH}")
