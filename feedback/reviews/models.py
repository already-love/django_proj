from django.db import models

# Create your models here.
class Review(models.Model):
    user_name= models.CharField(max_length=100)     #此处是models. 和forms里面不一样
    review_text = models.TextField()
    rating = models.IntegerField()
