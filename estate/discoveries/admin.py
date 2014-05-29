from django.contrib import admin
from discoveries.models import PartDiscovered

from discoveries.models import Discovery
from discoveries.models import DiscoveryToIpNetwork
from discoveries.models import IpNetwork
from discoveries.models import IpNetworkToSnmpCommunity
from discoveries.models import SnmpCommunity


# Register your models here.
admin.site.register(PartDiscovered)

admin.site.register(Discovery)
admin.site.register(DiscoveryToIpNetwork)
admin.site.register(IpNetwork)
admin.site.register(IpNetworkToSnmpCommunity)
admin.site.register(SnmpCommunity)

