from django import forms
from twits.models import Tweet, User_view

class TweetModelForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

class User_viewModelForm(forms.ModelForm):
    class Meta:
        model = User_view
        fields = '__all__'

