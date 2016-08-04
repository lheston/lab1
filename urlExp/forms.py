from django import forms

from .models import Input

class PostForm(forms.ModelForm):

    class Meta:
        model = Input
        fields = ('inURL',)