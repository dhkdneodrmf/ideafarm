# Generated by Django 3.2.6 on 2021-10-04 07:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0020_product_simexplanation'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Paytax',
            field=models.CharField(choices=[('1', '과세'), ('2', '면세')], default=1, max_length=1, verbose_name='과세유형'),
        ),
        migrations.AddField(
            model_name='product_qna',
            name='QTitle',
            field=models.CharField(db_index=True, default='', max_length=100, verbose_name='제목'),
        ),
        migrations.AddField(
            model_name='product_qna',
            name='QWriteday',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='작성일'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_review',
            name='RWriteday',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='작성일'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product_qna',
            name='Answer',
            field=models.TextField(db_index=True, max_length=10000, null=True, verbose_name='상품답변내용'),
        ),
        migrations.AlterField(
            model_name='product_qna',
            name='Question',
            field=models.TextField(db_index=True, max_length=10000, verbose_name='상품문의내용'),
        ),
        migrations.AlterField(
            model_name='product_review',
            name='Answer',
            field=models.TextField(db_index=True, max_length=10000, null=True, verbose_name='후기답변내용'),
        ),
        migrations.AlterField(
            model_name='product_review',
            name='Content',
            field=models.TextField(db_index=True, max_length=10000, verbose_name='상품리뷰'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Optioninfo', models.JSONField(default=dict, verbose_name='상품옵션정보')),
                ('Devliveryplace', models.CharField(max_length=200, verbose_name='배송지')),
                ('Payment', models.CharField(max_length=50, verbose_name='결제방법')),
                ('Devliverfee', models.PositiveIntegerField(verbose_name='배송비')),
                ('Orderprice', models.PositiveIntegerField(verbose_name='총결제금액')),
                ('Ordercondition', models.CharField(choices=[('1', '주문(결제)완료'), ('2', '입금확인'), ('3', '배송준비중'), ('4', '배송시작'), ('5', '배송완료'), ('6', '주문취소'), ('7', '반품처리'), ('8', '품절'), ('9', '기타')], default=1, max_length=1, verbose_name='주문상태')),
                ('registerday', models.DateTimeField(auto_now_add=True, verbose_name='주문등록일')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.product', verbose_name='해당제품')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.user', verbose_name='해당사용자')),
            ],
            options={
                'verbose_name': '장바구니',
                'verbose_name_plural': '장바구니',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Islike', models.BooleanField(default=False, verbose_name='좋아요 여부')),
                ('registerday', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.product', verbose_name='해당제품')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.user', verbose_name='해당사용자')),
            ],
            options={
                'verbose_name': '좋아요',
                'verbose_name_plural': '좋아요',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Optioninfo', models.JSONField(default=dict, verbose_name='상품옵션정보')),
                ('registerday', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.product', verbose_name='해당제품')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.user', verbose_name='해당사용자')),
            ],
            options={
                'verbose_name': '장바구니',
                'verbose_name_plural': '장바구니',
            },
        ),
    ]
