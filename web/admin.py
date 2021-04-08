from django.contrib import admin
from .models import berita,galery,kontak,agenda,kontak
# Register your models here.

admin.site.register(berita)
admin.site.register(kontak)

admin.site.register(agenda)
admin.site.register(galery)