# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EsbAuthApplyReocrd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operator', models.CharField(max_length=32, verbose_name='\u7533\u8bf7\u4eba')),
                ('app_code', models.CharField(max_length=32, verbose_name='\u7533\u8bf7\u7684\u5e94\u7528')),
                ('sys_name', models.CharField(max_length=128, verbose_name='\u7ec4\u4ef6\u7cfb\u7edf\u540d\u79f0')),
                ('api_id', models.IntegerField(verbose_name='\u7ec4\u4ef6\u7cfb\u7edfAPI ID')),
                ('api_name', models.CharField(max_length=128, verbose_name='\u7ec4\u4ef6\u7cfb\u7edfAPI\u540d\u79f0')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('approver', models.CharField(max_length=32, null=True, verbose_name='\u5ba1\u6279\u4eba', blank=True)),
                ('approval_result', models.CharField(default=b'applying', max_length=32, verbose_name='\u5ba1\u6279\u7ed3\u679c', choices=[(b'applying', '\u7533\u8bf7\u4e2d'), (b'pass', '\u5ba1\u6279\u901a\u8fc7'), (b'reject', '\u9a73\u56de')])),
                ('approval_time', models.DateTimeField(null=True, verbose_name='\u5ba1\u6279\u65f6\u95f4', blank=True)),
            ],
            options={
                'db_table': 'paas_app_esb_auth_apply_record',
                'verbose_name': 'app\u7ec4\u4ef6\u7533\u8bf7\u8bb0\u5f55\u8868',
                'verbose_name_plural': 'app\u7ec4\u4ef6\u7533\u8bf7\u8bb0\u5f55\u8868',
            },
        ),
    ]
