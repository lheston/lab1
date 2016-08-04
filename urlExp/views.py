from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Input
from urllib.request import urlopen
from bs4 import BeautifulSoup 
import urllib.request as rq
import requests
import urllib
from .forms import InputForm


def post_list(request):
	url = Input.objects.all()
	#for i in Input.objects.all():
	#   i.title = title(Input.inURL)
	return render(request, 'urlExp/post_list.html', {'url': url})
	
	#if urls.exists():
	#	for url in urls.iterator():
	#		return render(request, 'urlExp/post_list.html', {'url': url, 'title': title(url.inURL)})

#def post_detail(request, pk):
#   urls = get_object_or_404(Input, pk=Input.inURL)
#   return render(request, 'urlExp/post_list.html', {'urls': urls})

def title(websites):
	website = str(websites)
	html = requests.get(website)
	soup = BeautifulSoup(html.text)
	soup2 = soup.title.string
	return soup2

def post_new(request):
	form = InputForm()
	return render(request, 'urlExp/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Input, pk=pk)
    return render(request, 'urlExp/post_edit.html', {'post': post})
