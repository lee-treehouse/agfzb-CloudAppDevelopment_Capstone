from django.contrib import admin
from .models import CarMake, CarModel

# from .models import related models

# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel 
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['name', 'description']

class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'type']
    inlines = [CarModelInline]


# Register models here
admin.site.register(CarModel)
admin.site.register(CarMake)
