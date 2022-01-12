from rest_framework import status
from rest_framework.response import Response


def response_fetched(data=None, count=None, errors=None):
    return Response(data={
        'status': 'Fetched',
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_200_OK)


def response_created(data=None, count=None, errors=None):
    return Response(data={
        'status': 'Created',
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_201_CREATED)


def response_updated(data=None, count=None, errors=None):
    return Response(data={
        'status': 'Updated',
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_200_OK)


def response_deleted(data=None, count=None, errors=None):
    return Response(data={
        'status': 'Deleted',
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_200_OK)


def response_unprocessable_entity(data=None, count=None, errors=None):
    return Response(data={
        'status': 'Unprocessable Entity',
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


def response_bad_request(data=None, count=None, errors=None):
    return Response(data={
        'status': 'Bad Request',
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_400_BAD_REQUEST)


def response_internal_server_error(data=None, count=None, errors=None):
    return Response(data={
        'status': 'Internal Server Error',
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
