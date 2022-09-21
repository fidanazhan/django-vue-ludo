from rest_framework import serializers, exceptions

from . models import JoinRequest 
from game . models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'id',
            'sport_type',
            'location1',
            'location2',
            'date'
        ]

class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinRequest
        fields = [
            'request_id',
            'sender',
            'receiver',
            'game'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["game"] = GameSerializer(instance.game).data
        return representation


