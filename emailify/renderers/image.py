from base64 import b64encode
from pathlib import Path

from emailify.models import Graph, Image
from emailify.renderers.core import _render
from emailify.renderers.style import merge_styles, render_extra_props, render_style
from emailify.styles.image_default import IMAGE_STYLE


def _as_data_uri(content: bytes, mime: str) -> str:
    return f"data:{mime};base64,{b64encode(content).decode('ascii')}"


def render_image(image: Image) -> str:
    src = str(Path(image.path))
    image._render(
        "image",
        image=image,
        src=src,
        style=render_style(image.style),
        extra_props=render_extra_props("image", image.style),
    )


def render_graph(graph: Graph) -> str:
    if isinstance(graph.data, (bytes, bytearray)):
        mime = "image/svg+xml" if graph.format == "svg" else f"image/{graph.format}"
        src = _as_data_uri(graph.data, mime)
    elif isinstance(graph.data, Path):
        src = str(Path(graph.data))
    else:
        raise ValueError("Graph.data must be bytes or a Path-like")

    cur_style = merge_styles(IMAGE_STYLE, graph.style)
    return _render(
        "image",
        image=graph,
        src=src,
        style=render_style(cur_style),
        extra_props=render_extra_props(
            "image", cur_style, {"width": graph.width, "height": graph.height}
        ),
    )
