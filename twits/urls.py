from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_twits, name = 'all_twits'), # http://127.0.0.1:8000/twits
    path('user', views.user, name = 'user'), # http://127.0.0.1:8000/twits/user
    path('create_twit', views.create_twit, name = 'create_twit'), #http://127.0.0.1:8000/twits/create_twit
]