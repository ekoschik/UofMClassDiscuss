from django.db import models
from django.contrib import admin
from datetime import date
	
class ClassComment(models.Model):
	fbid = models.IntegerField();
	department = models.CharField(max_length=50)
	classNum = models.IntegerField()
	className = models.CharField(max_length=200)
	comment_text = models.TextField()
	prof = models.CharField(max_length=50, null=False)
	year = models.IntegerField(null=False, default=(date.today().year + 1))
	SEMESTER_OPTIONS = (('F','Fall'),
						('W','Winter'),
						('S','Spring/Summer'))
	semester = models.CharField(max_length=1, choices=SEMESTER_OPTIONS, null=False)
	difficulty = models.IntegerField(null=False, default=3)
	workload = models.IntegerField(null=False, default=3)
	recommended = models.BooleanField()
