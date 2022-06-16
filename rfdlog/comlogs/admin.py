from django.contrib import admin
from .models import Supplies_fict
# Register your models here.
class SupAdminViews(admin.ModelAdmin):
    list_display = ['supplies_type','brand_name','org_number','serial_number','date_recive','acquisition_type','status_sup','other']
    list_filter = ['supplies_type']
    #list_editable = ['brand_name'] 

admin.site.register(Supplies_fict, SupAdminViews)