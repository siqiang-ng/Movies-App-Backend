from django.urls import path

from . import views

urlpatterns = [
    path('<int:movie_id>/', views.handleMovieRequest, name="handleMovieRequest"),
    path('', views.index, name="index"),
]