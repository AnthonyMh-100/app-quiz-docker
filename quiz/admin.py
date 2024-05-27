from django.contrib import admin
from .models import Product


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ['name','imagen','description','price','stock']
    
