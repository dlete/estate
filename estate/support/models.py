from django.db import models

# Create your models here.
class PartSupported (models.Model):
    project = models.CharField(max_length=200, null=True)
    budget_name = models.CharField(max_length=200, null=True)
    budget_number = models.PositiveSmallIntegerField(null=True)
    comment = models.CharField(max_length=400, null=True)
    to_do = models.CharField(max_length=200, null=True)
    hostname = models.CharField(max_length=200, null=True)
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

    def __unicode__(self):
        return self.serial_number
