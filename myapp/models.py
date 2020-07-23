from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

	user = models.OneToOneField(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username


class t8_9(models.Model):

	halls=models.CharField(max_length=20,primary_key=True)
	block=models.CharField(max_length=20,default='NAB')
	monday=models.CharField(max_length=20,default='empty')
	tuesday=models.CharField(max_length=20,default='empty')
	wednesday=models.CharField(max_length=20,default='empty')
	thursday=models.CharField(max_length=20,default='empty')
	friday=models.CharField(max_length=20,default='empty')
	types=models.CharField(max_length=1,default='L')
	monday_copy=models.CharField(max_length=20,default='empty')
	tuesday_copy=models.CharField(max_length=20,default='empty')
	wednesday_copy=models.CharField(max_length=20,default='empty')
	thursday_copy=models.CharField(max_length=20,default='empty')
	friday_copy=models.CharField(max_length=20,default='empty')


	# class Meta:
	# 	db_table='t8_9'

class t9_10(models.Model):
	halls=models.CharField(max_length=20,primary_key=True)
	block=models.CharField(max_length=20,default='NAB')
	monday=models.CharField(max_length=20,default='empty')
	tuesday=models.CharField(max_length=20,default='empty')
	wednesday=models.CharField(max_length=20,default='empty')
	thursday=models.CharField(max_length=20,default='empty')
	friday=models.CharField(max_length=20,default='empty')
	types=models.CharField(max_length=1)
	monday_copy=models.CharField(max_length=20,default='empty')
	tuesday_copy=models.CharField(max_length=20,default='empty')
	wednesday_copy=models.CharField(max_length=20,default='empty')
	thursday_copy=models.CharField(max_length=20,default='empty')
	friday_copy=models.CharField(max_length=20,default='empty')


	# class Meta:
	# 	db_table='t9_10'

class t10_11(models.Model):
	halls=models.CharField(max_length=20,primary_key=True)
	block=models.CharField(max_length=20,default='NAB')
	monday=models.CharField(max_length=20,default='empty')
	tuesday=models.CharField(max_length=20,default='empty')
	wednesday=models.CharField(max_length=20,default='empty')
	thursday=models.CharField(max_length=20,default='empty')
	friday=models.CharField(max_length=20,default='empty')
	types=models.CharField(max_length=1)
	monday_copy=models.CharField(max_length=20,default='empty')
	tuesday_copy=models.CharField(max_length=20,default='empty')
	wednesday_copy=models.CharField(max_length=20,default='empty')
	thursday_copy=models.CharField(max_length=20,default='empty')
	friday_copy=models.CharField(max_length=20,default='empty')


class t11_12(models.Model):
	halls=models.CharField(max_length=20,primary_key=True)
	block=models.CharField(max_length=20,default='NAB')
	monday=models.CharField(max_length=20,default='empty')
	tuesday=models.CharField(max_length=20,default='empty')
	wednesday=models.CharField(max_length=20,default='empty')
	thursday=models.CharField(max_length=20,default='empty')
	friday=models.CharField(max_length=20,default='empty')
	types=models.CharField(max_length=1)
	monday_copy=models.CharField(max_length=20,default='empty')
	tuesday_copy=models.CharField(max_length=20,default='empty')
	wednesday_copy=models.CharField(max_length=20,default='empty')
	thursday_copy=models.CharField(max_length=20,default='empty')
	friday_copy=models.CharField(max_length=20,default='empty')


class t12_1(models.Model):
	halls=models.CharField(max_length=20,primary_key=True)
	block=models.CharField(max_length=20,default='NAB')
	monday=models.CharField(max_length=20,default='empty')
	tuesday=models.CharField(max_length=20,default='empty')
	wednesday=models.CharField(max_length=20,default='empty')
	thursday=models.CharField(max_length=20,default='empty')
	friday=models.CharField(max_length=20,default='empty')
	types=models.CharField(max_length=1)
	monday_copy=models.CharField(max_length=20,default='empty')
	tuesday_copy=models.CharField(max_length=20,default='empty')
	wednesday_copy=models.CharField(max_length=20,default='empty')
	thursday_copy=models.CharField(max_length=20,default='empty')
	friday_copy=models.CharField(max_length=20,default='empty')


class t1_2(models.Model):

	halls=models.CharField(max_length=20,primary_key=True)
	block=models.CharField(max_length=20,default='NAB')
	monday=models.CharField(max_length=20,default='empty')
	tuesday=models.CharField(max_length=20,default='empty')
	wednesday=models.CharField(max_length=20,default='empty')
	thursday=models.CharField(max_length=20,default='empty')
	friday=models.CharField(max_length=20,default='empty')
	types=models.CharField(max_length=1)
	monday_copy=models.CharField(max_length=20,default='empty')
	tuesday_copy=models.CharField(max_length=20,default='empty')
	wednesday_copy=models.CharField(max_length=20,default='empty')
	thursday_copy=models.CharField(max_length=20,default='empty')
	friday_copy=models.CharField(max_length=20,default='empty')


class t2_3(models.Model):
	halls=models.CharField(max_length=20,primary_key=True)
	block=models.CharField(max_length=20,default='NAB')
	monday=models.CharField(max_length=20,default='empty')
	tuesday=models.CharField(max_length=20,default='empty')
	wednesday=models.CharField(max_length=20,default='empty')
	thursday=models.CharField(max_length=20,default='empty')
	friday=models.CharField(max_length=20,default='empty')
	types=models.CharField(max_length=1)
	monday_copy=models.CharField(max_length=20,default='empty')
	tuesday_copy=models.CharField(max_length=20,default='empty')
	wednesday_copy=models.CharField(max_length=20,default='empty')
	thursday_copy=models.CharField(max_length=20,default='empty')
	friday_copy=models.CharField(max_length=20,default='empty')

	
class t3_4(models.Model):
	halls=models.CharField(max_length=20,primary_key=True)
	block=models.CharField(max_length=20,default='NAB')
	monday=models.CharField(max_length=20,default='empty')
	tuesday=models.CharField(max_length=20,default='empty')
	wednesday=models.CharField(max_length=20,default='empty')
	thursday=models.CharField(max_length=20,default='empty')
	friday=models.CharField(max_length=20,default='empty')
	types=models.CharField(max_length=1)
	monday_copy=models.CharField(max_length=20,default='empty')
	tuesday_copy=models.CharField(max_length=20,default='empty')
	wednesday_copy=models.CharField(max_length=20,default='empty')
	thursday_copy=models.CharField(max_length=20,default='empty')
	friday_copy=models.CharField(max_length=20,default='empty')


class t4_5(models.Model):
	halls=models.CharField(max_length=20,primary_key=True)
	block=models.CharField(max_length=20,default='NAB')
	monday=models.CharField(max_length=20,default='empty')
	tuesday=models.CharField(max_length=20,default='empty')
	wednesday=models.CharField(max_length=20,default='empty')
	thursday=models.CharField(max_length=20,default='empty')
	friday=models.CharField(max_length=20,default='empty')
	types=models.CharField(max_length=1)
	monday_copy=models.CharField(max_length=20,default='empty')
	tuesday_copy=models.CharField(max_length=20,default='empty')
	wednesday_copy=models.CharField(max_length=20,default='empty')
	thursday_copy=models.CharField(max_length=20,default='empty')
	friday_copy=models.CharField(max_length=20,default='empty')


class update(models.Model):
	day=models.CharField(max_length=20,primary_key=True)
	date=models.CharField(max_length=20,default='')




