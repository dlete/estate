from django.shortcuts import render

from scout.models import Discovery
from scout.forms import SaForm
from discoveries.models import PartDiscovered
import logging

def aa(request):
    context = {'bodymessage': "AA page of the Scout app"}
    context['titlemessage'] = "AA Scout"

#    fruits = ['apple', 'cherry', 'pear']
#    context['fruits'] = fruits

    parts = PartDiscovered.objects.all()[0:4]
#    parts = [[p.id, p.serial_number] for p in PartDiscovered.objects.all()[0:4]]
    context['parts'] = parts

    return render(request, 'scout/aa.html', context)


def ab(request):
    if request.method == 'POST':
        context = {'bodymessage': "AB page of the Scout app"}

#        fruits = request.POST.getlist('fruits')
#        context['fruits'] = fruits

        parts = request.POST.getlist('parts')
#        parts = request.POST.lists()
        context['parts'] = parts

        return render(request, 'scout/ab.html', context)


def sa(request):
    form = SaForm()
    return render(request, 'scout/sa.html', {'form': form})


def sb(request):
    try:
        selected_choices = request.POST.getlist('interests')
    except:
        return HttpResponseRedirect(reverse('scout:sa'))
    else:
        context = {'bodymessage': "SB view of the scout app"}
        context['selected_choices'] = selected_choices
        return render(request, 'scout/sb.html', context)


def index(request):
    context = {'boldmessage': "This is the INDEX page of the scout app"}
    return render(request, 'scout/index.html', context)
