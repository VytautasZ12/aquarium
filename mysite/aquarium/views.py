from django.shortcuts import render
from django.http import HttpResponse
from . models import FishSpieces, Fish


# Create your views here.
def index(request):
    num_fishspecies = FishSpieces.objects.count()
    num_fish = Fish.objects.count()

    context = {
        'num_fishspecies': num_fishspecies,
        'num_fish': num_fish,
    }
    return render(request, 'index.html', context=context)