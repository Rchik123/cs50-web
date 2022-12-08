from django.shortcuts import render
from django import forms

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def search(request):
    if request.method == "GET":
        title = request.GET.get("q")
        entry = util.get_entry(title)
        if entry is None:
            titles = []
            entries = util.list_entries()
            for e in entries:
                if e.__contains__(title):
                    titles.append(e)
            return render(request, "encyclopedia/searchnf.html", {
                "titles": titles
            })
        else:
            return render(request, "encyclopedia/entry.html", {
                "entry": entry,
                "title": input
        })
        

def entry(request, title):
    entry = util.get_entry(title)
    if entry is None:
        return render(request, "encyclopedia/entrynf.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": entry,
            "title": title
        })
    