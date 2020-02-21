# Generated by Django 2.1 on 2020-02-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='用户ID')),
                ('username', models.CharField(max_length=50, verbose_name='账户')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
                ('time_of_create', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('time_of_update', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
            },
        ),
    ]