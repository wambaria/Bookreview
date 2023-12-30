"""from django.shortcuts import render

def index(request):
    name = "world"
    return render(request, "base.html", {"name":name})

def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-results.html", {"search_text":search_text})"""

from django.http import HttpResponse
from .models import Book

def welcome_view(request):
    message = f"<html><h1>Welcome to Bookreview</h1>
    <p>{Book.objects.count()} books and counting</p></html>"
    return HttpResponse(message)