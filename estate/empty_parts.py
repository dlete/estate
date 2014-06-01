import os


def empty_all_parts():

    # delete all the parts discovered
    print "I am going to delete the PartDiscovered table"
    for pn in PartDiscovered.objects.all():
        pn.delete()

    print "I am going to delete the PartSupported table"
    for pn in PartSupported.objects.all():
        pn.delete()


# Start execution here!
if __name__ == '__main__':
    print "Starting to populate the PartDiscovered table..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estate.settings')
    from discoveries.models import PartDiscovered
    from support.models import PartSupported
    empty_all_parts()
