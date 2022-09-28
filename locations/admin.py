from django.contrib import admin

from .models import Location, Country, Person

# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'country')
    list_filter = ('country', 'date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Location, LocationAdmin)
admin.site.register(Country)
admin.site.register(Person)