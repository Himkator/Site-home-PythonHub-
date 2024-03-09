from django.contrib import admin
from goods.models import *
# Register your models here.
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display=['name', 'slug']
    prepopulated_fields={'slug':('name',)}
    
    

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}