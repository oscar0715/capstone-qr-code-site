from django.contrib import admin

from .models import Traveller, Background, TravelPlan, Area, Shop
from .models import ShopActivity, AirportActivity

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class AreaResource(resources.ModelResource):
    class Meta:
        model = Area

class AreaAdmin(ImportExportModelAdmin):
    resource_class = AreaResource
    readonly_fields = ('created','modified')

admin.site.register(Area, AreaAdmin)


class TravellerResource(resources.ModelResource):
    class Meta:
        model = Traveller

class TravellerAdmin(ImportExportModelAdmin):
    resource_class = TravellerResource
    readonly_fields = ('created','modified')

admin.site.register(Traveller, TravellerAdmin)



class BackgroundResource(resources.ModelResource):
    class Meta:
        model = Background
        import_id_fields = ['traveller']

class BackgroundAdmin(ImportExportModelAdmin):
    resource_class = BackgroundResource
    readonly_fields = ('created','modified')

admin.site.register(Background, BackgroundAdmin)



class TravelPlanResource(resources.ModelResource):
    class Meta:
        model = TravelPlan
        import_id_fields = ['traveller']

class TravelPlanAdmin(ImportExportModelAdmin):
    resource_class = TravelPlanResource
    readonly_fields = ('created','modified')

admin.site.register(TravelPlan, TravelPlanAdmin)

class ShopResource(resources.ModelResource):
    class Meta:
        model = Shop

class ShopAdmin(ImportExportModelAdmin):
    resource_class = ShopResource
    readonly_fields = ('created','modified')

admin.site.register(Shop, ShopAdmin)

class ShopActivityResource(resources.ModelResource):
    class Meta:
        model = ShopActivity
        import_id_fields = ['traveller']

class ShopActivityAdmin(ImportExportModelAdmin):
    resource_class = ShopActivityResource
    readonly_fields = ('created','modified')

admin.site.register(ShopActivity, ShopActivityAdmin)

class AirportActivityResource(resources.ModelResource):
    class Meta:
        model = AirportActivity
        import_id_fields = ['traveller']

class AirportActivityAdmin(ImportExportModelAdmin):
    resource_class = AirportActivityResource
    readonly_fields = ('created','modified')

admin.site.register(AirportActivity, AirportActivityAdmin)