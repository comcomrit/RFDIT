from django.db import models

# Create your models here.
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
    
#class Register(models.Model):
