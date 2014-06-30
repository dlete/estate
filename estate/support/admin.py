from django.contrib import admin

# Register your models here.
from support.models import PartSupported
from support.models import Location
from support.models import Project
from support.models import Budget
from support.models import Site
admin.site.register(PartSupported)
admin.site.register(Location)
admin.site.register(Project)
admin.site.register(Budget)
admin.site.register(Site)
