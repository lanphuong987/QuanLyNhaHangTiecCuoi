# Generated by Django 3.2.5 on 2021-10-21 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrangChu', '0008_merge_20211021_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='is_contact',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userrating', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rating',
            name='rate',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='wedding_bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billrating', to='TrangChu.weddingbill'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usercomment', to=settings.AUTH_USER_MODEL)),
                ('wedding_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billcomment', to='TrangChu.weddingbill')),
            ],
        ),
    ]
