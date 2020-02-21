from rest_framework.response import Response


def success_response(msg, data=None):
    return Response({'status': 1, 'msg': msg, 'data': data})


def error_response(msg):
    return Response({'status': 0, 'msg': msg})
