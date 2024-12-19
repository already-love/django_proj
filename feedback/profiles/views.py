from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.

from .forms import ProfileForm
from .models import UserProfile

# def store_file(file):
#     with open(f"temp/{file}", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html",{
            "form":form,              
        })

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            # store_file(request.FILES['image'])
            profile = UserProfile(image= request.FILES["user_image"])   #forms.py里面的
            profile.save()
            return HttpResponseRedirect("/profiles")
        return render(request, "profiles/create_profile.html",{
            "form":submitted_form,              
        })