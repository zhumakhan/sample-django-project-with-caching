from django.db import models
from django.utils.translation import gettext_lazy as _
from ..helpers.constants import CURRENCIES,KZT
# Create your models here.
class Stream(models.Model):
	start_time = models.DateTimeField(null=True,blank=True,verbose_name=_('Start Time'))
	end_time = models.DateTimeField(null=True,blank=True,verbose_name=_('End Time'))
	url = models.CharField(max_length=2048,null=True,blank=True,verbose_name=_('URL'))
	title = models.CharField(max_length=2048,null=False,blank=False,verbose_name=_('title'),default='Untitled')
	cover_image = models.FileField(verbose_name='фото для обложки', blank=True, null=True)
	image = models.FileField(verbose_name='Фото', blank=True, null=True)
	currency = models.CharField(max_length=250, choices=CURRENCIES, blank=False, null=False,
                              verbose_name=_('currency'),default=KZT)
	ticket_cost = models.FloatField(null=False,blank=False,verbose_name=_('ticket cost'))
	current = models.BooleanField(default=False)
	past = models.BooleanField(default=False)
	
	def __str__(self):
		return "{}.  {}".format(self.id, self.title)

class Code(models.Model):
	code = models.CharField(max_length=255,db_index=True,verbose_name=_('Code'),null=False,blank=False)
	stream = models.ForeignKey(Stream, null=False, db_index=True,on_delete=models.CASCADE, blank=False,
		verbose_name=_('Stream'), related_name='codes')
	email = models.CharField(max_length=255,null=True,blank=True,db_index=True,verbose_name=_('Email'))
	valid = models.BooleanField(default=True,db_index=True)
	
	class Meta:
		unique_together = ('code', 'stream')

	def __str__(self):
		return "{}.  {}".format(self.id,self.code)