from django.urls import path

from . views import BasicGameView, DetailGameView


urlpatterns = [
    path('', BasicGameView.as_view(), name='game-list'),
    path('<int:pk>', DetailGameView.as_view(), name='game-detail'),
    # path('<int:pk>', BookmarkGameView.as_view(), name='game-bookmark'),
]
