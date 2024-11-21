from django.contrib import admin

from .models import *
# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    search_fields = ["id"]

class EndPointAdmin(admin.ModelAdmin):
    search_fields = ["id"]

class PermisionAdmin(admin.ModelAdmin):
    search_fields = ["id"]

admin.site.register(Document, DocumentAdmin)
admin.site.register(EndPoint, EndPointAdmin)
admin.site.register(Permision, PermisionAdmin)