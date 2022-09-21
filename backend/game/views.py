from django.http import Http404

from . serializers import GameBaseSerializer, GameListSerializer
from . models import Game

from account.authenticate import JWTAuthentication
from rest_framework import status, serializers
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import math

# Create your views here.
class BasicGameView(APIView):

    """
    Get a list of games or create a new game.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        games = Game.objects.exclude(Q(request_user = request.user) | Q(arranger=request.user) | Q(player_joined=request.user) | Q(is_active=False)).order_by('-date_created')
        
        total = len(games)

        per_page = 10
        page = int(request.query_params.get('page', 1))
        start = (page - 1) * per_page
        end = page * per_page

        # With pagination -> return 10 data per page, time_taken = 152ms, data_transfer = 1.83KB
        data = GameBaseSerializer(games[start:end], many=True).data
        return Response({
            'data' : data,
            'meta' : {
                'total' : total,
                'page' : page,
                'last_page' : math.ceil(total / per_page)
            }
        })

        # Tanpa pagination -> return 1031 data, time_taken = 3.42s, data_transfer = 137.52KB
        # serializer = GameBaseSerializer(games, many=True)
        # return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data

        data["arranger"] = request.user.pk
        # print(data)

        # Insert into the database
        serializer = GameListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Your game added to the game board')

class DetailGameView(APIView):
    """"
    Get detail, edit or delete of game.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def try_get_object(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise serializers.ValidationError("Game not found")

    def get(self, request, pk,  *args, **kwargs):
        game = self.try_get_object(pk)
        serializer = GameListSerializer(game)        
        return Response({
            'detail': serializer.data
        })

    def put(self, request, pk, format=None):
        game = self.try_get_object(pk)
        arranger = game.arranger

        if request.user == arranger:
                        
            serializer = GameListSerializer(game, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response('Your game is updated')
 
        else:
            return Response({'detail':'You are not authorized here'}, status=401)

    def delete(self, request, pk, format=None):
        game = self.try_get_object(pk)
        arranger = game.arranger

        if request.user == arranger:

            game.delete()
            return Response({'detail':'Delete successfully'}, status=status.HTTP_204_NO_CONTENT)

        else:
            return Response({'detail':'You are not authorized here'}, status=401)


