from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    data = {
        "articles": Article.objects.all(),
    }
    return render(request, 'index.html', data)

def article(request, a):
    data = {
        "article": Article.objects.get(id=a),
    }
    return render(request, 'article.html', data)