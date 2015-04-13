from django.db import models

# Create your models here.
class leds(models.Model):
	username = models.CharField(max_length=32)
	name = models.CharField(max_length=10)
	userid = models.IntegerField(default=0)
	x = models.IntegerField()
	y = models.IntegerField()
	status = models.IntegerField(default=0)
	radius = models.IntegerField(default=15)
	color = models.CharField(max_length=15)
	intesity = models.IntegerField(default=15)
	group_type = models.IntegerField(default=1)
	group_name = models.CharField(max_length=20)
	r = models.IntegerField(default=255)
	g = models.IntegerField(default=255)
	b = models.IntegerField(default=255)
	temp1 = models.CharField(max_length=20)
	temp2 = models.IntegerField(default=0)
	def __unicode__(self):
		return  self.name

class ledsgroup(models.Model):
	username= models.CharField(max_length=32)
	name = models.CharField(max_length=10)
	groupstatus = models.IntegerField(default=0)
	groupintensity = models.IntegerField(default=5)
	groupcolor = models.CharField(max_length=10)
	groupname = models.CharField(max_length=10)
	def __unicode__(self):
		return self.name

class group_name(models.Model):
	username = models.CharField(max_length=32)
	groupname = models.CharField(max_length=10)
	groupstatus = models.IntegerField(default=0)
	groupintensity = models.IntegerField(default=5)
	groupcolor = models.CharField(max_length=10)
	quantity = models.IntegerField(default=0)
	def __unicode__(self):
		return self.groupname

class date_temp(models.Model):
	username = models.CharField(max_length=32)
	name = models.CharField(max_length=10)
	on_date = models.DateField(auto_now_add=True, blank=True)
	off_date = models.DateField(auto_now_add=True, blank=True)
	day = models.DateField(auto_now_add=True, blank=True)
	on_time = models.TimeField(auto_now_add=True, blank=True)
	off_time = models.TimeField(auto_now_add=True, blank=True)
	status = models.IntegerField(default=0)
	raw_time = models.TimeField(auto_now_add=True, blank=True)
	total_time = models.FloatField(default=0)
	voltage = models.FloatField(default=1)
	current = models.FloatField(default=1)
	intesity = models.IntegerField(default=1)
	units_used = models.FloatField(default=0)
	def __unicode__(self):
		return self.username

class temp123(models.Model):
	a = models.CharField(max_length=10)
	b = models.IntegerField(default=0)
	def __unicode__(self):
		return self.a

class sample(models.Model):
	num = models.IntegerField(default=0)