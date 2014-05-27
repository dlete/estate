from django.contrib import admin

# Register your models here.
from scout.models import IpNetwork, IpNetworkToSnmpCommunity, SnmpCommunity

admin.site.register(IpNetwork)
admin.site.register(IpNetworkToSnmpCommunity)
admin.site.register(SnmpCommunity)
