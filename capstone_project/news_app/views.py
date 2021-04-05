from django.shortcuts import render
from news_app.models import Barron, Bloomberg, Google
def index(request):
    barrons_lst = Barron.objects.all()
    bloomberg_lst = Bloomberg.objects.all()
    google_lst = Google.objects.all()
    context = {
        'barrons_objects': barrons_lst,
        'bloomberg_objects': bloomberg_lst,
        'google_objects': google_lst,
    }
    return render(request, 'index.html', context)
