# Generated by Django 3.2.5 on 2021-10-06 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrangChu', '0006_auto_20211003_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('phone', models.TextField(null=True)),
                ('email', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='EmployeeBook', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='BookTrip',
        ),
    ]
