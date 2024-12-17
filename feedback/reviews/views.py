from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm

# Create your views here.
def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)                     #返回dict {'user_name': 'max'}
            return HttpResponseRedirect("/thank-you")
        # entered_username = request.POST['username']    #POST的key是设置的name，value是实际form里input得到的值
        # if entered_username == "":
        #     return render(request, "reviews/review.html", {
        #         "has_error": True
        #     })
    else:
        form = ReviewForm()       #user_name在forms.py定义好了，就不用在template里面hard-code了
        
    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")