from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm

# Create your views here.
def review(request):
    if request.method == "POST":
        entered_username = request.POST['username']    #POST的key是设置的name，value是实际form里input得到的值
        if entered_username == "":
            return render(request, "reviews/review.html", {
                "has_error": True
            })
        print(entered_username)
        return HttpResponseRedirect("/thank-you")
        
    return render(request, "reviews/review.html", {
        "has_error": False
    })

def thank_you(request):
    return render(request, "reviews/thank_you.html")