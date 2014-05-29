from django.shortcuts import render

# from now down, not defaults
from django.shortcuts import get_object_or_404

from discoveries.models import PartDiscovered
from discoveries.models import Discovery


def index(request):
    context = {'bodymessage': "Index view of the discoveries app"}
    all_discoveries = Discovery.objects.all()
    context['all_discoveries'] = all_discoveries
    return render(request, 'discoveries/index.html', context)


def detail(request, discovery_id):
    context = {'bodymessage': "Detail view of the discoveries app"}
    discovery = get_object_or_404(Discovery, pk=discovery_id)
    context['discovery'] = discovery
    context['discovery_to_ipnetworks'] = discovery.discoverytoipnetwork_set.all()
    # it is missing to print the snmp communities associated with each of the networks
    return render(request, 'discoveries/detail.html', context)    


def scan(request, discovery_id):
    context = {'bodymessage': "This is the SCAN page of the discoveries app"}
    context['titlemessage'] = "SCAN DISC"

    discovery = get_object_or_404(Discovery, pk=discovery_id)

    # this should be a list with entries being a couple discovery <-> network
    discovery_to_ipnetworks = discovery.discoverytoipnetwork_set.all()
    networks = []
    for di in discovery_to_ipnetworks:
        n = di.ip_network
        networks.append(n.network)
    context['networks'] = networks

    ip_collections = []
    for n in networks:
#        n = IPNetwork(n)
        # list
        ip_collection = explode_network(n)

        # append list to another list
        ip_collections.append(ip_collection)
    context['ip_collections'] = ip_collections
         

    context['discovery'] = discovery
    return render(request, 'discoveries/scan.html', context)


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



def reports(request):
    number_of_parts_discovered = PartDiscovered.objects.all().count()
    context = {'number_of_parts_discovered': number_of_parts_discovered}
    context['boldmessage'] = "This is the REPORTS page of the discoveries app. I am using templates"
    return render(request, 'discoveries/reports.html', context)



###############################################################################

from netaddr import *

###############################################################################
'''
Requires:
This function needs the module "netaddr"

What it does:
Takes text and converts to an IPNetwork object (as defined in the netaddr  
module) to lists all the valid IP addresses in that network. 
Valid in this case means that the IP representing the network (the first one 
in the range) and the broadcast (the last on in the range) are not listed.
There are exceptions though:
 - in networks with /31 and /32 mask all IP addresses are valid, so are printed

 How to use
 network = '192.168.12.0/29'
 explode_network(network)
'''
def explode_network(network):
    # convert to and netaddr network object
    network = IPNetwork(network)

    # initialize an empty list. We will populate it with IP addresses
    valid_ip_addresses = []

    # find out the number of IP addresses contained in the network
    network_size = network.size

    # if the mask is /30 or lower (e.g. /29, /28, etc.) the number of IP
    # addresses in the network will be more than 2
    if network_size > 2:
        # the first IP in the range represents the network, not valid for hosts
        # hence we bypass it and start on the second IP address
        first_valid_ip = 1

        # the last IP in the range represents all the hosts (broadcast address)
        # hence not valid neither. We are not interested in this IP address
        last_valid_ip = network_size - 1
    elif network_size <= 2:
        # this is a /31 or a /32, where all IP in the range are valid

        # start on the first IP address
        first_valid_ip = 0

        # stop counting on the third IP address. If we handle a /31 we will
        # have 2 address, if a /32 we will have a single one. In both cases
        # we are covered stopping counting in the third IP
        #
        # remember, in a list b = a[start:stop]
        # start is the first item that we want
        # stop is the first item that we do not want
        last_valid_ip = 2
#    elif network_size == 1:
#        # this a /32, 
#        first_ip = 0
#        last_ip = 1
    else:
        print "I have no clue. I guess I should raise an error and let you know"

    # now iterate through the IP in the network. Start and stop where
    # appropiate, the If conditions above will have set the start/end variables
    for ip in network[first_valid_ip:last_valid_ip]:
        # append to a list
        valid_ip_addresses.append(str(ip))

    # this is our product: a LIST with valid IP addresses in the network that
    # was given to us as input
    return valid_ip_addresses
###############################################################################
