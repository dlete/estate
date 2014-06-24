import datetime
import os
import random
import string


def random_string_number_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def populate():

    # add to Locations, random items
    for i in range(15):
        length = random.randint(7, 11)
        abbreviation = random_string_number_generator(length)
        internal_designation = random_string_number_generator(length)
        building = random_string_number_generator(length)
        street = random_string_number_generator(length)
        country = random_string_number_generator(length)
        add_location(abbreviation, internal_designation, building, street, country)

    # print what we have added
    for location in Location.objects.all():
        print "- {0}".format(str(location))


def add_location(abbreviation, internal_designation, building, street, country):
    location = Location.objects.get_or_create(
        abbreviation = abbreviation,
        internal_designation = internal_designation,
        building = building,
        street = street,
        country = country
        )[0]
    return location


# Start execution here!
if __name__ == '__main__':
    print "Starting to populate the Location table..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estate.settings')
    from support.models import Location
    populate()
