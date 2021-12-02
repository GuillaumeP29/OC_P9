from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='follow_index'),
    path('index/', views.index, name='follow_index'),
    path('user_follow/', views.user_follow, name='user_follow'),
    path('delete_follow/', views.delete_follow, name='delete_follow'),
]
