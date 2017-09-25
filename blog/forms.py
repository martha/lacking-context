from django import forms

from .models import Post

class PostForm(forms.ModelForm):

  class Meta:
    model = Post
    fields = ('album_artist', 'album_name', 'spotify_id', 'text')
