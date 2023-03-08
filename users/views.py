from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework.status import status
from rest_framework.permissions import permissions

class AuthUserApiView(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return Response({'user':serializer.data})



class Login(APIView):
    serializer_class = LoginSerializer()
    def post(self, request):
        email = request.data.get['email', None]
        password = request.data.get['password', None]

        user = authenticate(username=email, password=password)
        
        if user:
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials try again'}, status=status.HTTP_401_UNAUTHORIZED)

