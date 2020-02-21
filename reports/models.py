from django.db import models
from users.models import User


# 日报
class DailyReport(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True, verbose_name='日报ID')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    time = models.DateField()
    plan_of_today = models.TextField()
    working_of_today = models.TextField()
    plan_of_tomorrow = models.TextField()
    output = models.TextField(blank=True, default='')
    unresolved = models.TextField(blank=True, default='')
    time_of_create = models.DateTimeField('CreateTime', auto_now_add=True)
    time_of_update = models.DateTimeField('UpdateTime', auto_now=True)

    class Meta:
        ordering = ['time']
        verbose_name = '日报表'
        verbose_name_plural = verbose_name

    @property
    def real_name(self):
        if self.user:
            return self.user.real_name
        else:
            return None

    @property
    def weight(self):
        if self.user:
            return self.user.weight
        else:
            return None

    def __str__(self):
        return self.id


# 周报
class WeeklyReport(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True, verbose_name='周报ID')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    time = models.DateField()
    plan_of_this_week = models.TextField()
    working_of_this_week = models.TextField()
    summary_of_this_week = models.TextField(blank=True, default='')
    unresolved = models.TextField()
    self_evaluation = models.TextField()
    improving_methods = models.TextField(blank=True, default='')
    plan_of_next_week = models.TextField()
    remark = models.TextField(blank=True, default='')
    time_of_create = models.DateTimeField('CreateTime', auto_now_add=True)
    time_of_update = models.DateTimeField('UpdateTime', auto_now=True)

    class Meta:
        ordering = ['time']
        verbose_name = '周报表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id
