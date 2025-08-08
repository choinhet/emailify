from pathlib import Path

import pandas as pd

import emailify as ef


def simple_table():
    df = pd.DataFrame(
        {
            "testing": [1, 2, 3],
            "hello": ["My", "Name", "Is"],
        }
    )
    component = ef.Table(
        data=df,
        header_style={
            "testing": ef.Style(background="#000000", font_color="#ffffff"),
        },
        column_style={
            "hello": ef.Style(background="#d0d0d0", bold=True),
        },
        row_style={
            1: ef.Style(background="#cbf4c9", bold=True),
        },
    )
    rendered = ef.render(component, component)

    Path("example.html").write_text(rendered)


if __name__ == "__main__":
    simple_table()
