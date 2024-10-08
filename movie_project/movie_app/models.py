from django.db import models

class Movie(models.Model):
    name=models.CharField("",max_length=255)
    description=models.TextField("")
    director=models.CharField("",max_length=255)
    year=models.IntegerField("")
    cover=models.ImageField(upload_to='movies/covers/')

    def __str__(self):
       return f"{self.pk}-{self.name}-{self.director}"