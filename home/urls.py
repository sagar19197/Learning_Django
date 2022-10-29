from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name = "index"),
	path("contact/", views.contact, name = "Contact us"),
	path("services/", views.services, name = "Services"),
	path("login/", views.loginUser, name = "Login"),
	path("logout/", views.logoutUser, name = "Logout"),
]