from django.contrib import admin

from .models import Traveller, Background, TravelPlan, Area, Shop, ShopActivity

# Register your models here.

class TimeAdmin(admin.ModelAdmin):
    readonly_fields = ('created','modified')

admin.site.register(Background, TimeAdmin)
admin.site.register(Traveller, TimeAdmin)
admin.site.register(TravelPlan, TimeAdmin)
admin.site.register(Area, TimeAdmin)
admin.site.register(Shop, TimeAdmin)
admin.site.register(ShopActivity, TimeAdmin)