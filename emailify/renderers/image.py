from pathlib import Path

from emailify.models import Image
from emailify.renderers.core import _render
from emailify.renderers.style import render_style


def render_image(image: Image) -> str:
    src = str(Path(image.path))
    return _render(
        "image",
        image=image,
        src=src,
        style=render_style(image.style),
    )
