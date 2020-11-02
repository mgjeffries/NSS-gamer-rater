""" Database game module"""
from django.db import models

class Game(models.Model):
    """ database game model"""
    player = models.ForeignKey("Player", on_delete=models.PROTECT)
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=500)
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    time_to_play = models.IntegerField()
    age_recommendation = models.IntegerField()


     
    