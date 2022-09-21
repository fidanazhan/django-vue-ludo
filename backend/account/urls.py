from django.urls import path
from . views import (AccountRegisterView, AuthenticatedUserView, LoginView, 
                     LogoutView, UserGameHostedCountView, UserGameRequestedView,
                     UserGameHostedActiveListView, UserGameHostedGameDetailView, UserGameHostedGameDetail2View)

urlpatterns = [
    path('register', AccountRegisterView.as_view(), name='user-register'),
    path('login', LoginView.as_view(), name='user-login'),
    path('logout', LogoutView.as_view(), name='user-logout'),
    path('auth-user', AuthenticatedUserView.as_view(), name='home'),

    # Game Host Count
    path('game-host', UserGameHostedCountView.as_view(), name='game-host'),
    path('join-request', UserGameRequestedView.as_view(), name='game-join-request'),

    # List 
    path('game-list', UserGameHostedActiveListView.as_view(), name='game-list'),

    # Detail
    path('game-host/<int:game_pk>', UserGameHostedGameDetailView.as_view(), name='game-host-detail'),
    path('game-host/<int:game_pk>/detail', UserGameHostedGameDetail2View.as_view(), name='game-host-detail'),


]
