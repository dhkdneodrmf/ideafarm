# Generated by Django 3.2.6 on 2021-09-17 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_auto_20210916_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mberterm', models.TextField(max_length=6000, verbose_name='회원가입약관')),
                ('Privterm', models.TextField(max_length=6000, verbose_name='개인정보처리방침')),
                ('registerday', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
            ],
        ),
    ]
