from django.db import models

# Create your models here.
class PartSupported (models.Model):
    project = models.CharField(max_length=200, null=True)
    budget_name = models.CharField(max_length=200, null=True)
    budget_number = models.PositiveSmallIntegerField(null=True)
    comment = models.CharField(max_length=400, null=True)
    to_do = models.CharField(max_length=200, null=True)
    hostname = models.CharField(max_length=200, null=True)
    # add manufacturer (Cisco, Juniper, etc.)
    part_number = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    serial_number = models.CharField(max_length=200)
    is_active = models.NullBooleanField()
    internal_designation = models.CharField(max_length=200, null=True)
    building = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)
    town_area = models.CharField(max_length=200, null=True)
    county_postcode = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    gps = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField('date added', null=True)
    date_modified = models.DateTimeField('date modified', null=True)
    date_removed = models.DateTimeField('date removed', null=True)
# add date_last_discovered? = models.DateTimeField('date last discovered', null=True)

    def __unicode__(self):
        return self.serial_number

# this table should reside in a different, central?, database and info on it
# be called via an API
class Location (models.Model):
    abbreviation = models.CharField(max_length=200, null=True)
    internal_designation = models.CharField(max_length=200, null=True)
    building = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)
    neighbourhood = models.CharField(max_length=200, null=True)
    town_area = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    gps = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.abbreviation


# this table should reside in a different, central?, database and info on it
# be called via an API
class Project (models.Model):
    abbreviation = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.abbreviation


class Budget(models.Model):
    project = models.ForeignKey('Project')
    abbreviation = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        # if we return self.project, we get the error 
        # 'project' object has no attribute '__getitem__'
        # have to specify to return self.project.abbreviation
        return self.abbreviation
