from django.db import models

# Create your models here.
class Supplies_fict(models.Model):
    alltype = ((0,'คอมพิวเตอร์ตั้งโต๊ะ'),
				  (1,'คอมพิวเตอร์พกพา'),
				  (2,'เครื่องสำรองไฟ'),
				  (3,'เครื่องพิมพ์ ขาวดำ LED'),
				  (4,'เครื่องพิมพ์ สี LED'),
				  (5,'เครื่องสแกน Scanner'))

    allacquisition = ((0,'ได้รับจัดสรรตามปีงบประมาณ'),
				    (1,'เช่าซื้อ/บริจาค'))

    allstatus = ((0,'ดี'),
			    (1,'ชำรุด'),
                (2,'เสีย'),
                (3,'รอจำหน่าย'))

    supplies_type = models.IntegerField(max_length=100, choices=alltype, default=0)
    brand_name = models.CharField(max_length=200, blank=True, null=True)
    org_number = models.CharField(max_length=200, blank=True, null=True)
    serial_number = models.CharField(max_length=200, blank=True, null=True)
    date_recive = models.IntegerField(max_length=4, blank=True, null=True)
    acquisition_type = models.IntegerField(max_length=100, choices=allacquisition, default=0)
    status_sup = models.IntegerField(max_length=100, choices=allstatus, default=0)
    location = models.CharField(max_length=200, blank=True, null=True)
    other = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
    	return '{} {} {} {} {} {} {} {}'.format(self.supplies_type,self.brand_name,self.serial_number,self.org_number,self.date_recive,self.acquisition_type, self.status_sup,self.location, self.other)

