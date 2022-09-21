from . models import Notification

from account.authenticate import JWTAuthentication

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

# Create your views here.
class NotificationView(APIView):
    """
    Get request list for host.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        
        notifications = list(Notification.objects.filter(receiver=request.user).values('id', 'sender__username', 'receiver__username',
        'game_id', 'game__sport_type', 'game__location1', 'game__location2', 'game__date', 'game__arranger__username', 'notification_types'))

        return JsonResponse(notifications, safe=False)

