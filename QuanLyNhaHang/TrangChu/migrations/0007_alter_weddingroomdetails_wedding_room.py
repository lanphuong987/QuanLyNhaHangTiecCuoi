# Generated by Django 3.2.5 on 2021-10-05 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrangChu', '0006_auto_20211003_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weddingroomdetails',
            name='wedding_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weddingroomdetails', to='TrangChu.weddingroom'),
        ),
    ]