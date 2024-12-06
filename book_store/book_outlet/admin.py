from django.contrib import admin

from .models import Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)      #tuple必须要多于一个，所以必须有逗号
    prepopulated_fields = {"slug":("title",)}   #这里的引号之中都是model里面的field的名字
    list_filter = ("author","rating",)
    list_display= ("title","author",)

admin.site.register(Book, BookAdmin)   #传入一个model