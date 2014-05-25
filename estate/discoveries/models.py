from django.db import models

# part_number could be redone as a foreign key "part_number_id"
# where there would be a table "PartNumber" with all the possible
# part numbers
# Also, it is possible to self-reference each part number to another 
# part number as contained_in. This would be implemented as a 
# foreign key pointing to the same table
class PartDiscovered (models.Model):
    hostname = models.CharField(max_length=200, null=True)
    part_number = models.CharField(max_length=200, null=True)
    serial_number = models.CharField(max_length=200)
    type = models.PositiveSmallIntegerField(null=True)
    is_fru = models.NullBooleanField()
    date_discovered = models.DateTimeField('date discovered', null=True)

    def __unicode__(self):
        return self.serial_number
