from django import forms
from . models import Post

class PostForm(forms.ModelForm):
    # Create form for most model

    class Meta:
        model = Post
        fields = ('title', 'text',)
