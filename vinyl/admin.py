from django.contrib import admin

from .models import Artist, Album, Disk, Label

admin.site.register(Artist)
admin.site.register(Disk)
admin.site.register(Album)
admin.site.register(Label)

