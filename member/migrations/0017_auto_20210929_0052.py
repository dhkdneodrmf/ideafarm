# Generated by Django 3.2.6 on 2021-09-28 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0016_alter_devlivery_com_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Option',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name='상품옵션'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProdRelation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.product', verbose_name='연관상품 선택'),
        ),
    ]