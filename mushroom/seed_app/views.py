from django.shortcuts import render
from seed_app.forms import UserForm,UserProfileInfoForm

#Additional
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request,'seed_app/index.html',{})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def register(request):
	registered = False

	if request.method=='POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				print('FOUND IT!')
				profile.profile_pic = request.FILES['profile_pic']
			profile.save()
			registered = True

			return HttpResponseRedirect(reverse('index'))
		else:
			print(user_form.errors,profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()
	return render(request,'seed_app/register.html',{
		'user_form':user_form,
		'profile_form':profile_form,
		'registered':registered
		})

def user_login(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))
		else:
			print("unsuccessful login attempt registered")
			print("username: {}, password: {}".format(username,password))
			return HttpResponse('<center>Username and Password are not recognized</center>')
	else:
		return render(request,'seed_app/login.html',{})