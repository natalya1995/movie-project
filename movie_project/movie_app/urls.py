from django.urls import path
from . import views

urlpatterns=[
    path('',views.movies_page, name='movies_page'),
    path('create/',views.create_movie, name='create_movie'),
    path('read/<int:pk>/',views.read_movie, name='read_movie'),
    path('delete/<int:pk>/',views.delete_movie, name='delete_movie'),
    path('update/<int:pk>/',views.update_movie, name='update_movie'),
]