import datetime
import os
import random
import string


def random_string_number_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def populate():

    # add to both Discovered and Supported, random items
    for i in range(15):
        length = random.randint(7, 11)
        sn = random_string_number_generator(length)
        is_fru = 1
        is_active = 1
        just_now = timezone.now()
        add_part_discovered(sn, is_fru, just_now)
        add_part_supported(sn, is_active, just_now)


    # add random items to Discovered
    for i in range(5):
        length = random.randint(9, 13)
        sn = random_string_number_generator(length)
        is_fru = 1
        just_now = timezone.now()
        add_part_discovered(sn, is_fru, just_now)


    # add random items to Supported
    for i in range(4):
        length = random.randint(6, 12)
        sn = random_string_number_generator(length)
        is_active = 1
        just_now = timezone.now()
        add_part_supported(sn, is_active, just_now)


    # add a known sequence to Discovered
    for i in range(1010, 1020):
        sn = i
        is_fru = 1
        just_now = timezone.now()
        add_part_discovered(sn, is_fru, just_now)


    # add a known sequence to Supported
    for i in range(1015, 1025):
        sn = i
        is_active = 0
        just_now = timezone.now()
        add_part_supported(sn, is_active, just_now)

    
    # print what we have added
    for pn in PartDiscovered.objects.all():
        print "- {0}".format(str(pn))


def add_part_discovered(serial_number, is_fru, date_discovered):
    pd = PartDiscovered.objects.get_or_create(
        serial_number = serial_number, 
        is_fru = is_fru,
        date_discovered = date_discovered
        )[0]
    return pd

def add_part_supported(serial_number, is_active, date_added):
    ps = PartSupported.objects.get_or_create(
        serial_number = serial_number,
        is_active = is_active,
        date_added = date_added
        )[0]
    return ps

# Start execution here!
if __name__ == '__main__':
    print "Starting to populate the PartDiscovered table..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estate.settings')
    from discoveries.models import PartDiscovered
    from support.models import PartSupported
    from django.utils import timezone
    populate()
