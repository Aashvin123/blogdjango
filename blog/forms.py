from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter title here"}),
            "body": forms.Textarea(attrs={"placeholder": "Write your post here..."}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
        widgets = {
            "comment": forms.TextInput(attrs={"placeholder": "Enter comment here"}),
            
        }
