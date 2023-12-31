from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'rating']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3})  # Customize
        }
