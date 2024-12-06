from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # author = models.CharField(null=True, max_length=100)  #可以为null默认值
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)  # CASCADE意味着一个author删除，相应书同样删除
    is_bestselling = models.BooleanField(default=True)
    slug = models.SlugField(default="", blank=True, 
                            null=False, db_index= True)  # 如果用这个query，可以设置为index。但是设置太多column为index会降低效率。
    # blank = True 意味着admin界面存储的时候，这一项不是required。反正最后会被save覆盖
    # editable = False意味着也不让admin改这个值

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])  #可以传给index.html让它找url
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) # Harry Potter 1 => harry-potter-1 从标题自动转换
        super().save(*args, **kwargs)

    def __str__(self):    #此处必须写self
        return f"{self.title} ({self.rating})"