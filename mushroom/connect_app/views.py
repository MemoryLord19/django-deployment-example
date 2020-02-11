from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request,'connect_app/index.html',{})

@login_required
def find(request):
	return render(request,'connect_app/find.html',{})

@login_required
def messages(request):
	return render(request,'connect_app/messages.html',{})

@login_required
def public(request):
	return render(request,'connect_app/public.html',{})
