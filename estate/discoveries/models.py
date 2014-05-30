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
    part_type = models.PositiveSmallIntegerField(null=True)
    is_fru = models.NullBooleanField()
    date_discovered = models.DateTimeField('date discovered', null=True)

    def __unicode__(self):
        return self.serial_number



# should have a field for 
# - the user/company/admin entity owner of the discovery
# - date it was created
# - date it was modified
class Discovery(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

# liaison table between Discovery and IpNetwork tables so that 
# one Discovery can have more than one IpNetwork associated to it
class DiscoveryToIpNetwork(models.Model):
    discovery = models.ForeignKey('Discovery')
    ip_network = models.ForeignKey('IpNetwork')

    def __unicode__(self):
        # if we return self.discovery, we get the error 
        # 'ip_network' object has no attribute '__getitem__'
        # have to specify to return self.discovery.name
        return self.discovery.name


# will store IP addresses as text and rely in Python instead of the database
# to handle IP networks/addresses. Intend to use the "netaddr" package for
# Python 2.x and the "ipaddress" module if Python3. If use the database for
# IP handling then it limits functionality/coding depending on whether MySQL
# or PostgreSQL or SQLITE3 are being used. 
#
# should have a field tying the IP Network tot he user and/or organization/company
# should have a field with created_on and another with modified_on
class IpNetwork(models.Model):
    name = models.CharField(max_length=200)
    network = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class IpNetworkToSnmpCommunity(models.Model):
    ip_network = models.ForeignKey('IpNetwork')
    snmp_community = models.ForeignKey('SnmpCommunity')

    def __unicode__(self):
        # if we return self.ip_network, we get the error 
        # 'ip_network' object has no attribute '__getitem__'
        # have to specify to return self.ip_network.name
        return self.ip_network.name


# should have a field tying the Community to the user and/or organization/company
class SnmpCommunity(models.Model):
    # the lenght of and SNMP community does not seem to be defined anywhere
    # have not found any MIB where it is stated. SNMP-COMMUNITY-MIB 
    # appears to be the place where it should be defined, but it is not
    name = models.CharField(max_length=200)
    # should find a way to limit to 1, 2 or 3
    version = models.PositiveSmallIntegerField(default=2)

    def __unicode__(self):
        return self.name
