# Generated by Django 3.2.5 on 2021-10-03 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrangChu', '0005_auto_20211003_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuinbill',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='menubills', to='TrangChu.menu'),
        ),
        migrations.AlterField(
            model_name='menuinbill',
            name='wedding_bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weddingmenubills', to='TrangChu.weddingbill'),
        ),
        migrations.AlterField(
            model_name='serviceinbill',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='servicebills', to='TrangChu.menu'),
        ),
        migrations.AlterField(
            model_name='serviceinbill',
            name='wedding_bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weddingservicebills', to='TrangChu.weddingbill'),
        ),
    ]