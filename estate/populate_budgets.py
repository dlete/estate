import os
import random
import string


def random_string_number_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def populate():

    # add to Budgets, random items
    for i in range(7):
        piccolo = random.randint(3, 7)
        grande = random.randint(9, 23)
        abbreviation = random_string_number_generator(piccolo)
        name = random_string_number_generator(grande)
        project_id = 3
        add_budget(abbreviation, name, project_id)

    # print what we have added
    for budget in Budget.objects.all():
        print "- {0}".format(str(budget))


def add_budget(abbreviation, name, project_id):
    budget = Budget.objects.get_or_create(
        abbreviation = abbreviation,
        name = name,
        project = Project.objects.get(id=project_id)
        )[0]
    return budget


# Start execution here!
if __name__ == '__main__':
    print "Starting to populate the Budget table..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estate.settings')
    from support.models import Budget
    from support.models import Project
    populate()
