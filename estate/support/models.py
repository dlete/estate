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

 
class Site(models.Model):
    parent_type = models.CharField(max_length=200, null=True)
    abbreviation = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
# Company table is not defined yet
#    company = models.ForeignKey('Company')
# clientdb names lat and lng
# latitude (-90 to +90) with space for 5 decimals, (-90.00000 to 90.00000) 
    latitude = models.DecimalField(max_digits=7, decimal_places=5, null=True)
# longitude  (-180.00000 to 180.00000)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
# clientdb has the field "zoom", not imported here
#    zoom = models.PositiveSmallIntegerField(null=True)
# could be just Boolean, but we do not know if clientdb will enforce
    is_pop = models.NullBooleanField()
    active = models.NullBooleanField()

    def __unicode__(self):
        return self.abbreviation
