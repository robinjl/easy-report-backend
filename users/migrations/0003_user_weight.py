# Generated by Django 2.1 on 2020-02-21 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_real_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.IntegerField(default=1, verbose_name='排序权重'),
        ),
    ]