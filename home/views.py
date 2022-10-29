from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact, Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(response):
	if response.method == "POST":
		r = response.POST;
		#print(r.get("username"),r.get("phn"),r.get("email"), r.get("date"));
		ob = Contact(name = r.get("username") ,phn = r.get("phn") , email = r.get("email") , data = r.get("date"));
		ob.save();
		return HttpResponse("THANK YOU Registering !!");
	return render(response, "home/home.html");	



def contact(response):
	if response.method == "POST":
		r = response.POST;
		#print(r.get("username"),r.get("email"), r.get("pass"));
		user = User.objects.create_user(username = r.get("username"), email = r.get("email"), password = r.get("pass"));
		user.save();
		profile = Profile(user = user, bio = r.get("bio"));
		profile.save();
	return render(response, "home/contact.html");



def services(response):
	data = {
		"data" : Contact.objects.all(),
		"data2" : Profile.objects.all()
	}
	return render(response, "home/services.html",data);

def loginUser(response):
	if response.method == "POST":
		r = response.POST;
		#print(r.get("username"), r.get("password"));
		user = authenticate(response, username = r.get("username"), password = r.get("password"));
		if user is not None:
			login(response, user);
		return redirect("index")
	else:
		return HttpResponse("404 ERROR not found")

def logoutUser(response):
	logout(response);
	return redirect("index");