from django.urls import include, path
from . import views
from .views import RegisterCreate

urlpatterns = [
    path('', views.home, name='home'),
	path('register/', RegisterCreate.as_view(), name='register'),
]

