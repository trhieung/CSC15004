from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import sqlite3

# Create your views here.

def index(request):
    print(sqlite3.sqlite_version)
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "index.html")