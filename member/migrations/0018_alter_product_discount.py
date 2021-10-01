# Generated by Django 3.2.6 on 2021-10-01 09:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0017_auto_20210929_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Discount',
            field=models.FloatField(validators=[django.core.validators.RegexValidator('^((100)|(\\d{1,2}(\\.\\d*)?))$', '백분율 값을 입력해야합니다.')], verbose_name='할인율(%)'),
        ),
    ]