from django.db import models
from django.contrib import admin
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


class Class(models.Model):
	department = models.CharField(max_length=50)
	classNum = models.IntegerField()
	className = models.CharField(max_length=200)

class ClassComment(models.Model):
	fbid = models.IntegerField();
	classobj = models.ForeignKey(Class)
	year = models.IntegerField()
	SEMESTER_OPTIONS = (('F','Fall'),
						('W','Winter'),
						('S','Spring/Summer'))
	semester = models.CharField(max_length=1, choices=SEMESTER_OPTIONS)
	comment_text = models.TextField()

