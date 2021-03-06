# Generated by Django 3.2.6 on 2021-09-24 14:37

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_exituser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prod_Categ_big',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='상품분류코드')),
                ('Name', models.CharField(db_index=True, max_length=50, verbose_name='상품분류명')),
                ('Intro', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='상품분류소개')),
            ],
        ),
        migrations.CreateModel(
            name='Prod_Categ_mid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='상품분류코드')),
                ('Name', models.CharField(db_index=True, max_length=50, verbose_name='상품분류명')),
                ('Intro', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='상품분류소개')),
                ('Big', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.prod_categ_big')),
            ],
        ),
        migrations.RemoveField(
            model_name='exituser',
            name='UID',
        ),
        migrations.RemoveField(
            model_name='exituser',
            name='UPW',
        ),
        migrations.RemoveField(
            model_name='exituser',
            name='Ucombid',
        ),
        migrations.RemoveField(
            model_name='exituser',
            name='Uemail',
        ),
        migrations.RemoveField(
            model_name='exituser',
            name='Umailrecive',
        ),
        migrations.RemoveField(
            model_name='exituser',
            name='Unick',
        ),
        migrations.RemoveField(
            model_name='exituser',
            name='Usmsrecive',
        ),
        migrations.RemoveField(
            model_name='exituser',
            name='Utel',
        ),
        migrations.AlterField(
            model_name='exituser',
            name='Uregisterday',
            field=models.DateTimeField(verbose_name='회원가입일'),
        ),
        migrations.AlterField(
            model_name='user',
            name='UID',
            field=models.CharField(db_index=True, max_length=20, unique=True, verbose_name='아이디'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Ucombid',
            field=models.CharField(db_index=True, max_length=12, null=True, unique=True, verbose_name='사업자등록번호'),
        ),
        migrations.CreateModel(
            name='Prod_Categ_sma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='상품분류코드')),
                ('Name', models.CharField(db_index=True, max_length=50, verbose_name='상품분류명')),
                ('Intro', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='상품분류소개')),
                ('Big', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.prod_categ_big')),
                ('Mid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.prod_categ_mid')),
            ],
        ),
    ]
