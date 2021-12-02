from django.urls import path

from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('feed/', views.feed, name='feed'),
    path('my_posts/', views.my_posts, name='my_posts'),
    path('new_review/', views.new_review, name='new_review'),
    path('ticket_review/', views.ticket_review, name='ticket_review'),
    path('edit_review/', views.edit_review, name='edit_review'),
    path('delete_review/', views.delete_review, name='delete_review'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('edit_ticket/', views.edit_ticket, name='edit_ticket'),
    path('delete_ticket/', views.delete_ticket, name='delete_ticket'),
]
