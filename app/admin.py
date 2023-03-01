from django.contrib import admin
from .models import *
# Register your models here.

@admin.register((info))
class infoModelAdmin(admin.ModelAdmin):
    list_display= ['id','Name','Email','Subject','Message']

@admin.register((Product))
class ProductModelAdmin(admin.ModelAdmin):
    list_display= ['id','upload_photo','description']