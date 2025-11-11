from django.urls import path
from .views import HomePageView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
 ]