from django.urls import path
from . import views

urlpatterns = [
    path('wallet/', views.wallet, name='wallet'),
    path('history/', views.history, name='history'),
    path('balance/', views.balance, name='balance'),
    path('Payment/', views.Payment, name='Payment'),
    path('sendmoney/', views.sendmoney, name='sendmoney'),
    path('Addmoney/', views.Addmoney, name='Addmoney'),
]