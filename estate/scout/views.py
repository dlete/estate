from django.shortcuts import render

# Create your views here.
from scout.models import Discovery
from django.http import HttpResponse

def discoveries(request):
    context = {'bodymessage': "Discoveries view of the scout app"}

    all_discoveries = Discovery.objects.all()
    context['all_discoveries'] = all_discoveries
    return render(request, 'scout/discoveries.html', context)

def disc_detail(request, disc_id):
    return HttpResponse("You're looking at discovery %s." % disc_id)

def index(request):
    context = {'boldmessage': "This is the INDEX page of the scout app"}
    return render(request, 'scout/index.html', context)
