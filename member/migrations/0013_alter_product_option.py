# Generated by Django 3.2.6 on 2021-09-28 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0012_auto_20210927_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Option',
            field=models.CharField(max_length=5000, null=True, verbose_name='상품옵션'),
        ),
    ]
