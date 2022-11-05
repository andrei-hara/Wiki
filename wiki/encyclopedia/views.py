from django.shortcuts import render
from markdown import Markdown
import random

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


def search(request):
    entry_list = []
    all_entries = util.list_entries()

    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = md_to_html(entry_search)    

        for entry in all_entries:
            if entry_search.lower() in entry.lower():
                entry_list.append(entry)

        if html_content:
            return render(request, "encyclopedia/entrypage.html", {
            "title": entry_search,
            "page": html_content
            })
        elif entry_list:
             return render(request, "encyclopedia/entries.html", {
            "entries": entry_list
            })
        else:
            return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
            })


def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if  titleExist is not None:
            return render(request, "encyclopedia/none.html",{
                "message" : "Page already exists."
            })
        else:
            util.save_entry(title, content)
            html_content = md_to_html(title)
            return render(request, "encyclopedia/entrypage.html", {
            "title": title,
            "page": html_content
            })


def edit_page_init(request):
    if request.method == "POST":
        title = request.POST['title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit_page.html",{
            "title" : title,
            "content" : content
        })
    elif request.method == "GET":
        title = request.GET['title']
        content = request.GET['content']
        util.save_entry(title, content)
        html_content = md_to_html(title)
        return render(request, "encyclopedia/entrypage.html", {
            "title": title,
            "page": html_content
            })


def random_page(request):
    all_entries = util.list_entries()
    random_entry = random.choice(all_entries)
    random_page = md_to_html(random_entry)

    return render(request, "encyclopedia/entrypage.html", {
            "title": random_entry,
            "page": random_page
            })
