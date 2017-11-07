from django.shortcuts import render
from charative.models import Chara
from charativeproject.settings.local import BASE_DIR

# Create your views here.

def index(request):

    poop, made = Chara.objects.get_or_create(name="Midas")
    print(poop.name)
    context = {}
    context['poop'] = poop

    return render(request, 'index.html', context)
