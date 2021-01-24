from django.shortcuts import render
import json
import os

def index(request):
    context = {'title': 'Магазин'}
    return render(request, 'mainapp/index.html', context)

def products(request):
    module_dir = os.path.dirname(__file__)
    with open(os.path.join(module_dir, 'fixtures/products.json'), "r", encoding='UTF-8') as f:
        to_python = json.loads(f.read())

    context = {'title': 'Товары',
               'products': to_python}
    return render(request, 'mainapp/products.html', context)

def contact(request):
    context = {'title': 'Контакты'}
    return render(request, 'mainapp/contact.html', context)