from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',) # need to add the comment so it is seen as a tuple