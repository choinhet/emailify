from mjml import mjml2html

from emailify.models import Component, Fill, Graph, Image, Table, Text
from emailify.renderers.core import _render
from emailify.renderers.fill import render_fill
from emailify.renderers.image import render_graph, render_image
from emailify.renderers.table import render_table
from emailify.renderers.text import render_text

RENDER_MAP = {
    Table: render_table,
    Text: render_text,
    Fill: render_fill,
    Image: render_image,
    Graph: render_graph,
}


def render(
    *components: Component,
) -> str:
    parts: list[str] = []
    for component in components:
        if type(component) not in RENDER_MAP:
            raise ValueError(f"Component {type(component)} not supported")
        parts.append(RENDER_MAP[type(component)](component))

    body_str = _render(
        "index",
        content="".join(parts),
    )
    return mjml2html(body_str)
