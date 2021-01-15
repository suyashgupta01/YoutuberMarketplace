from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'myphoto', 'first_name', 'role', 'created_date')
    list_display_links = ('first_name', ) # this is a python tuple & if there's only one item then there has to be a , after it
    search_fields = ('first_name', 'role')
    list_filter = ('role', )

    def myphoto(self, object):
        return format_html('<img  src="{}" width="50" />'.format(object.first_name))


# Register your models here.
admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)