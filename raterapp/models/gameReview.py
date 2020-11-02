"""GameReview module"""
from django.db import models

class GameReview(models.Model):
    """GameReview model"""
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.CharField(max_length=500)