# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apigw', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='unfiltered_params',
            field=models.CharField(default=b'', help_text='\u591a\u4e2a\u4ee5\u9017\u53f7\u5206\u9694\uff0c\u654f\u611f\u53c2\u6570\u5c06\u5728API Gateway\u88ab\u8fc7\u6ee4\uff0c\u4e0d\u5411\u540e\u7aef\u4f20\u9012\uff0c\u4f46\u662f\u7f51\u5173\u6307\u5b9a\u4e0d\u8fc7\u6ee4\u7684\u53c2\u6570\uff0c\u5c06\u4f1a\u88ab\u5411\u540e\u4f20\u9012', max_length=512, verbose_name='\u4e0d\u8fc7\u6ee4\u7684\u53c2\u6570', blank=True),
        ),
        migrations.AlterField(
            model_name='api',
            name='api_type',
            field=models.IntegerField(default=10, verbose_name='API\u5206\u7c7b', choices=[(0, 'ESB'), (1, '\u5b98\u65b9\u4e91API'), (10, '\u4e91API[\u9694\u79bb\u533a]'), (11, '\u4e91API[\u975e\u9694\u79bb\u533a]')]),
        ),
    ]
