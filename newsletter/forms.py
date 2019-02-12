from django import forms
from .models import Subscribers
from .validators import validateSubscribeEmail,validateUnSubscribeEmail

class EmailSubscribeForm(forms.Form):
    user_email = forms.EmailField(label = '',validators = [validateSubscribeEmail], widget = forms.TextInput(attrs={"placeholder":"Your Email","class":"form-control"}))


class EmailUnSubscribeForm(forms.Form):
    user_email = forms.EmailField(label = '',validators = [validateUnSubscribeEmail], widget = forms.TextInput(attrs={"placeholder":"Your Email","class":"form-control"}))