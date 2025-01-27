from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notify-button-click/', views.notify_button_click, name='notify_button_click'),
]