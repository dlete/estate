import os

def populate():

    add_ip_network(
        name="network1",
        network="193.1.1.0/24")

    add_ip_network(
        name="network2",
        network="193.1.2.0/24")

    # Print out what we have added.
    for c in IpNetwork.objects.all():
        print "- {0}".format(str(c))

def add_ip_network(name, network):
    c = IpNetwork.objects.get_or_create(name=name, network=network)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting to populate IP Networks..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estate.settings')
    from discoveries.models import IpNetwork
    populate()
