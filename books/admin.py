from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name","slug")
    prepopulated_fields = {"slug":("name",)} 

    
admin.site.register(Category)
admin.site.register(TgAdmin)