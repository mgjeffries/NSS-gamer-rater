"""GameImage database module"""
from django.db import models
from django.db.models.deletion import CASCADE

class GameImage(models.Model):
    """GameImage database module"""
    game = models.ForeignKey("Game", on_delete=models.CASCADE)

    ## TODO: check args for the image field
    image = models.ImageField()