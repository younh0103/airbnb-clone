from django.contrib import admin
from . import models

@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    
    """ List Model Definition """
    
    pass

