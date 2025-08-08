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
    component = ef.Table(data=df)
    rendered = ef.render(component, component)

    Path("example.html").write_text(rendered)


if __name__ == "__main__":
    simple_table()
