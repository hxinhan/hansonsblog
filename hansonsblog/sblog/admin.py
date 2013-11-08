# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Category,Tag,Blog,ClientInfo

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name',)}

class BlogAdmin(admin.ModelAdmin):
    list_display = ['caption','slug','id','counts','category','publish_time']
    list_filter = ['caption']
    prepopulated_fields = {'slug':('caption',)}
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)

class ClientInfoAdmin(admin.ModelAdmin):
    list_display = ['ip_address','time']
    ordering = ('-time',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Tag)
admin.site.register(ClientInfo,ClientInfoAdmin)
