from datetime import datetime
from django.db.models import Count
import jwt, datetime

from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse

import json, math

from account.authenticate import JWTAuthentication
from account.models import CustomizeUser
from join.models import JoinRequest
from . serializers import UserSerializer

from . validations import LoginValidation, RegisterValidation
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from game.models import Game
from game.serializers import GameHostDetailSerializer, GameHostDetail2Serializer

# Create your views here.
class AccountRegisterView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data

        # Get data from the request.
        email = data['email']
        username = data['username']
        password = data['password']
        password_confirm = data['password_confirm']

        # Input the data to validate class for validation.
        data_validation = RegisterValidation(email, username, password, password_confirm)
        data_validation.is_valid()

        # 
        serializer = UserSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        data = request.data

        # Get data from request.
        username = data['username']
        password = data['password']

        # Input the data to validate class for validation.
        data_validation = LoginValidation(username, password)
        if not data_validation.is_valid():
            user = get_object_or_404(CustomizeUser, Q(username__iexact=username) | Q(email__iexact=username))
        
            payload = {
                'id':user.id,
                'exp':datetime.datetime.utcnow() + datetime.timedelta(hours=8760),
                'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256') 

            response = Response()

            response.set_cookie(key='jwt', value=token)

            response.data = {
                'message':'Login successfully',
                'token': token
            }

            return response
        else:
            return Response({
                'message':'Login failed'
            })

class AuthenticatedUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = UserSerializer(request.user).data
        return Response({
            'data' : data
        })

class UserGameHostedCountView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        game_host = Game.objects.filter(arranger=request.user).count()
        return Response({
            'game_host': game_host
        })

class UserGameHostedActiveListView(APIView):
    """
    Get the list of active games hosted by the user
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        games = list(Game.objects.filter(Q(arranger=request.user) & Q(is_active=True)).annotate(Count('request_user'))
        .order_by('-date_created').values('pk', 'sport_type','location1','location2','date','arranger',
          'arranger__username', 'request_user__count'
        ))

        total = len(games)

        per_page = 10
        page = int(request.query_params.get('page', 1))
        start = (page - 1) * per_page
        end = page * per_page

        data=list(games[start:end])


        context = {
            'game_host':data,
            'meta': {
                'total' : total,
                'page' : page,
                'last_page' : math.ceil(total / per_page)
            }
        }

        data = json.dumps(context, indent=4, sort_keys=True, default=str)
        return HttpResponse(data, content_type='application/json')

class UserGameHostedGameDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def try_get_object(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise serializers.ValidationError("Game not found")

    def get(self, request, game_pk,  *args, **kwargs):
        game = self.try_get_object(game_pk)
        serializer = GameHostDetailSerializer(game)        
        return Response({
            'detail': serializer.data
        })

class UserGameHostedGameDetail2View(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def try_get_object(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise serializers.ValidationError("Game not found")

    def get(self, request, game_pk,  *args, **kwargs):
        game = self.try_get_object(game_pk)
        serializer = GameHostDetail2Serializer(game)        
        return Response({
            'detail': serializer.data
        })

class UserGameRequestedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        joiner_request_count = JoinRequest.objects.filter(sender=request.user, is_active=True).count()
        return Response({
            'joiner_request_count': joiner_request_count
        })

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'Logout successfully'
        }

        return response