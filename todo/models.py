from django.db import models

# Create your models here.


class Zadacha(models.Model):
	Opisanie = models.CharField(max_length=150)
	zz = 'Zaplanirovana'
	vv = 'Vypolneno'
	oo = 'Otmeneno'
	choice_status = (
			(zz,'Zaplanirovana'),
			(vv, 'Vypolneno'),
			(oo, 'Otmeneno')
		)
	status = models.CharField(max_length=100, choices = choice_status)