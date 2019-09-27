from django.contrib import admin

# Register your models here.
from django.contrib import admin
from portalapp.models import HydJob
from portalapp.models import PuneJob
from portalapp.models import BangaloreJob
from portalapp.models import ChennaiJob
from portalapp.models import MumbaiJob


# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ['posting_date','job_title','location','position','eligibility','last_date','more_information']


admin.site.register(HydJob, JobAdmin)
admin.site.register(PuneJob, JobAdmin)
admin.site.register(BangaloreJob, JobAdmin)
admin.site.register(ChennaiJob, JobAdmin)
admin.site.register(MumbaiJob, JobAdmin)


