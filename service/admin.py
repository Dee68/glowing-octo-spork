from django.contrib import admin
from .models import Service
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title','available','icon_status']
    list_editable = ['available']
    prepopulated_fields = {'slug':('title',)} 
admin.site.register(Service,ServiceAdmin)