from django.forms import widgets
from rest_framework import serializers
from urlExp.models import Input

class UrlsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Input
		fields = ('author', 'inURL', 'status', 'destination', 'title', 'exp', 'wayurl', 'waytime')


def create(self, validated_data):
	"""
	Create and return a new 'web' instance, given the validated validated_data
	"""
	return retUrl.objects.create(**validated_data)

def update(self, instance, validated_data):
	"""
	Update and return an existing url instance, given the validated validated_data
	"""
	instance.pk = validated_data.get('pk', instance.created)
	instance.author = validated_data.get('author', instance.created)
	instance.inURL = validated_data.get('inURL', instance.created)
	instance.destination = validated_data.get('destination', instance.created)
	instance.title = validated_data.get('title', instance.created)
	instance.exp = validated_data.get('exp', instance.created)
	instance.wayurl = validated_data.get('wayurl', instance.created)
	instance.waytime = validated_data.get('waytime', instance.created)
	return instance

