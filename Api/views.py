from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserSerializer

@api_view(['GET'])
def getUsers(request):
    user = User.objects.all()
    ser = UserSerializer(user, many=True)
    return Response(ser.data)