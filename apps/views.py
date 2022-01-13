from rest_framework.views import APIView
from datetime import datetime

from .models import AdminTable
from .serializer import AdminSerializer
from .response import (
    response_fetched,
    response_bad_request,
    response_internal_server_error,
    response_created,
    response_unprocessable_entity,
    response_updated,
    response_success,
    response_not_found
)


class AdminManagement(APIView):
    def get(self, request):
        try:
            admins = AdminTable.objects.all()
            serializer = AdminSerializer(admins, many=True)
            return response_fetched(data=serializer.data, count=len(serializer.data))
        except Exception as e:
            print(e)
            return response_internal_server_error(errors=str(e))

    def post(self, request):
        try:
            serializer = AdminSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response_created()
            errors = ""
            for i in serializer.errors:
                errors += serializer.errors.get(i)[0].replace('This', i)
                break
            return response_unprocessable_entity(errors=errors)
        except Exception as e:
            print(e)
            return response_internal_server_error(errors=str(e))


class SingleAdminManagement(APIView):

    def get(self, request, pk):
        try:
            admin = AdminTable.objects.get(pk=pk)
            serializer = AdminSerializer(admin)
            return response_fetched(data=serializer.data)
        except AdminTable.DoesNotExist as e:
            print(e)
            return response_not_found(errors=str(e))
        except Exception as e:
            print(e)
            return response_internal_server_error(errors=str(e))

    def put(self, request, pk):
        try:
            admin = AdminTable.objects.get(pk=pk)
            serializer = AdminSerializer(admin, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response_updated()
            errors = ""
            for i in serializer.errors:
                errors += serializer.errors.get(i)[0].replace('This', i)
                break
            return response_unprocessable_entity(errors=errors)
        except AdminTable.DoesNotExist as e:
            print(e)
            return response_not_found(errors=str(e))
        except Exception as e:
            print(e)
            return response_internal_server_error(errors=str(e))

    def patch(self, request, pk):
        try:
            admin = AdminTable.objects.get(pk=pk)
            admin.email = request.data.get('email', admin.email)
            admin.password = request.data.get('password', admin.password)
            admin.status = request.data.get('name', admin.status)
            admin.last_login = request.data.get('last_login', admin.last_login)
            admin.date_joined = request.data.get('date_joined', admin.date_joined)
            admin.is_active = request.data.get('is_active', admin.is_active)
            admin.is_superuser = request.data.get('is_superuser', admin.is_superuser)
            admin.is_staff = request.data.get('is_staff', admin.is_staff)
            admin.save()
            return response_updated()
        except AdminTable.DoesNotExist as e:
            print(e)
            return response_not_found(errors=str(e))
        except Exception as e:
            print(e)
            return response_internal_server_error(errors=str(e))


class LoginManagement(APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            admin = AdminTable.objects.get(email=email)
            if admin.password == password:
                admin.last_login = datetime.now()
                admin.save()
                return response_success(data=admin.id, msg='Login Successfully')
            return response_not_found(errors='Invalid email or password')
        except AdminTable.DoesNotExist as e:
            print(e)
            return response_not_found(errors=str(e))
        except Exception as e:
            print(e)
            return response_internal_server_error(errors=str(e))


