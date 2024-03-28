from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def trainer(request):
    return render(request, 'trainer.html')

def why_view(request):
    return render(request, 'why.html')