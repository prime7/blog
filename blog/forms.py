from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget,SummernoteInplaceWidget

class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=SummernoteWidget())

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '500px'}}),
        }

class PostCreateFormAdmin(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '500px'}}),
        }