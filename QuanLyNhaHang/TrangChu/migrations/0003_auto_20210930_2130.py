# Generated by Django 3.2.5 on 2021-09-30 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrangChu', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='food_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='FoodCategory', to='TrangChu.foodcategory'),
        ),
        migrations.DeleteModel(
            name='MenuAndCategory',
        ),
    ]