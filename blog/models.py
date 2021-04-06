from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    image=models.ImageField(null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,default=None, null=True)
    def __str__(self):
        return self.title
class comment (models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comment')
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    body=models.TextField
    date= models.DateTimeField(auto_now_add=True) 