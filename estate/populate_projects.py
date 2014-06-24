import datetime
import os
import random
import string


def random_string_number_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def populate():

    # add to Projects, random items
    for i in range(7):
        piccolo = random.randint(3, 7)
        grande = random.randint(9, 23)
        abbreviation = random_string_number_generator(piccolo)
        name = random_string_number_generator(grande)
        add_project(abbreviation, name)

    # print what we have added
    for project in Project.objects.all():
        print "- {0}".format(str(project))


def add_project(abbreviation, name):
    project = Project.objects.get_or_create(
        abbreviation = abbreviation,
        name = name
        )[0]
    return project


# Start execution here!
if __name__ == '__main__':
    print "Starting to populate the Project table..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estate.settings')
    from support.models import Project
    populate()
