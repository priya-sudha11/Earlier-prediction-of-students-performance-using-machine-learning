"""Dp URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from. import views
from django.contrib.auth.views import LoginView
from .views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path('login/', login_view, name='login'),
    path('main/',views.main, name='main'),
    path("main/registration/", views.registration, name='registration'),
    path("main/registration/logredir", views.logredir, name='logredir'),
    path("main/registration/predict2", views.predict2, name='predict2'),
    path("main/registration/result_2", views.result_2, name='result_2'),
    path("main/registration/send_sms", views.send_sms, name='send_sms'),
    path("registration/predict", views.predict, name='predict'),
    path('login/', LoginView.as_view(), name='login'),
    path("login/logredir/", views.logredir, name='logredir'),
    path("login/logredir/predict2", views.predict2, name='predict2'),
    path("login/logredir/predict", views.predict, name='predict'),
    path("login/logredir/login", LoginView.as_view(), name='login'),
    path("login/logredir/result_2", views.result_2, name='result_2'),
    path("login/logredir/send_sms", views.send_sms, name='send_sms'),
    path("logredir/predict/",views.predict, name='predict'),
    # path('base/', views.registration, name='base'),
    # path('base/login', login_view, name='login'),
    # path('send_sms/', views.send_sms, name='send_sms'),
    # path("predict/",views.predict, name='predict'),
    # path("predict/send_sms/", views.send_sms, name='send_sms'),
    # path("predict/predict2/", views.predict2, name='predict2'),
    # path("predict/predict2/result_2", views.result_2, name='result_2'),
    # path("predict2/",views.predict2),
    # path("predict2/result_2",views.result_2),
    # path("predict2/send_sms/", views.send_sms, name='send_sms'),
]
#login/logredir/predict login/logredir/login

