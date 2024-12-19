from django.db import models

# Create your models here.
class UserProfile(models.Model):
    image= models.FileField(upload_to="images")  #在settings.py 的MEDIA_ROOT
