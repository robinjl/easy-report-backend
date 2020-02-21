from rest_framework import mixins, viewsets
from reports.models import DailyReport, WeeklyReport
from reports.serializers import DailyReportSerializer, WeeklyReportSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import list_route
from users.models import User
from common.utils import success_response


class DailyReportViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = DailyReport.objects.all().order_by('-time')
    serializer_class = DailyReportSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'time']

    @list_route(methods=['get'], url_path='statistics')
    def statistics(self, request):
        """
        期望返回数据格式： { total: 20, data: [{time: 'xxx', count: 5}, {}]
        目前返回数据格式： { total: 20, data: [{time: 'xxx', user: 1}, {}]
        """
        users_total = User.objects.all().count()
        reports = DailyReport.objects.all().order_by('-time')
        statistics = []
        for report in reports:
            statistics.append({'time': report.time, 'user': report.user_id})
        data = {'total': users_total, 'list': statistics}
        return success_response('', data)


class WeeklyReportViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = WeeklyReport.objects.all()
    serializer_class = WeeklyReportSerializer
