from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class UserManagement(APIView):
    def get(self, request):
        return Response(data={'message': 'Hello World'}, status=200)

    def post(self, request):
        try:
            return Response(data={'message': 'Success'}, status=201)
        except Exception as e:
            print(e)
            return Response(data={'message': 'Something went wrong'}, status=500)
