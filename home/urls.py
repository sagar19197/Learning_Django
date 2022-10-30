from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path("", views.index, name = "index"),
	path("contact/", views.contact, name = "Contact us"),
	path("services/", views.services, name = "Services"),
	path("login/", views.loginUser, name = "Login"),
	path("logout/", views.logoutUser, name = "Logout"),
	path("media/pdf/<str:file>", views.securePDF, name="SECUREPDF"),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)