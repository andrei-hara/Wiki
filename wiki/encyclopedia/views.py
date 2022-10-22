from django.shortcuts import render
from markdown import Markdown

from . import util


def md_to_html(title):
    content = util.get_entry(title)
    markdown = Markdown()
    if content == None:
        return None
    else:
       return markdown.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, name):
    content = md_to_html(name)
    if content == None:
         return render(request, "encyclopedia/none.html",{
            "message" : "Invalid page"
         })
    else:
        return render(request, "encyclopedia/entrypage.html", {
            "title": name,
            "page": content
    })

