from django.shortcuts import render

# from now down, not defaults
from discoveries.models import PartDiscovered

def aa(request):
    context = {'bodymessage': "AA page of the discoveries app"}
    context['titlemessage'] = "AA"

    parts_discovered = PartDiscovered.objects.all()
    context['parts_discovered'] = parts_discovered
    return render(request, 'discoveries/aa.html', context)


def ab(request):
    context = {'bodymessage': "AB page of the discoveries app"}
    context['titlemessage'] = "AB"

    if request.POST['choice']:
        c = request.POST['choice']
        pieza = PartDiscovered.objects.get(pk=c)
        context['pieza'] = pieza
    else:
        context['pieza'] = "vacio"

    if request.POST['vehicle']:
        v = request.POST.getlist('vehicle')
        context['vehiculo'] = v
    else:
        context['vehiculo'] = "vacio"

    return render(request, 'discoveries/ab.html', context)


def index(request):
    context = {'boldmessage': "This is the INDEX page of the discoveries app. I am using templates"}
    return render(request, 'discoveries/index.html', context)

def reports(request):
    number_of_parts_discovered = PartDiscovered.objects.all().count()
    context = {'number_of_parts_discovered': number_of_parts_discovered}
    context['boldmessage'] = "This is the REPORTS page of the discoveries app. I am using templates"
    return render(request, 'discoveries/reports.html', context)


def scan(request):
    context = {'boldmessage': "This is the SCAN page of the discoveries app"}

    number_of_parts_discovered = PartDiscovered.objects.all().count()
    context['number_of_parts_discovered'] = number_of_parts_discovered
    return render(request, 'discoveries/scan.html', context)
