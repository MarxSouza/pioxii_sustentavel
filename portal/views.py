from django.shortcuts import render

def index(request):
    return render(request, 'portal/index.html', {})
def form(request):
    return render(request, 'portal/form.html', {})
def grafico(request):
    return render(request, 'portal/grafico.html', {})
def sobre(request):
    return render(request, 'portal/sobre.html', {})