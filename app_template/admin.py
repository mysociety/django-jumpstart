from django.contrib import admin
from {{ app_name }} import models

# tweak to taste - simple at the top and more custom below


# admin.site.register(models.FooBar)



# class FooBarAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ["name"]}
#     list_display  = [ 'slug', 'name', ]
#     search_fields = ['name']
# 
# admin.site.register( models.FooBar, FooBarAdmin )
