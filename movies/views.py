from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Movie, Genre

# Create your views here.
def index(request):
    movies = Movie.objects.select_related('genre').all()

    # output = '\n'.join([str(movie) for movie in movies])
    # return HttpResponse(f"Hello, world. You're at the movies index. Movies:\n{output}", content_type="text/plain")
    # return render(request, '../templates/index.html', {'movies': movies})
    return render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
    try:
        movie = Movie.objects.select_related('genre').get(pk=movie_id)
        return render(request, 'movies/detail.html', {'movie': movie})
    except Movie.DoesNotExist:
        context = {
            'request_path': request.get_full_path(),
            'movie_id': movie_id
        }
        return render(request, 'movies/404.html', context, status=404)

def custom_404_view(request, exception):
    """Custom 404 error page"""
    context = {
        'request_path': request.get_full_path(),
        'exception': exception
    }
    return render(request, 'movies/404.html', context, status=404)
   
