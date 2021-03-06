# Generated by Django 3.2.5 on 2021-10-03 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrangChu', '0004_auto_20211003_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weddingbill',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customerbill', to='TrangChu.customer'),
        ),
        migrations.AlterField(
            model_name='weddingbill',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employeebill', to='TrangChu.employee'),
        ),
        migrations.AlterField(
            model_name='weddingbill',
            name='wedding_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weddingroombill', to='TrangChu.weddingroom'),
        ),
    ]
