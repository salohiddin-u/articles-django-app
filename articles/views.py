import datetime
from itertools import count

from django.shortcuts import render, redirect

from .models import *

# Create your views here.
def index(request):
    data = {
        "count_unread": len(Article.objects.filter(status=False)),
        "count_read": len(Article.objects.filter(status=True)),
        "articles": Article.objects.all(),
        "read_today": Article.objects.filter(read_time__date=datetime.datetime.today()).count(),
    }
    return render(request, 'index.html', data)

def articles_read(request):
    data = {
        "count_unread": len(Article.objects.filter(status=False)),
        "count_read": len(Article.objects.filter(status=True)),
        "articles": Article.objects.filter(status=True),
        "read_today": Article.objects.filter(read_time__date=datetime.datetime.today()).count(),

    }

    return render(request, 'index.html', data)

def articles_unread(request):
    data = {
        "articles": Article.objects.filter(status=False),
        "count_unread": len(Article.objects.filter(status=False)),
        "count_read": len(Article.objects.filter(status=True)),
        "read_today": Article.objects.filter(read_time__date=datetime.datetime.today()).count(),

    }

    return render(request, 'index.html', data)

def article(request, a):
    data = {
        "article": Article.objects.get(id=a),
    }
    return render(request, 'article.html', data)

def mark_as_read(request, b):
    article = Article.objects.get(id=b)
    article.status = True
    article.read_time = datetime.datetime.now()
    article.save()

    return redirect("/")