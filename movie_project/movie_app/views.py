from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie
from .forms import MovieForm

def movies_page(request):
    movies = Movie.objects.all()
    context={
        'movies':movies
    }
    return render(request, 'movies_page.html', context)

def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies_page')
    else:
        form = MovieForm()
        context={
        'form':form
    }
  
    return render(request, 'create_movie.html',context)

def read_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context={
        'movie':movie
    }
    return render(request, 'read_movie.html', context)

def update_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies_page')
    else:
        form = MovieForm(instance=movie)
        context={
        'form':form
    }
  
    return render(request, 'create_movie.html',context)

def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies_page')
    context={
        'movie':movie
    }
    return render(request, 'delete_movie.html', context)