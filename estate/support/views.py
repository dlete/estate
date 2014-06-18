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

    parts_supported = PartSupported.objects.all()
    context['parts_supported'] = parts_supported

    return render(request, 'support/index.html', context)


def add_to_support(request, part_id):
    add_discovered_part_to_support(part_id)
    return HttpResponseRedirect(reverse('support:reconcile'))

def add_to_support_many(request):
    if request.method == 'POST':
#        context = {'bodymessage': "add_to_support_many view in Support"}
#        context['titlemessage'] = "add many"

        part_ids = request.POST.getlist('chosen_parts')
        for part_id in part_ids:
            add_discovered_part_to_support(part_id)

        '''
        chosen_parts = request.POST.getlist('chosen_parts')
        parts_to_add = []
        for part_id in chosen_parts:
            part_to_add = PartDiscovered.objects.get(id=part_id)
            parts_to_add.append(part_to_add)

        context['parts_to_add'] = parts_to_add

        for part in parts_to_add:
            add_part_to_support = PartSupported.objects.get_or_create(
                hostname = part.hostname,
                serial_number = part.serial_number,
                comment = "Add to contract",
                is_active = 1,
                date_added = timezone.now(),
                date_modified = timezone.now()
                )

#        return render(request, 'support/add_to_support_many.html', context)
        '''
        return HttpResponseRedirect(reverse('support:reconcile'))

def reconcile(request):
    context = {'bodymessage': "Reconcile view in Support."}

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


# function to move a PartDiscovered to PartSupported
# takes as input the ID (integer) of the PartDiscovered
def add_discovered_part_to_support(discovered_part_id):
    part_discovered = PartDiscovered.objects.get(id=discovered_part_id)
    part_supported = PartSupported.objects.get_or_create(
        hostname = part_discovered.hostname,
        serial_number = part_discovered.serial_number,
        comment = "Add to contract",
        is_active = 1,
        date_added = timezone.now(),
        date_modified = timezone.now()
        )
