from django.shortcuts import render

from scout.models import Discovery
from scout.forms import SaForm
from discoveries.models import PartDiscovered
import logging

# to use the Python CSV library
import csv
from django.http import HttpResponse

def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

#    writer = csv.writer(response)
#    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
#    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    parts = PartDiscovered.objects.all()
    writer = csv.writer(response)
    writer.writerow([
        "Hostname",
        "Part number",
        "Serial number",
    ])
    for part in parts:
        writer.writerow([
            part.hostname,
            part.part_number,
            part.serial_number,
        ])
    return response


def aa(request):
    context = {'bodymessage': "AA page of the Scout app"}
    context['titlemessage'] = "AA Scout"

    parts = PartDiscovered.objects.all()[0:4]
    context['parts'] = parts

    return render(request, 'scout/aa.html', context)


def ab(request):
    if request.method == 'POST':
        context = {'bodymessage': "AB page of the Scout app"}

        parts = request.POST.getlist('parts')
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
    context = {'title': "INDEX SCOUT"}
    context['bodymessage'] = "Index page of the scout app"

    discovered_parts = PartDiscovered.objects.all()
    context['discovered_parts'] = discovered_parts

    return render(request, 'scout/index.html', context)
