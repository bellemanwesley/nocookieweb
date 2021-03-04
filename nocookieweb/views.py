# coding=utf-8
import os
import sys
from django.shortcuts import render

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR,'authentication/'))
import authentication

def home(request):
    # ----- Don't change between these markers, add this to the top of each function ----- 
    if not authentication.check_login(request):
        return authentication.handle_not_logged_in(request)
    else:
        # ----- Don't change between these markers, add this to the top of each function ----- 
        # Below is what you plan to return if the user is logged in
        # Do not remove the "authentication_code":authentication.code() key:value pair
        return render(request, "home.html", {"authentication_code":authentication.code()})
        

