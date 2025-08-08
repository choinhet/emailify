from emailify.models import Style


def merge_styles(*styles: Style) -> Style:
    styles = list(filter(None, styles))
    if len(styles) == 0:
        return Style()
    _style = styles[0]
    for s in styles[1:]:
        _style.merge(s)
    return _style
