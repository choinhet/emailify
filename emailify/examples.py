from io import StringIO
from pathlib import Path

import pandas as pd

import emailify as ef


def sample_data():
    headers = [
        "Date",
        "Sessions",
        "Page Views",
        "Visitors",
        "Views Per User",
        "Average Session Duration (Seconds)",
        "Clicks",
        "Impressions",
        "CTR",
        "Average Search Position",
    ]
    data = "08/05/2025,100,200,300,1.2,100,200,200K,0.5%,20\n"
    all_data = "\n".join([data] * 50)
    return pd.read_csv(StringIO(f"""{",".join(headers)}\n{all_data} """))


def simple_table():
    df = sample_data()
    component = ef.Table(data=df)
    rendered = ef.render(component)
    Path("example.html").write_text(rendered)


def table_with_merged_headers():
    df = pd.DataFrame(
        {
            "hello2": [1, 2, 3],
            "hello": ["My", "Name", "Is"],
            "hello3": [1, 2, 3],
        }
    )
    df.rename(columns={"hello2": "hello"}, inplace=True)
    component = ef.Table(data=df, merge_equal_headers=True)
    rendered = ef.render(component)
    Path("example.html").write_text(rendered)


def table_hierarchy_styles():
    df = pd.DataFrame(
        {
            "super big column name, with a lot of text": [1, 2, 3],
            "hello": ["My", "Name", "Is"],
        }
    )
    component = ef.Table(
        data=df,
        header_style={
            "super big column name, with a lot of text": ef.Style(
                background="#000000", font_color="#ffffff"
            ),
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
    table_with_merged_headers()
