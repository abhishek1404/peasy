# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponse
from .models import UserProfile,Prescription, RequestQ
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Create your views here.

def ask_approval(request):
    username = request.user.username
    user_info = list(UserProfile.objects.filter(user=username).values())
    requested_by_id = user_info[0].get('id')
    requested_by = requested_by_id
    requested_to = request.POST.get("requested_to")
    a = RequestQ(requested_by= requested_by,requested_to=requested_to,status='p')
    a.save()
    return HttpResponse("Requested the related patient for prescription")





def get_doc_page(id):

    print "not here",id
    user_list = list(UserProfile.objects.filter(user_type="p").values())
    print user_list
    for item in user_list:
        app_requests = list(RequestQ.objects.filter(requested_by=id,requested_to=item["id"]).values())
        if app_requests:
            if app_requests[0]["status"] == "a":
                presc = Prescription.objects.filter(user__pk=app_requests[0]["requested_to"]).values()[0]
                item["prescription"] = presc
            else:
                item["prescription"] = "Pending"

        else:
            item["prescription"] = None
    return user_list



def get_pat_page(id):
    data = list(RequestQ.objects.filter(requested_to=id,status = "p").values())
    return data

def approve(request):
    request_id=request.POST.get("request_id")[0]
    RequestQ.objects.filter(pk=request_id).update(status='a')
    return HttpResponse("Requested is aproved")


def user_page(request):
    username = request.user.username
    user_info = list(UserProfile.objects.filter(user=username).values())
    user_type = user_info[0].get('user_type')
    id = user_info[0].get('id')
    if str(user_type) =='d' or str(user_type)=='m':
        data = get_doc_page(id)
    else:
        data = get_pat_page(id)
    return render(request,"detail.html",{"data":data,"user_type":user_type})
