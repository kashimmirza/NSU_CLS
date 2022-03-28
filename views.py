

# Create your views here.
from django.shortcuts import render


def userProfile(request,pk):
    return render(request, 'profile1/user_profile.html')