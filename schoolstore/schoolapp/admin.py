from django.contrib import admin

# Register your models here.
from .models import Stream, Product


class StreamAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Stream,StreamAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'fees', 'seats', 'available', 'created', 'updated']
    list_editable = ['fees', 'seats', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(Product, ProductAdmin)