from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def starting_page(request):
    latest_posts =Post.objects.all().order_by("-date")[:3]     #这里不能用负数做slice。只是变成一个SQL query语句，所以效率不低，只抽3个
    # sorted_posts = sorted(all_posts, key = get_date)
    # latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts                #传给这个html的值。记得看里面的for post in posts的posts！
    })

def posts(request):
    all_posts=Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts               #传给这个all-posts.html。记得看里面的for post in posts的posts！
    })

def post_detail(request, slug):   #因为url那里设置了一个slug，所以这里必须传入
    # identified_post = next(post for post in all_posts if post['slug']==slug)  #直接找all_posts里面post slug吻合的一项
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post":identified_post,
        "post_tags":identified_post.tags.all()     #如果只是传tags进去，传入的是一个mapping
    })
