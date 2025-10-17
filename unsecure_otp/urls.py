from django.urls import path
from . import views

app_name = 'unsecure_otp'

urlpatterns = [
    path('', views.unsecure_otp_home, name='unsecure_otp_home'),  
    path('request/', views.request_otp, name='request'),
    path('verify/', views.verify_otp, name='verify'),

]


