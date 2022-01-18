from rest_framework import status
from rest_framework.response import Response


def response_success(data=None, count=None, errors=None, msg='Success'):
    return Response(data={
        'status': msg,
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_200_OK)


def response_fetched(data=None, count=None, errors=None, msg='Fetched'):
    return Response(data={
        'status': msg,
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_200_OK)


def response_created(data=None, count=None, errors=None, msg='Created'):
    return Response(data={
        'status': msg,
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_201_CREATED)


def response_updated(data=None, count=None, errors=None, msg='Updated'):
    return Response(data={
        'status': msg,
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_200_OK)


def response_deleted(data=None, count=None, errors=None, msg='Deleted'):
    return Response(data={
        'status': msg,
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_200_OK)


def response_not_found(data=None, count=None, errors=None, msg='Not Found'):
    return Response(data={
        'status': msg,
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_204_NO_CONTENT)


def response_unprocessable_entity(data=None, count=None, errors=None, msg='Unprocessable Entity'):
    return Response(data={
        'status': msg,
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


def response_bad_request(data=None, count=None, errors=None, msg='Bad Request'):
    return Response(data={
        'status': msg,
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_400_BAD_REQUEST)


def response_internal_server_error(data=None, count=None, errors=None, msg='Internal Server Error'):
    return Response(data={
        'status': msg,
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def response_forbidden(data=None, count=None, errors=None, msg='Forbidden'):
    return Response(data={
        'status': msg,
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_403_FORBIDDEN)


def response_unauthorized(data=None, count=None, errors=None, msg='Unauthorized'):
    return Response(data={
        'status': msg,
        'errors': errors,
        'count': count,
        'data': data
    }, status=status.HTTP_401_UNAUTHORIZED)
