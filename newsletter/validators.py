from django.core.exceptions import ValidationError
from .models import Subscribers

def validateSubscribeEmail(value):
    qs = Subscribers.objects.filter(user_email__iexact = value)
    if qs.exists():
        raise ValidationError("Already subscribed :-) ")
    return value

def validateUnSubscribeEmail(value):
    qs = Subscribers.objects.filter(user_email__iexact = value)
    if not qs.exists():
        raise ValidationError("Email not subscribed ")
    return value