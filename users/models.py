from django.db import models


# 用户
class User(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True, verbose_name='用户ID')
    username = models.CharField(max_length=50, verbose_name='账户')
    password = models.CharField(max_length=50, verbose_name='密码')
    real_name = models.CharField(max_length=50, blank=True, default='', verbose_name='姓名')
    weight = models.IntegerField(default=1, verbose_name='排序权重')
    time_of_create = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    time_of_update = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id
