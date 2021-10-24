from django.urls import path

from . import views

urlpatterns = [
    path('<int:movie_id>/delete/', views.delete, name="delete"),
    path('<int:movie_id>/retrieve/', views.retrieve, name="retrieve"),
    path('<int:movie_id>/update/', views.update, name="edit"),
    path('create/', views.create, name="create"),
    path('', views.index, name="index"),
]