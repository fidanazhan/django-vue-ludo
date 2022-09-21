from rest_framework import serializers

from account.models import CustomizeUser
from . models import Game
# from rest_framework.fields import CurrentUserDefault

from rest_framework import exceptions

class ArrangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomizeUser
        fields = [
            'id',
            'username'
        ]

class PlayerJoinedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomizeUser
        fields = [
            'id',
            'username'
        ]

class BookmarkUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomizeUser
        fields = [
            'username'
        ]

class RequestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomizeUser
        fields = [
            'id',
            'username'
        ]

class GameBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'id',
            'sport_type',
            'location1',
            'location2',
            'date',
            'arranger',
            
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["arranger"] = ArrangerSerializer(instance.arranger).data
        return representation

    def validate_sport_type(self, value):
        if not value or value == "":
            raise exceptions.ValidationError('Please input sport')
        return value

    def validate_location1(self, value):
        if not value or value == "":
            raise exceptions.ValidationError('Please input sport venue')
        return value

    def validate_location2(self, value):
        if not value or value == "":
            raise exceptions.ValidationError('Please input location')
        return value

    def validate_date(self, value):
        if not value or value == "":
            raise exceptions.ValidationError('Please input play date')
        return value

    def validate_arranger(self, value):
        if not value or value == "":
            raise exceptions.ValidationError('Please input host name')
        return value

class GameListSerializer(GameBaseSerializer):
    player_needed = serializers.IntegerField(min_value=0)
    court_status = serializers.CharField(max_length = 20)
    court_price = serializers.IntegerField(min_value=0)
    price_per_player = serializers.IntegerField(min_value=0)

    class Meta(GameBaseSerializer.Meta):
        fields = GameBaseSerializer.Meta.fields + [
            'occupied_player',
            'player_needed',
            'court_status',
            'court_name',
            'court_price',
            'price_per_player',
        ]

    def validate_occupied_player(self, value):
        if not value or value == "":
            raise serializers.ValidationError('Please input occupied player')
        return value

    def validate_court_status(self, value):
        if not value or value == "":
            raise serializers.ValidationError('Please input court status')
        return value

    def validate_court_name(self, value):
        if not value or value == "":
            raise serializers.ValidationError('Please input the court name')
        return value

    def validate_court_price(self, value):
        if not value or value == "":
            raise serializers.ValidationError('Please input the court price')
        return value  

    def validate_price_per_player(self, value):
        if not value or value == "":
            raise serializers.ValidationError('Please input price for player who want to join')
        return value      

class GameHostDetailSerializer(GameListSerializer):
    player_joined = PlayerJoinedSerializer(read_only=True, many=True)

    class Meta(GameListSerializer.Meta):
        fields = GameListSerializer.Meta.fields + [
            'player_joined'
        ]

class GameHostDetail2Serializer(GameHostDetailSerializer):
    request_user = RequestUserSerializer(read_only=True, many=True)

    class Meta(GameHostDetailSerializer.Meta):
        fields = GameHostDetailSerializer.Meta.fields + [
            'request_user'
        ]


    
    

