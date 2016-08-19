from django.db import models
from django.utils import timezone
from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# This code is triggered whenever a new user has been created and saved to the database

@receiver(post_save, sender='auth.User')
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Input(models.Model):
	author = models.ForeignKey('auth.User')
	inURL = models.CharField(max_length=200)
	status = models.CharField(max_length=200, default='')
	destination = models.CharField(max_length=200, default='')
	title = models.CharField(max_length=200, default='')
	exp = models.CharField(max_length=200, default='')
	wayurl = models.CharField(max_length=200, default='')
	waytime = models.CharField(max_length=200, default='')
	imgUrl = models.CharField(max_length=200, default='')

	def __str__(self):
		return self.inURL


