from django.db import models
from django.utils import timezone

class Input(models.Model):
	author = models.ForeignKey('auth.User')
	inURL = models.CharField(max_length=200)

	def __str__(self):
		return self.inURL