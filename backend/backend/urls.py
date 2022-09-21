from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('account.urls')),
    path('api/games/', include('game.urls')),
    path('api/joins/', include('join.urls')),
    path('api/notifications/', include('notification.urls')),
]
