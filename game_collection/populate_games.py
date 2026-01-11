# populate_games.py

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "game_collection.settings")
django.setup()

from games.models import Genre, Game

# Створимо жанри
action = Genre.objects.create(name="Action")
rpg = Genre.objects.create(name="RPG")
strategy = Genre.objects.create(name="Strategy")
adventure = Genre.objects.create(name="Adventure")

# Створимо ігри
game1 = Game.objects.create(title="The Witcher 3", release_year=2015, rating=9.8)
game1.genres.set([rpg, adventure])

game2 = Game.objects.create(title="Civilization VI", release_year=2016, rating=9.2)
game2.genres.set([strategy])

game3 = Game.objects.create(title="God of War", release_year=2018, rating=9.6)
game3.genres.set([action, adventure])

print("Genres and Games created successfully!")
