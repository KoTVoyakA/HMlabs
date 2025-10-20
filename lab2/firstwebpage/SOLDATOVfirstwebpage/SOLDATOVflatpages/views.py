from django.http import HttpResponse
from django.shortcuts import render

# с указанием типа
def hello_with_type(request):
    return HttpResponse('Привет, Мир!', content_type="text/plain")

# без указания типа
def hello(request):
    return HttpResponse('Привет, Мир!')


# Представление для шаблона
def home(request):
    # render ищет 'index.html' в DIRS и app/templates
    return render(request, 'index.html')
