from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from .models import Input
import os, sys
from urllib.request import urlopen
from bs4 import BeautifulSoup 
import urllib.request as rq
import requests
import urllib
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from .forms import PostForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required
from urlExp.models import Input
from urlExp.serializers import UrlsSerializer
from selenium import webdriver
from boto.s3.connection import S3Connection, Bucket, Key
from boto.s3.key import Key
from ratelimit.decorators import ratelimit


#@login_required
def post_list(request):
	url = Input.objects.all()
	return render(request, 'urlExp/post_list.html', {'url': url})
	
@login_required
def post_detail(request, pk):
	post = get_object_or_404(Input, pk=pk)
	return render(request, 'urlExp/post_detail.html', {'post': post})

def delete(request, pk):
	post = get_object_or_404(Input, pk=pk)
	screenshot(post.imgUrl,2)
	post = post.delete()
	return HttpResponseRedirect(reverse('post_list'))

def title(websites):
	website = str(websites)
	html = requests.get(website)
	soup = BeautifulSoup(html.text, "html.parser")
	soup2 = soup.title.string
	return soup2

def num(websites):
	website = str(websites)
	html = requests.get(website)
	soup = BeautifulSoup(html.text, "html.parser")
	soup2 = len(soup.find_all('img'))
	return soup2
def fin(websites):
	r = requests.get(websites, allow_redirects=True)
	out = websites + '->' + str(r.url)
	return out

@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.title = title(str(request.POST['inURL']))
			post.status = requests.get(str(request.POST['inURL']))
			post.exp = num(str(request.POST['inURL']))
			post.destination = fin(str(request.POST['inURL']))
			post.wayurl = wayUrl(str(request.POST['inURL']))
			post.waytime = wayTime(str(request.POST['inURL']))
			post.imgUrl = screenshot(str(request.POST['inURL']),1)
			post.save()
			return redirect('post_detail', pk=post.pk)

	else:
		form = PostForm()
	return render(request, 'urlExp/post_edit.html', {'form': form})


def screenshot(request,val):
	if val == 1 :
		conn = S3Connection('##', '##')
		bucket = conn.get_bucket('lheston-bucket')
		k = Key(bucket)
		k.key = '//lab3' + request + '_toS3.png'
		driver = webdriver.PhantomJS() # or add to your PATH                                                                
		driver.set_window_size(1024, 768) # optional                                                                        
		driver.get(request)
		driver.save_screenshot('tempfile.png')
		driver.quit
		file1 = open('tempfile.png', 'rb')
		os.remove('tempfile.png')
		k.set_contents_from_file(file1)
		driver.quit
		return str(request + '_toS3.png')
	elif val == 2:
		text = '/lab3' + request
		conn = S3Connection('##', '##')
		S3_BUCKET_NAME = 'lheston-bucket'
		bucket = Bucket(conn, S3_BUCKET_NAME)
		bucket = bucket.delete_key(text)
		#bucket.delete_key('/lab3/' + request.split(':')[1])
		#k = Key(b)
		#k.name = k.get_key(text)
		#b.delete_key(k)
		#k.name = k.get_key(text)
		#b.delete_key(k)
		#b.delete_key('//lab3' + request.split(':')[1] + '_toS3.png')
	else:
		return str('incorrect input')





def wayUrl(request):
	r = requests.get('http://archive.org/wayback/available?url=' + request).json()
	return r['archived_snapshots']['closest']['url']

def wayTime(request):
	DateFormat = '%Y%m%d%H%M%S'
	r = requests.get('http://archive.org/wayback/available?url=' + request).json()
	r = r['archived_snapshots']['closest']['timestamp']
	dt = datetime.strptime(r,DateFormat)
	return dt


@ratelimit(key='ip', rate='10/m', block=True)
@api_view(['GET', 'POST'])
def url_list(request, format=None):
	"""
	Lists all urls, or create a url.
	"""
	if request.method =='GET':
		urlsdata = Input.objects.all()
		serializer = UrlsSerializer(urlsdata, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = UrlsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@ratelimit(key='ip', rate='10/m', block=True)
@api_view(['GET', 'PUT', 'DELETE'])
def url_detail(request, pk, format=None):
	"""
	Retrive, update or delete a book
	"""
	try:
		 users = Input.objects.get(pk=pk)
	except Input.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = UrlsSerializer(users)
		return Response(serializer.data)
	elif request.method == 'PUT':
		serializer = UrlsSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.tatus.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		screenshot(request,2)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



