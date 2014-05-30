from django.shortcuts import render
from discoveries.models import PartDiscovered
from support.models import PartSupported

# Create your views here.
def index(request):
    context = {'bodymessage': "Index view in Support. Maybe include a form/checkboxes"}
    return render(request, 'support/index.html', context)


def reconcile(request):
    context = {'bodymessage': "Reconcile view in Support. Maybe include a form/checkboxes"}

    parts_discovered = PartDiscovered.objects.all()
    parts_supported = PartSupported.objects.all()
    context['number_of_parts_discovered'] = parts_discovered.count()
    context['number_of_parts_supported'] = parts_supported.count()



    return render(request, 'support/reconcile.html', context)
