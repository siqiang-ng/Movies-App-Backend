from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Movie
from .forms import MovieForm

def index(request):
    latest_movie_list = Movie.objects.all()
    return render(request, 'movie/index.html', {'movies': latest_movie_list})

def create(request):
    form = MovieForm()

    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Movie has been added successfully!")
        else: 
            messages.error(request, "Movie has not been added")
        return redirect('index')

    return render(request, 'movie/form.html', {'form': form})

def update(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)

    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, "Movie has been edited successfully!")
            return redirect('retrieve', movie_id=movie.id)
    else :
        form = MovieForm(instance=movie)

    return render(request, 'movie/edit.html', {'form': form})

def retrieve(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movie/movie.html', {'movie': movie})

def delete(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie.delete()
    messages.success(request, "Movie has been deleted successfully!")
    return redirect('index')