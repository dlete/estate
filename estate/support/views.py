from django.shortcuts import render
from discoveries.models import PartDiscovered
from support.models import PartSupported
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    context = {'bodymessage': "Index view in Support. Maybe include a form/checkboxes"}
    return render(request, 'support/index.html', context)

def add_to_support(request, part_id):
    context = {'bodymessage': "Add To Support view in Support"}
    part = get_object_or_404(PartDiscovered, pk=part_id)
    context['part'] = part

    part_supported = PartSupported.objects.get_or_create(
        hostname = part.hostname,
        serial_number = part.serial_number,
        comment = "Add to contract",
        is_active = 1,
        date_added = timezone.now(),
        date_modified = timezone.now()
        )

#    return render(request, 'support/reconcile.html', context)
    return HttpResponseRedirect(reverse('support:reconcile'))

def reconcile(request):
    context = {'bodymessage': "Reconcile view in Support. Maybe include a form/checkboxes"}

    parts_discovered = PartDiscovered.objects.all()
    parts_supported = PartSupported.objects.all()
    context['number_of_parts_discovered'] = parts_discovered.count()
    context['number_of_parts_supported'] = parts_supported.count()


    discovered_serial_numbers = set(pd.serial_number for pd in parts_discovered)
    supported_serial_numbers = set(ps.serial_number for ps in parts_supported)

    serials_only_in_discovered = discovered_serial_numbers.difference(supported_serial_numbers)
    serials_only_in_supported = supported_serial_numbers.difference(discovered_serial_numbers)
    serials_in_discovered_and_supported = discovered_serial_numbers.intersection(supported_serial_numbers)

    parts_only_in_discovered = []
    for s in serials_only_in_discovered:
        pn = PartDiscovered.objects.get(serial_number=s)
        parts_only_in_discovered.append(pn)

    parts_only_in_supported = []
    for s in serials_only_in_supported:
        pn = PartSupported.objects.get(serial_number=s)
        parts_only_in_supported.append(pn)

    context['parts_only_in_discovered'] = parts_only_in_discovered
    context['parts_only_in_supported'] = parts_only_in_supported

    return render(request, 'support/reconcile.html', context)
