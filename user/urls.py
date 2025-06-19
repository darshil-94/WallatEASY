from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('signin/',views.sigin,name="signin"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/', views.logout, name='logout'),
    path('', views.main, name='main'),
]