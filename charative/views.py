from django.shortcuts import render
from charativeproject.settings.local import BASE_DIR

# Create your views here.

def index(request):
    context = {'poop':'poop'}
    return render(request, 'index.html', context)
