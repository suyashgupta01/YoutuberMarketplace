from django.contrib import admin
from .models import Youtuber

# Register your models here.

class YtAdmin(admin.ModelAdmin): # admin panel pe kya kaise dikhega ye change krre h 
    list_display = ('id', 'name', 'subs_count', 'is_featured') 
    search_fields = ('name', 'camera_type')
    list_filter = ('city', 'camera_type')
    list_display_links = ('id', 'name') # these will be clickable
    list_editable = ('is_featured',) # directly is_featured ko edit krdo bina individual entry pe jaaye 

admin.site.register(Youtuber, YtAdmin)