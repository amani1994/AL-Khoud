from django.contrib import admin
from .models import Club, Say, Offers, Package

# Register your models here.


class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'decription', 'city', 'type')
    list_filter=('city',)


class SayAdmin(admin.ModelAdmin):
    list_display = ('name', 'decription')

class OffersAdmin(admin.ModelAdmin):
    list_display=('name','price','discount','description')

class PackageAdmin (admin.ModelAdmin):
    list_display=('club','name','price','duration')
    list_filter=('club',)



admin.site.register(Club, ClubAdmin)
admin.site.register(Say, SayAdmin)
admin.site.register(Offers, OffersAdmin)
admin.site.register(Package, PackageAdmin)
