from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def richtext(value):
    """Plain text → HTML. Blank line = new paragraph; lines starting with '- ' = bullet list.
    Everything is HTML-escaped first, so it is safe for text typed into the admin."""
    if not value:
        return ""
    html = []
    for block in str(value).replace("\r\n", "\n").split("\n\n"):
        lines = [ln.strip() for ln in block.strip().split("\n") if ln.strip()]
        if not lines:
            continue
        para, items = [], []
        for ln in lines:
            if ln.startswith("- "):
                if para:
                    html.append("<p>" + " ".join(para) + "</p>")
                    para = []
                items.append("<li>" + escape(ln[2:]) + "</li>")
            else:
                if items:
                    html.append("<ul>" + "".join(items) + "</ul>")
                    items = []
                para.append(escape(ln))
        if para:
            html.append("<p>" + " ".join(para) + "</p>")
        if items:
            html.append("<ul>" + "".join(items) + "</ul>")
    return mark_safe("".join(html))
