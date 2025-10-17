from django.urls import path
from . import views

app_name = 'secure_otp'

urlpatterns = [
    path('', views.secure_otp_home, name='home'),
    path('request/', views.request_otp, name='request'),
    path('verify/', views.verify_otp, name='verify'),
]
