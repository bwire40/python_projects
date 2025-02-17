from django.db import models

# Create your models here.
# define our table fields

class Post(models.Model):
    # title,body,slug
    title=models.CharField(max_length=75),
    body=models.TextField(),
    slug= models.SlugField(),
    date=models.DateTimeField(auto_now_add=True),
