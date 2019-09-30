from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


# Register your models here.


# admin.site.register(Desktop)
# admin.site.register(Laptop)
# admin.site.register(Mobile)


@admin.register(Desktop, Laptop, Mobile)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id',)
