from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from .models import Input
from urllib.request import urlopen
from bs4 import BeautifulSoup 
import urllib.request as rq
import requests
import urllib
from datetime import datetime
from .forms import PostForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required

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
			post.save()
			return redirect('post_detail', pk=post.pk)

	else:
		form = PostForm()
	return render(request, 'urlExp/post_edit.html', {'form': form})


def wayUrl(request):

	r = requests.get('http://archive.org/wayback/available?url=' + request).json()
	return r['archived_snapshots']['closest']['url']

def wayTime(request):
	DateFormat = '%Y%m%d%H%M%S'
	r = requests.get('http://archive.org/wayback/available?url=' + request).json()
	r = r['archived_snapshots']['closest']['timestamp']
	dt = datetime.strptime(r,DateFormat)
	return dt
