
from . models import JoinRequest
from game . models import Game, Gamelist
from account . models import CustomizeUser
from notification . models import Notification

# from notification.models import Notification

from account.authenticate import JWTAuthentication
from rest_framework import status, serializers

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import JoinSerializer
from django.http import JsonResponse

# Create your views here.
class Joiner_SendJoinRequestView(APIView):
    """
    Send join request to join the game.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, game_pk,*args, **kwargs):
        
        sender = request.user
        game = Game.objects.get(pk=game_pk)
        receiver = game.arranger

        if game.arranger == sender:
            raise serializers.ValidationError('You cannot send request for game that you host')

        if sender not in game.request_user.all():
            game.request_user.add(sender)
            join_request = JoinRequest.objects.create(sender=sender, game=game, receiver=receiver)

            notification = Notification.objects.create(notification_types = 1, 
                                                       game = game,
                                                       sender=request.user, 
                                                       receiver=receiver) 
            return Response('You have request to join the game.')
        else:
            return Response("You already sent request to join the game.")

class Host_JoinRequestResponseView(APIView):
    """
    Send response for join request.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, join_pk, *args, **kwargs):

        join_request = JoinRequest.objects.get(pk=join_pk)
        sender = join_request.sender

        game = Game.objects.get(pk=join_request.game.pk)

        data = request.data

        join_response = data['Response']

        if join_response == 'Accept':

            join_request.response_accept()

            game.add_player(sender)
            game.player_needed_count_decrease()
            game.remove_request_user(sender)

            notification = Notification.objects.create(notification_types = 2, 
                                                       game = game,
                                                       sender=request.user, 
                                                       receiver=sender) 

            return Response('You have accepted the request')

        elif join_response == "Reject":

            join_request.response_reject()

            game.remove_request_user(sender)

            return Response('You have declined the request')

class Joiner_JoinRequestListView(APIView):
    """
    See the list of sent request that still active.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        join_requests = JoinRequest.objects.filter(sender=request.user, is_active=True).order_by('-created_on')
        serializer = JoinSerializer(join_requests, many=True)
        join_request_count = join_requests.count()

        return Response(serializer.data)

class Joiner_CancelRequestView(APIView):
    """
    Joiner cancel join request.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, join_pk, *args, **kwargs):
        join_request = JoinRequest.objects.get(pk=join_pk)
        game = join_request.game

        if request.user in game.request_user.all():
            game.request_user.remove(request.user)
            join_request.delete()

            notification = Notification.objects.filter(notification_types = 1, 
                                                       game = game,
                                                       sender=request.user, 
                                                       receiver=game.arranger).first()
            notification.delete() 

            return Response("You have cancel your request to join the game.")
        else:
            return Response("There are no join request to join this game from you.")

class Joiner_UnjoinView(APIView):
    """
    Joiner send unjoin message.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, game_pk, *args, **kwargs):

        sender = request.user
        game = Game.objects.get(pk=game_pk)

        if sender in game.player_joined.all():
            game.remove_player(sender)
            game.player_needed_count_increase()

            notification = Notification.objects.create(notification_types = 4, 
                                                       game = game,
                                                       sender=request.user, 
                                                       receiver=game.arranger)
       
            return Response("You have send message that you will not join the game.")

        else:
            return Response("You are not approved to join the game. So, you cannot unjoin the game.")      

class Host_RemovePlayerView(APIView):
    """
    Host remove player
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, user, game_pk, *args, **kwargs):
        
        game = Game.objects.get(pk=game_pk)
        account = CustomizeUser.objects.get(username=user)

        if account in game.player_joined.all():
            game.player_needed_count_increase()
            game.remove_player(account)

            notification = Notification.objects.create(notification_types = 3, 
                                                        game = game,
                                                        sender=request.user, 
                                                        receiver=account)

            return Response("You have removed player from the game.")
        else:
            return Response("The player is not in the list for joined player.")

class Host_JoinRequestListView(APIView):
    """
    Get request list for host.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, game_pk, *args, **kwargs):

        print(request)
        print(request.user)

        join_requests = list(JoinRequest.objects.filter(game__pk=game_pk, is_active=True).values('request_id','sender__username', 
        'receiver__username', 'game_id', 'game__sport_type', 'game__location1', 'game__location2', 'game__date'))

        return JsonResponse(join_requests, safe=False)

        
