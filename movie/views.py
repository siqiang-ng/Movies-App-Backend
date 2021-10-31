from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Movie
from .serializers import MovieSerializer

@csrf_exempt
def index(request):
    if request.method == "GET" :
        latest_movie_list = Movie.objects.all()
        serializer = MovieSerializer(latest_movie_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST" :
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def handleMovieRequest(request, movie_id) :
    
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == "GET" :
        return retrieve(movie)

    elif request.method == "PUT" :
        data = JSONParser().parse(request)
        return update(movie, data)

    elif request.method == "DELETE" :
        return delete(movie)

def retrieve(movie):
    serializer = MovieSerializer(movie)
    return JsonResponse(serializer.data)

def update(movie, data):
    serializer = MovieSerializer(movie, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

def delete(movie):
    movie.delete()
    return HttpResponse(status=204)