from django.urls import path

from . import views

urlpatterns = [
    path('', views.LoginPage.as_view(), name='login'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('sign_up/', views.sign_up_page, name='sign_up'),
    path('logout/', views.logout_user, name='logout'),
]
