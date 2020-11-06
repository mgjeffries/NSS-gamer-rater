from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from raterapp.models import gameCategory
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from rest_framework import status
from raterapp.models import Game, Player, GameCategory

class Games(ViewSet):
    """Gamer Rater Games"""

    
    def list(self, request):
        """Handle GET requests to games resource

        Returns:
            Response -- JSON serialized list of games
        """
        # Get all game records from the database
        games = Game.objects.all()

        serializer = GameSerializer(
            games, many=True, context={'request': request})
        return Response(serializer.data)

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games

    Arguments:
        serializer type
    """
    class Meta:
        model = Game
        fields = ('id', 'player', 'title', 'description',
         'designer', 'year_released', 'number_of_players', 
         'time_to_play', 'age_recommendation')
        depth = 1