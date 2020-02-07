from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    posted_by= models.CharField(max_length=20 , default="me")
    utimestamp=models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)

    def _unicode_(self):
        return self.title
    
    def __str__(self):
        return self.title

    def get_abs_url(self):
        return reverse("detail", kwargs={"id":self.id})
        

