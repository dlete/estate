import os

def populate():

    add_discovery(
        name="Discovery 1")

    add_discovery(
        name="Discovery 2")

    # Print out what we have added.
    for c in Discovery.objects.all():
        print "- {0}".format(str(c))

def add_discovery(name):
    c = Discovery.objects.get_or_create(name=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting to populate the Discovery table..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estate.settings')
    from discoveries.models import Discovery
    populate()
