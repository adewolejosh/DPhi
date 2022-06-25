
from rest_framework.views import APIView, Response
from rest_framework import status

from .serializers import CreateUserSerializer


class AuthenticationNewUser(APIView):

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
