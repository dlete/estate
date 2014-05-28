from django.contrib import admin

# Register your models here.
from scout.models import Discovery
from scout.models import DiscoveryToIpNetwork
from scout.models import IpNetwork, IpNetworkToSnmpCommunity, SnmpCommunity

admin.site.register(Discovery)
admin.site.register(DiscoveryToIpNetwork)
admin.site.register(IpNetwork)
admin.site.register(IpNetworkToSnmpCommunity)
admin.site.register(SnmpCommunity)
