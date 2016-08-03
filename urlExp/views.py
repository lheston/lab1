from django.shortcuts import render
from .models import Input

def post_list(request):
	urls = Input.objects.all()
	return render(request, 'urlExp/post_list.html', {'urls': urls})