import io
import shutil
from io import StringIO
from pathlib import Path

import matplotlib.pyplot as plt
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
    html, _attachments = ef.render(component)
    Path("example.html").write_text(html)


def table_with_merged_headers():
    buf = io.BytesIO()
    plt.plot([1, 2, 3], [2, 4, 1])
    plt.tight_layout()
    plt.savefig(buf, format="png", dpi=150)
    temp_path = Path("temp")
    temp_path.mkdir(exist_ok=True)
    img = temp_path / "image.png"
    plt.savefig(img, format="png", dpi=150)
    plt.close()
    buf.seek(0)

    df = pd.DataFrame(
        {
            "hello2": [1, 2, 3],
            "hello": [
                "My",
                ef.Link(text="Google", href="https://www.google.com"),
                "Is",
            ],
            "Really long column name": [1, 2, 3],
            "hello3": [1, 2, 3],
        }
    )
    df.rename(columns={"hello2": "hello"}, inplace=True)
    html, _attachments = ef.render(
        ef.Text(
            text="Hello, this is a table with merged headers",
            style=ef.Style(background_color="#cbf4c9", padding_left="5px"),
        ),
        ef.Link(text="Hello", href="https://www.google.com"),
        ef.Table(
            data=df,
            merge_equal_headers=True,
            header_style={
                "hello": ef.Style(
                    background_color="#000000",
                    font_color="#ffffff",
                ),
                "hello3": ef.Style(
                    font_family="unknown",
                ),
            },
            column_style={
                "hello3": ef.Style(background_color="#0d0d0", bold=True),
            },
            row_style={
                1: ef.Style(background_color="#cbf4c9", bold=True),
            },
            column_widths={
                "hello": 10,
            },
        ),
        ef.Fill(style=ef.Style(background_color="#cbf4c9")),
        ef.Image(data=img, format="png", width="600px"),
        ef.Image(data=buf, format="png", width="600px"),
        ef.Table(data=df).with_stripes(),
    )
    shutil.rmtree(temp_path, ignore_errors=True)
    Path("example.html").write_text(html)


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
                background_color="#000000", font_color="#ffffff"
            ),
        },
        column_style={
            "hello": ef.Style(background_color="#d0d0d0", bold=True),
        },
        row_style={
            1: ef.Style(background_color="#cbf4c9", bold=True),
        },
    )
    html, _attachments = ef.render(component, component)

    Path("example.html").write_text(html)


if __name__ == "__main__":
    table_with_merged_headers()
