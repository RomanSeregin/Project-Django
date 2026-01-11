from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='games')
    release_year = models.PositiveIntegerField()
    rating = models.FloatField()  # наприклад від 0 до 10

    def __str__(self):
        return self.title
