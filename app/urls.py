from django.urls import path
from app import views

urlpatterns = [
    path('registration',views.registration,name='registration'),
    path('patient',views.patient,name='patient'),
    path('login',views.LogIn,name='login'),
    path('view',views.DoctorView,name='view'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('logout',views.LogOut,name='logout'),
    path('about',views.about,name='about'),
    path('sms',views.sms,name='sms'),
    path('',views.home,name='home')
]
