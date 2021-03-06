# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-10 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0004_auto_20181010_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='username',
            field=models.CharField(default=1, max_length=40, verbose_name='持卡人姓名'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank',
            field=models.CharField(choices=[(0, '中国银行'), (1, '工商银行'), (2, '建设银行'), (3, '农业银行'), (4, '交通银行'), (5, '招商银行')], default=0, max_length=40, verbose_name='开户行'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='tradepwd',
            field=models.CharField(default=1, max_length=100, verbose_name='交易密码'),
            preserve_default=False,
        ),
    ]
