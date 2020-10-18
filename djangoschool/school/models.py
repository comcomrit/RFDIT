from django.db import models

class ExamScore(models.Model):

	allsubject = (('คณิตศาสตร์','คณิตศาสตร์'),
				  ('วิทยาศาสตร์','วิทยาศาสตร์'),
				  ('ศิลป','ศิลป'),
				  ('ภาษาอังกฤษ','ภาษาอังกฤษ'),
				  ('ฟิสิกส์','ฟิสิกส์'),
				  ('ชีววิทยา','ชีววิทยา'))

	subject = models.CharField(max_length=200, choices=allsubject, default='คณิตศาสตร์')
	student_name = models.CharField(max_length=200)
	score = models.IntegerField(default=0)

	def __str__(self):
		return self.student_name +'-'+ self.subject +'-' + str(self.score)


class AllStudent(models.Model):
	levellist = ( ('ม.1','ม.1'),
				('ม.2','ม.2'),
			  	('ม.3','ม.3'),
			  	('ม.4','ม.4'),
			  	('ม.5','ม.5'),
			  	('ม.6','ม.6'))

	level = models.CharField(max_length=100, choices=levellist, default='ม.1')
	student_name = models.CharField(max_length=200)
	student_id = models.CharField(max_length=200)
	student_tel = models.CharField(max_length=200,blank=True,null=True)
	parent_name = models.CharField(max_length=200,blank=True,null=True)
	parent_tel = models.CharField(max_length=200,blank=True,null=True)
	other = models.TextField(blank=True,null=True)
	photo = models.ImageField(upload_to="studentphoto",blank=True,null=True)

	def __str__(self):
		return '{}-{}'.format(self.student_id,self.student_name)


from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	photoprofile = models.ImageField(default='default.png',upload_to='photo_profile',blank=True,null=True)
	usertype = models.CharField(max_length=100,null=True,blank=True,default='student')

	def __str__(self):
		return f'{self.user.username} Profile'


class DocumentUpload(models.Model):
	levellist = ( ('ม.1','ม.1'),
			  ('ม.2','ม.2'),
			  ('ม.3','ม.3'),
			  ('ม.4','ม.4'),
			  ('ม.5','ม.5'),
			  ('ม.6','ม.6'))

	level = models.CharField(max_length=100, choices=levellist, default='ม.1')
	document_name = models.CharField(max_length=100)
	document = models.FileField(upload_to='alldocument')
	other = models.TextField(blank=True,null=True)
	
	def __str__(self):
		return '{}-{}'.format(self.document_name,self.other)


# Create your models here.
class Supplies_fict(models.Model):
    alltype = ((0,'คอมพิวเตอร์ตั้งโต๊ะ'),
				  (1,'คอมพิวเตอร์โน๊ตบุ๊ค'),
				  (2,'เครื่องสำรองไฟ UPS'),
				  (3,'เครื่องพิมพ์ ขาวดำ LED'),
				  (4,'เครื่องพิมพ์ สี LED'),
				  (5,'เครื่องสแกน Scanner'),
				  (6,'เครื่องพิมพ์ฉีดหมึก Ink jet'),
				  (7,'Scanner'),
				  (8,'เครื่องพิมพ์ Multifunction'),
				  (9,'คอมพิวเตอร์แท็ปแล็ต Tablet'),
				  (10,'เครื่องพิมพ์แผนที่ plotter')
				  )

    allacquisition = ((0,'ได้รับจัดสรรตามปีงบประมาณ'),
				    (1,'เช่าซื้อ/บริจาค'))

    allstatus = ((0,'ดี'),
			    (1,'ชำรุด'),
                (2,'รอจำหน่าย'),
                (3,'จำหน่ายแล้ว'))

    orgslv = (('ส่วนภูมิภาค',(
                (99,'เลือกหน่วยงาน'),
				(0,'สำนักจัดการทรัพยากรป่าไม้ที่ 1 (เชียงใหม่)'),
			    (1,'สำนักจัดการทรัพยากรป่าไม้ที่ 1 สาขาแม่ฮ่องสอน'),
                (2,'สำนักจัดการทรัพยากรป่าไม้ที่ 2 (เชียงราย)'),
                (3,'สำนักจัดการทรัพยากรป่าไม้ที่ 3 (ลำปาง)'),
				(4,'สำนักจัดการทรัพยากรป่าไม้ที่ 3 สาขาแพร่'),
			    (5,'สำนักจัดการทรัพยากรป่าไม้ที่ 4 (ตาก)'),
                (6,'สำนักจัดการทรัพยากรป่าไม้ที่ 4 สาขานครสวรรค์'),
                (7,'สำนักจัดการทรัพยากรป่าไม้ที่ 4 สาขาพิษณุโลก'),
				(8,'สำนักจัดการทรัพยากรป่าไม้ที่ 5 (สระบุรี)'),
			    (9,'สำนักจัดการทรัพยากรป่าไม้ที่ 6 (อุดรธานี)'),
                (10,'สำนักจัดการทรัพยากรป่าไม้ที่ 6 สาขานครพนม'),
                (11,'สำนักจัดการทรัพยากรป่าไม้ที่ 7 (ขอนแก่น)'),
				(12,'สำนักจัดการทรัพยากรป่าไม้ที่ 7 สาขาอุบลราชธานี'),
			    (13,'สำนักจัดการทรัพยากรป่าไม้ที 8 (นครราชสีมา)'),
                (14,'สำนักจัดการทรัพยากรป่าไม้ที่ 9 (ชลบุรี)'),
                (15,'สำนักจัดการทรัพยากรป่าไม้ที่ 9 สาขาปราจีนบุรี'),
				(16,'สำนักจัดการทรัพยากรป่าไม้ที่ 10 (ราชบุรี)'),
				(17,'สำนักจัดการทรัพยากรป่าไม้ที่ 10 สาขาเพชรบุรี'),
			    (18,'สำนักจัดการทรัพยากรป่าไม้ที่ 11 (สุราษฎร์ธานี)'),
                (19,'สำนักจัดการทรัพยากรป่าไม้ที่ 12 (นครศรีธรรมราช)'),
                (20,'สำนักจัดการทรัพยากรป่าไม้ที่ 12 สาขากระบี่'),
				(21,'สำนักจัดการทรัพยากรป่าไม้ที่ 13 (สงขลา)'),
			    (22,'สำนักจัดการทรัพยากรป่าไม้ที่ 13 สาขานราธิวาส'),
                )), 
                ('ส่วนกลาง',(
				(23,'สำนักกฎหมาย'),
			    (24,'สำนักการอนุญาต'),
                (25,'สำนักบริหารกลาง'),
                (26,'สำนักจัดการป่าชุมชน'),
				(27,'สำนักจัดการที่ดินป่าไม้'),
			    (28,'สำนักส่งเสริมการปลูกป่า'),
                (29,'สำนักเศรษฐกิจการป่าไม้'),
                (30,'สำนักการป่าไม้ต่างประเทศ'),
				(31,'สำสำนักแผนงานและสารสนเทศ'),
			    (32,'สำนักวิจัยและพัฒนาการป่าไม้'),
                (33,'สำนักป้องกันรักษาป่าและควบคุมไฟป่า'),
                (34,'สำนักโครงการพระราชดำริและกิจการพิเศษ'),
				(35,'กลุ่มตรวจสอบภายใน'),
			    (36,'กลุ่มพัฒนาระบบบริหาร'),
                (37,'กลุ่มงานคุ้มครองจริยธรรมกรมป่าไม้'),
                (38,'ศูนย์เทคโนโลยีสารสนเทศและการสื่อสาร'),
				)),
				)
    orgs = models.IntegerField(verbose_name = 'หน่วยงาน',max_length=100, choices=orgslv, default=99)
    supplies_type = models.IntegerField(verbose_name = 'รายการครุภัณฑ์',max_length=100, choices=alltype, default=0)
    brand_name = models.CharField(verbose_name = 'ยี่ห้อ/รุ่น',max_length=200, blank=True, null=True)
    org_number = models.CharField(verbose_name = 'เลขครุภัณฑ์ (ปม)',max_length=200, blank=True, null=True)
    serial_number = models.CharField(verbose_name = 'หมายเลขเครื่อง (S/N)',max_length=200, blank=True, null=True)
    date_recive = models.IntegerField(verbose_name = 'ปีที่ได้รับ',max_length=4, blank=True, null=True)
    acquisition_type = models.IntegerField(verbose_name = 'วีธีการได้มา',max_length=100, choices=allacquisition, default=0)
    status_sup = models.IntegerField(verbose_name = 'สถานะ',max_length=100, choices=allstatus, default=0)
    location = models.CharField(verbose_name = 'ที่ตั้ง ส่วน/ฝ่าย',max_length=200, blank=True, null=True)
    other = models.CharField(verbose_name = 'หมายเหตุ',max_length=200,blank=True,null=True)
    sup_img = models.ImageField(verbose_name = 'รูปครุภัณฑ์',default='default.png',upload_to='supplies_img',blank=True,null=True)
    

    def __str__(self):
    	return '{} {} {} {} {} {} {} {} {} {} {}'.format(self.orgs,self.supplies_type,self.brand_name,self.serial_number,self.org_number,self.date_recive,self.acquisition_type, self.status_sup, self.location, self.other,self.sup_img)

