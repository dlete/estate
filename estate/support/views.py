from django.shortcuts import render
from discoveries.models import PartDiscovered
from support.models import PartSupported
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from support.forms import EditPartSupportedForm

def search_form(request):
    context = {'bodymessage': "search_form in Support."}
    return render(request, 'support/search_form.html', context)

# import Q is needed for searches
# https://docs.djangoproject.com/en/dev/topics/db/queries/#complex-lookups-with-q-objects
# recipe: http://www.michelepasin.org/blog/2010/07/20/the-power-of-djangos-q-objects/
# http://julienphalip.com/post/2825034077/adding-search-to-a-django-site-in-a-snap
from django.db.models import Q
import functools
import operator
def search_results(request):
    context = {'bodymessage': "search_results in Support."}
    if request.method == 'POST':
    # Now we update only the fields/attributes that do NOT have a null
    # value in the form

        my_list = []
        if request.POST.get('hostname'):
            hostname = request.POST['hostname']
            my_list.append(('hostname__icontains', hostname))

# works
#            parts = PartSupported.objects.filter(hostname__icontains=hostname)
            parts = PartSupported.objects.filter(Q(hostname__icontains=hostname))
            context['parts'] = parts

        q_list = [Q(x) for x in my_list]
        parts = PartSupported.objects.filter(functools.reduce(operator.or_, q_list))
        context['parts'] = parts
#        else:
#            context['search_message'] = 'You submitted an empty form.'

    return render(request, 'support/search_results.html', context)



# to use the Python CSV library
import csv
from django.http import HttpResponse

def edit_one(request, part_id):
    context = {'bodymessage': "edit_one in Support."}

    part_supported = PartSupported.objects.get(id=part_id)
    context['part_supported'] = part_supported

    return render(request, 'support/edit_one.html', context)

def update_one(request, part_id):
    context = {'bodymessage': "update_one in Support."}

    part_supported = PartSupported.objects.get(id=part_id)
    context['part_supported'] = part_supported

    if request.method == 'POST':
        # Now we update only the fields/attributes that do NOT have a null
        # value in the form

        # get value from the form
        hostname = request.POST.get('hostname')
        # if empty -> do nothing. 
        # If there is a value -> update all records with that value
        if hostname != "":
            part_supported.hostname = hostname
            part_supported.save()

        # repeat the same process. Most proabably this can be refractored        
        part_number = request.POST.get('part_number')
        if part_number != "":
            part_supported.part_number = part_number
            part_supported.save()

        # Once done, send to the Index page
        return HttpResponseRedirect(reverse('support:index'))

#    return render(request, 'support/update_one.html', context)


# KEEP
def edit_many_part_supported(request):
    if request.method == 'POST':
        context = {'bodymessage': "edit_many_part_supported in Support."}
        parts_to_edit = request.POST.getlist('chosen_parts')
        context['parts_to_edit'] = parts_to_edit
        return render(request, 'support/edit_many_part_supported.html', context)

# KEEP
def update_many_part_supported(request):
    if request.method == 'POST':
        # the form does give us a list of integers (like [u'193', u'194']) that are the
        # id of the objects selected
        part_ids_to_update = request.POST.getlist('chosen_parts')

        # From the ids we get the objects.
        # Get all the PartSupported objects that have been selected for update
        # https://docs.djangoproject.com/en/dev/ref/models/querysets/#in
        parts_to_update = PartSupported.objects.filter(id__in=part_ids_to_update)

        # Now we update only the fields/attributes that do NOT have a null
        # value in the form

        # get value from the form
        hostname = request.POST.get('hostname')
        # if empty -> do nothing. 
        # If there is a value -> update all records with that value
        if hostname != "":
            parts_to_update.update(hostname=hostname)

        # repeat the same process. Most proabably this can be refractored        
        part_number = request.POST.get('part_number')
        if part_number != "":
            parts_to_update.update(part_number=part_number)

        # Once done, send to the Index page
        return HttpResponseRedirect(reverse('support:index'))


# KEEP
def index(request):
    context = {'bodymessage': "Index view in Support. Maybe include a form/checkboxes"}

    parts_supported = PartSupported.objects.all()
    context['parts_supported'] = parts_supported

#    return render(request, 'support/index.html', context)

    if request.method == 'GET':
        ''' normal situation '''
        return render(request, 'support/index.html', context)
    if request.method == 'POST':
        ''' user wants to download the contents of the page '''
        if request.POST.get('download_spreadsheet'):
#            return render(request, 'support/index.html', context)
            # Create the HttpResponse object with the appropriate CSV header.
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
            writer = csv.writer(response)
            for part in parts_supported:
                writer.writerow([
                    part.hostname,
                    part.part_number,
                    part.serial_number,
            ])
            return response




# this should be in a reconcile app?
def add_to_support(request, part_id):
    add_discovered_part_to_support(part_id)
    return HttpResponseRedirect(reverse('support:reconcile'))


# this should be in a reconcile app?
def add_to_support_many(request):
    if request.method == 'POST':
#        context = {'bodymessage': "add_to_support_many view in Support"}
#        context['titlemessage'] = "add many"

        part_ids = request.POST.getlist('chosen_parts')
        for part_id in part_ids:
            add_discovered_part_to_support(part_id)

        return HttpResponseRedirect(reverse('support:reconcile'))


# this should be in a reconcile app?
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
