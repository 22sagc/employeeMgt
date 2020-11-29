from django.contrib import admin
from employee import models
# Register your models here.
class Manager(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['id']

admin.site.register(models.Employee,Manager)