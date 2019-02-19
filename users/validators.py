from django.core.exceptions import ValidationError
from .models import Profile

def validateEmail(value):
    print(value)
    qs = Profile.objects.filter(user__email  = value)
    if qs.exists():
        raise ValidationError("Email Already there.")
    return value