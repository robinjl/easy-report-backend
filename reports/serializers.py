from reports.models import DailyReport, WeeklyReport
from rest_framework import serializers


class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = ('id', 'user', 'real_name','weight', 'time', 'plan_of_today', 'working_of_today',
                  'plan_of_tomorrow', 'output', 'unresolved')


class WeeklyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyReport
        fields = ('id', 'user', 'time', 'plan_of_this_week', 'working_of_this_week',
                  'summary_of_this_week', 'unresolved', 'self_evaluation', 'improving_methods',
                  'plan_of_next_week', 'remark')
