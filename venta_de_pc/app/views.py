from django.shortcuts import render

def index(request):
    context = {'saludo': "hola pendejos"}
    return render(request, 'index.html', context)