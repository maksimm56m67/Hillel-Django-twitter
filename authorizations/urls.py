from django.urls import path
from authorizations import views

urlpatterns = [
    path('login', views.login, name='login'), # http://127.0.0.1:8000/authorizations/login
    path('logout', views.logout_user, name='logout'), # http://127.0.0.1:8000/authorizations/logout
    path('register', views.registration, name='register'), #http://127.0.0.1:8000/authorizations/register
]
