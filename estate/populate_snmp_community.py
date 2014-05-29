import os

def populate():

    add_snmp_community(
        name="community1",
        version=2)

    add_snmp_community(
        name="community2",
        version=2)

    # Print out what we have added.
    for c in SnmpCommunity.objects.all():
        print "- {0}".format(str(c))

def add_snmp_community(name, version):
    c = SnmpCommunity.objects.get_or_create(name=name, version=version)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting to populate SNMP Communities..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estate.settings')
    from discoveries.models import SnmpCommunity
    populate()
