from django.db import models
from django.utils import timezone
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Input(models.Model):
	author = models.ForeignKey('auth.User')
	inURL = models.CharField(max_length=200)
	status = models.CharField(max_length=200, default='')
	destination = models.CharField(max_length=200, default='')
	title = models.CharField(max_length=200, default='')

	def __str__(self):
		return self.inURL



def title(website):
	soup = BeautifulSoup(urlopen("https://www.google.com"))
	return soup.title.string