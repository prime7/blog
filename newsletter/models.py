from django.db import models
from django.urls import reverse
from .utils import get_key
# Create your models here.



class Subscribers(models.Model):
    user_email = models.EmailField()
    timestamp = models.DateField(auto_now_add = True)
    confirmKey = models.CharField(max_length = 20 , blank = True, null = True)
    confirmed = models.BooleanField(default= False)

    def __str__(self):
        return self.user_email

    def save(self,*args,**kwargs):
        if self.confirmKey is None or self.confirmKey == "":
            self.confirmKey = get_key(self)
        
        super(Subscribers,self).save(*args,**kwargs)
