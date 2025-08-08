import importlib.resources as pkg_resources
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict

from pandas.io.parquet import json

import emailify.resources as rsc
from emailify.models import Style, StyleProperty


def merge_styles(*styles: Style) -> Style:
    styles = list(filter(None, styles))
    if len(styles) == 0:
        return Style()
    _style = styles[0]
    for s in styles[1:]:
        _style = _style.merge(s)
    return _style


@lru_cache
def style_map() -> Dict[str, StyleProperty]:
    resources_path = Path(str(pkg_resources.files(rsc)))
    styles_path = resources_path / "styles.json"
    style_map = json.loads(styles_path.read_text())
    mappings = defaultdict(list)
    for key, mapped in style_map.items():
        cur = StyleProperty.from_mapping_key(key, mapped)
        mappings[cur.prop].append(cur)
    return mappings


def map_style(prop: str, value: Any) -> str:
    style_properties = style_map()
    if prop not in style_properties:
        return f"{prop.replace('_', '-')}:{value};"

    cur = style_properties[prop]
    for c in cur:
        if c.value == str(value):
            return c.render(value)

    cur = style_properties[prop]
    for c in cur:
        if c.value == "%s":
            return c.render(value) % value

    return ""


def render_style(style: Style) -> str:
    style_dict = style.model_dump(exclude_none=True)
    rendered = ""
    for prop, value in style_dict.items():
        rendered += map_style(prop, value)
    return rendered
