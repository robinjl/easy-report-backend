from rest_framework import mixins, viewsets
from common.utils import success_response, error_response
from rest_framework.decorators import list_route

from users.models import User
from users.serialziers import UserSerializer


class UserViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @list_route(methods=['post'], url_path='login')
    def login(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
            user = User.objects.filter(username=username, password=password).last()

            serializer = UserSerializer(user)
            if user:
                return success_response('登录成功', serializer.data)
            else:
                return error_response('账号或密码错误')
        except Exception as e:
            return error_response(str(e))
