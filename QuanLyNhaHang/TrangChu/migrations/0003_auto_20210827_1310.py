# Generated by Django 3.2.5 on 2021-08-27 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrangChu', '0002_auto_20210826_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to='avatar/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='weddingroom',
            name='hinh_chinh_dien',
            field=models.ImageField(upload_to='sanhcuoi/%Y/%m'),
        ),
    ]
