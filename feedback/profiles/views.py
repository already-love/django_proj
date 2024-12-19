from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
# Create your views here.

from .forms import ProfileForm
from .models import UserProfile

# def store_file(file):
#     with open(f"temp/{file}", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"
