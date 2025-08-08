from typing import Dict

from emailify.models import Table
from emailify.renderers.core import _render
from emailify.renderers.style import merge_styles, render_style
from emailify.styles.table_default import COL_STYLE, HEADER_STYLE


def render_table(table: Table) -> str:
    row_styles: Dict[int, str] = {}
    header_styles: Dict[str, str] = {}
    col_styles: Dict[str, str] = {}

    for header in table.data.columns:
        header_styles[header] = render_style(
            merge_styles(
                HEADER_STYLE,
                table.header_style.get(header),
            )
        )

    for col in table.data.columns:
        col_styles[col] = render_style(
            merge_styles(
                COL_STYLE,
                table.column_style.get(col),
            )
        )

    body_style = render_style(
        merge_styles(
            table.body_style,
        )
    )

    for idx in range(table.data.shape[0]):
        row_styles[idx] = render_style(merge_styles(table.row_style.get(idx)))

    return _render(
        "table",
        table=table,
        header_styles=header_styles,
        col_styles=col_styles,
        row_styles=row_styles,
        body_style=body_style,
    )
