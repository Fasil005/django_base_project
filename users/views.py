from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import UserTable


class UserManagement(APIView):
    def get(self, request):
        try:
            users = UserSerializer(UserTable.objects.all(), many=True)
            return Response(data=users.data, status=200)
        except Exception as e:
            print(e)
            return Response(data={'message': 'Something went wrong'}, status=500)

    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.create(data)
                return Response(data={'message': 'User created successfully'}, status=200)
            errors = ""
            for i in serializer.errors:
                errors += serializer.errors.get(i)[0].replace('This', i)
                break
            if errors:
                return Response(data={'message': errors}, status=400)
        except Exception as e:
            print(e)
            return Response(data={'message': 'Something went wrong'}, status=500)
