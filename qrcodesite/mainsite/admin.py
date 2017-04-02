from django.contrib import admin

from .models import Traveller, Background, TravelPlan

# Register your models here.

class TimeAdmin(admin.ModelAdmin):
    readonly_fields = ('created','modified')

admin.site.register(Background, TimeAdmin)
admin.site.register(Traveller, TimeAdmin)
admin.site.register(TravelPlan, TimeAdmin)