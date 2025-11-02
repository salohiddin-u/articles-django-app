from django.shortcuts import render, redirect

from .models import *

# Create your views here.
def index(request):
    data = {
        "articles": Article.objects.all(),
    }
    return render(request, 'index.html', data)

def articles_read(request):
    data = {
        "articles": Article.objects.filter(status=True),
    }

    return render(request, 'index.html', data)

def articles_unread(request):
    data = {
        "articles": Article.objects.filter(status=False),
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
    article.save()
    return redirect("/")