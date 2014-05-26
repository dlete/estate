from django.shortcuts import render

# from now down, not defaults
from django.http import HttpResponse
from django.template import RequestContext, loader
from discoveries.models import PartDiscovered

def index(request):
    return HttpResponse("This is the INDEX page of the discoveries app")

def reports(request):
    number_of_parts_discovered = PartDiscovered.objects.all().count()
    template = loader.get_template('discoveries/reports.html')
    context = RequestContext(request, {
        'number_of_parts_discovered': number_of_parts_discovered,
    })
    return HttpResponse(template.render(context))

def scan(request):
    return HttpResponse("This is the SCAN page of the discoveries app")
