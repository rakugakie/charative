from django.shortcuts import render
from charative.models import Chara
from django.shortcuts import redirect
# Create your views here.


def index(request):

    poop, made = Chara.objects.get_or_create(name="Midas")
    print(poop.name)
    context = {}
    context['poop'] = poop

    return render(request, 'index.html', context)


def indexredirect(request):

    return redirect('index')