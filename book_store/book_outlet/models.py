from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)  #可以为null默认值
    is_bestselling = models.BooleanField(default=True)
    slug = models.SlugField(default="", null=False)  # Harry Potter 1 => harry-potter-1 从标题自动转换

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.id])  #可以传给index.html让它找url
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) # Harry Potter 1 => harry-potter-1 从标题自动转换
        super().save(*args, **kwargs)

    def __str__(self):    #此处必须写self
        return f"{self.title} ({self.rating})"