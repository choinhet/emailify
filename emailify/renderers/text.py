from emailify.models import Text
from emailify.renderers.core import _render
from emailify.renderers.style import render_style


def render_text(text: Text) -> str:
    return _render(
        "text",
        text=text,
        style=render_style(text.style),
        background_color=text.style.background_color or "transparent",
    )
