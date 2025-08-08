from mjml import mjml2html

from emailify.models import Component, Table
from emailify.renderers.core import _render
from emailify.renderers.table import render_table

RENDER_MAP = {
    Table: render_table,
}


def render(*components: Component) -> str:
    body_str = ""
    for component in components:
        if type(component) not in RENDER_MAP:
            raise ValueError(f"Component {type(component)} not supported")
        body_str += RENDER_MAP[type(component)](component) + "<br/>"

    body_str = _render("index", content=body_str)
    return mjml2html(body_str)
