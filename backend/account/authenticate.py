from rest_framework import exceptions
import jwt, datetime
from rest_framework.authentication import BaseAuthentication
from . models import CustomizeUser


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            return None
        
        try:
            # payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Unauthenticated')

        user = CustomizeUser.objects.get(pk=payload['id'])
        # user = CustomizeUser.objects.filter(id=payload['id'])
        # serializer = UserSerializer(user)

        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        return (user, None)




    @staticmethod
    def generate_jwt(id):
        payload = {
            'user_id': id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=3650),
            'iat': datetime.datetime.utcnow()
        }

        # return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return jwt.encode(payload, 'secret', algorithm='HS256')