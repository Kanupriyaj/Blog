from django import forms
from django.forms import ModelForm
from post.models import UserPost

# class PostForm(forms.Form):
            
#     image = forms.ImageField(label='Image ')
#     title = forms.CharField(label='Title ', max_length=100)
#     location = forms.CharField(label='Location ', max_length=100)
#     description = forms.CharField(label='Description ',widget=forms.Textarea)

class PostModelForm(ModelForm):

    class Meta:
        model = UserPost
        fields = ['image','title','location','description']

    field_order = ['image','category','location','description','title']
    