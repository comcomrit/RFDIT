from django.contrib import admin
from .models import ExamScore, AllStudent, Profile, DocumentUpload, Supplies_fict
from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, \
    SliderNumericFilter

# Register your models here.
admin.site.site_title = 'ระบบบริหารจัดการพัสดุ ศทส.'
admin.site.site_header = 'ระบบบริหารจัดการพัสดุ ศทส.'
#admin.site.register(ExamScore)

class StudentAdmin(admin.ModelAdmin):
	list_display = ['student_id','level','student_name','student_tel']
	list_filter = ['level']
	list_editable = ['student_tel']



class Documentlist(admin.ModelAdmin):
	list_display = ['document_name','level','document','other']
	list_filter = ['level']
	list_editable = ['other']

#admin.site.register(AllStudent, StudentAdmin)
#admin.site.register(DocumentUpload,Documentlist)
#admin.site.register(Profile)



#admin.site.register(Supplies_fict)


class SupAdminViews(admin.ModelAdmin):
    list_display = ['orgs','supplies_type','brand_name','org_number','serial_number','date_recive','acquisition_type','status_sup','location','other','sup_img']
    list_filter = (('supplies_type'),('status_sup'),('date_recive', RangeNumericFilter),'orgs')
    #list_editable = ['brand_name'] 

admin.site.register(Supplies_fict, SupAdminViews)