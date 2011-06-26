from django.contrib import admin
from models import NavigationItem, NavigationTree
import re

url_re = re.compile(r'^(https??://([a-zA-Z0-9]+\.)+[a-zA-Z0-9]([:@][a-zA-Z0-9@%-_\.]){0,2})?/\S*$')

class NavigationItemAdmin(admin.ModelAdmin):
    list_filter = ('tree',)
    list_display = ('label','title','location','staff_only','guests_only','guests_hidden',)

class NavigationTreeAdmin(admin.ModelAdmin):
    pass

admin.site.register(NavigationItem, NavigationItemAdmin)
admin.site.register(NavigationTree, NavigationTreeAdmin)
