from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import ReviewForm
from .models import Review

class ReviewView(View):
    def get(self,request):
        form = ReviewForm()       #user_name在forms.py定义好了，就不用在template里面hard-code了
        
        return render(request, "reviews/review.html", {
            "form": form
        })
    def post(self, request):
        form = ReviewForm(request.POST)   #如果此处是model form，就不需要下面几行直接form.save()
        if form.is_valid():
            form.save()         #返回dict {'user_name': 'max'}
            return HttpResponseRedirect("/thank-you")
        return render(request, "reviews/review.html", {
            "form": form
        })
    
# Create your views here.
def review(request):
    if request.method == "POST":
        # 如果需要update一个已有的model
        # existing_data = Review.objects.get(pk=1)
        # form = ReviewForm(request.POST, instance = existing_data)  

        form = ReviewForm(request.POST)   #如果此处是model form，就不需要下面几行直接form.save()
        if form.is_valid():
            # review = Review(user_name =form.cleaned_data['user_name'], 
            #                 review_text=form.cleaned_data['review_text'], 
            #                 rating=form.cleaned_data['rating'])
            # review.save()
            form.save()
            # print(form.cleaned_data)                     #返回dict {'user_name': 'max'}
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