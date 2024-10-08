from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'director', 'description', 'year', 'cover']
        labels = {
            'name': 'Название фильма',
            'director': 'Режиссер',
            'description': 'Описание',
            'year': 'Год выпуска',
            'cover': 'Обложка фильма',
        }
