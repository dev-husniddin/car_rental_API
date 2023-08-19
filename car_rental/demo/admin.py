from django.contrib import admin
from demo.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    model = Car
    list_display = ('id', 'model', 'make', 'year', 'color', 'mileage', 'fuel_type', 'price_per_day','avaibilaty_status')
    list_filter = ('model','make','year', 'color', 'mileage', 'fuel_type', 'price_per_day', )
    search_fields = ('model','make')
    list_display_links = ('id','model')
    list_per_page = 10

