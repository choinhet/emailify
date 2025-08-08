from emailify.models import Fill
from emailify.renderers.core import _render


def render_fill(fill: Fill) -> str:
    return _render(
        "fill",
        fill=fill,
        height=fill.height,
        width=fill.width,
        background_color=fill.style.background_color or "transparent",
    )
