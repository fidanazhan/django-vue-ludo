from django.urls import path

from . views import (Joiner_SendJoinRequestView, Joiner_JoinRequestListView, Joiner_CancelRequestView, Joiner_UnjoinView,
                     Host_JoinRequestResponseView, Host_RemovePlayerView, Host_JoinRequestListView)


urlpatterns = [
    path('joiner/join-list', Joiner_JoinRequestListView.as_view()),
    path('<int:game_pk>/create_request', Joiner_SendJoinRequestView.as_view()),
    path('<str:join_pk>/cancel_request', Joiner_CancelRequestView.as_view()),
    path('<int:game_pk>/unjoin_message', Joiner_UnjoinView.as_view()),


    path('<str:join_pk>/response', Host_JoinRequestResponseView.as_view()),
    path('<int:game_pk>/<str:user>/remove_player', Host_RemovePlayerView.as_view()),
    path('host/<int:game_pk>/join-list/', Host_JoinRequestListView.as_view()),
]
