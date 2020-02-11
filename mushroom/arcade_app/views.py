from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request,'arcade_app/index.html',{})

@login_required
def chat(request):
	return render(request,'arcade_app/chat.html',{})

@login_required
def games(request):
	return render(request,'arcade_app/games.html',{})

@login_required
def connect_four(request):
	return render(request,'arcade_app/games/connect_four.html',{})

@login_required
def kac(request):
	return render(request,'arcade_app/games/knots_and_crosses.html',{})
