from django.db import models
from django.contrib import admin


class Department(models.Model):
	code = models.CharField(max_length=8)
	fullName = models.CharField(max_length=200)


class Class(models.Model):
	department = models.ForeignKey(Department)
	classNum = models.IntegerField()
	className = models.CharField(max_length=200)


class Professor(models.Model):
	name = models.CharField(max_length=100)


class ClassComment(models.Model):
	#foreign key to facebook user
	classobj = models.ForeignKey(Class)
	professorobj = models.ForeignKey(Professor)
	year = models.IntegerField()
	SEMESTER_OPTIONS = (('F','Fall'),
						('W','Winter'),
						('S','Spring/Summer'))
	semester = models.CharField(max_length=1, choices=SEMESTER_OPTIONS)
	liked = models.BooleanField()
	difficulty_rating = models.SmallIntegerField()
	worthwhile_rating = models.SmallIntegerField()
	time_commitment_rating = models.SmallIntegerField()
	comment_text = models.TextField()


def addClass(department_code, department_name, class_num, prof_name):
	#adds department, if necessary
	if Department.objects.filter(code=department_code).count() < 1:
		print 'Adding department'
		d=Department(code=department_code, fullName=department_name)
		d.save() 

	#adds class, if necessary
	if Class.objects.filter(classNum=class_num).count() < 1:
		print 'Adding department'
		d=Department(code=department_code, fullName=department_name)
		d.save() 


	return
