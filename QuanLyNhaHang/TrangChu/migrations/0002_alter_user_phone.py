# Generated by Django 3.2.5 on 2021-09-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrangChu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
