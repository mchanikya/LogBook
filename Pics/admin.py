from django.contrib import admin

# Register your models here.
from .models import MobileAlbum,DirectAlbum,Mobilepics,DirectUpload

admin.site.register(MobileAlbum)
admin.site.register(DirectAlbum)
admin.site.register(Mobilepics)
admin.site.register(DirectUpload)
