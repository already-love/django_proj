from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView   #一种特定TemplateView
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
    
# # Create your views here.
# def review(request):
#     if request.method == "POST":
#         # 如果需要update一个已有的model
#         # existing_data = Review.objects.get(pk=1)
#         # form = ReviewForm(request.POST, instance = existing_data)  

#         form = ReviewForm(request.POST)   #如果此处是model form，就不需要下面几行直接form.save()
#         if form.is_valid():
#             # review = Review(user_name =form.cleaned_data['user_name'], 
#             #                 review_text=form.cleaned_data['review_text'], 
#             #                 rating=form.cleaned_data['rating'])
#             # review.save()
#             form.save()
#             # print(form.cleaned_data)                     #返回dict {'user_name': 'max'}
#             return HttpResponseRedirect("/thank-you")
#         # entered_username = request.POST['username']    #POST的key是设置的name，value是实际form里input得到的值
#         # if entered_username == "":
#         #     return render(request, "reviews/review.html", {
#         #         "has_error": True
#         #     })
#     else:
#         form = ReviewForm()       #user_name在forms.py定义好了，就不用在template里面hard-code了
        
#     return render(request, "reviews/review.html", {
#         "form": form
#     })

# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "reviews/thank_you.html")

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    # 不需要get和render

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This works!"
        return context
    # 把dictionary中的值传入那个template html

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    #如果用ListView，传入template就是一个object_list，或者复写
    context_object_name = "reviews"

    def get_queryset(self):
        base_query= super().get_queryset()
        data = base_query.filter(rating__gt=3)
        return data

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()   #models来的
    #     context['reviews'] = reviews  #增加一个键值对
    #     return context 

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review   #传入template的变量自动变小写
    


    # def get_context_data(self, **kwargs):     # int:id 是kwargs从urls.py传进来了
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs['id']
    #     selected_review = Review.objects.get(pk=review_id)   #models来的
    #     context['review'] = selected_review   #增加一个键值对
    #     return context 