from django.db import models
from django.contrib import admin
	
class ClassComment(models.Model):
	fbid = models.IntegerField();
	department = models.CharField(max_length=50)
	classNum = models.IntegerField()
	className = models.CharField(max_length=200)
	comment_text = models.TextField()
	
	#year = models.IntegerField()
	#SEMESTER_OPTIONS = (('F','Fall'),
	#					('W','Winter'),
	#					('S','Spring/Summer'))
	#semester = models.CharField(max_length=1, choices=SEMESTER_OPTIONS)
	
