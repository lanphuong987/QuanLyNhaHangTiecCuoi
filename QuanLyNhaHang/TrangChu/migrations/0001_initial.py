# Generated by Django 3.2.5 on 2021-09-13 04:04

import ckeditor.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.TextField(blank=True, null=True)),
                ('phonecus', models.CharField(max_length=10, null=True, unique=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('date_start', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('address', models.TextField(blank=True, null=True)),
                ('type', models.IntegerField()),
                ('date_start', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('active', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('hinh', models.ImageField(upload_to='menu/%Y/%m')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeddingRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('active', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('hinh_chinh_dien', models.ImageField(upload_to='sanhcuoi/%Y/%m')),
                ('max', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeddingRoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(upload_to='avatar/%Y/%m')),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='WeddingRoomDeTails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('wedding_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WeddingRopmDetails', to='TrangChu.weddingroom')),
            ],
        ),
        migrations.AddField(
            model_name='weddingroom',
            name='wedding_room_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WeddingRoomType', to='TrangChu.weddingroomtype'),
        ),
        migrations.CreateModel(
            name='WeddingBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('date_start', models.DateTimeField()),
                ('guest', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('earnest_money', models.DecimalField(decimal_places=2, max_digits=15)),
                ('is_organize', models.BooleanField(default=False)),
                ('pay_off', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CustomerBill', to='TrangChu.customer')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='EmployeeBill', to='TrangChu.employee')),
                ('wedding_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WeddingRoomBill', to='TrangChu.weddingroom')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceInBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SIBService', to='TrangChu.menu')),
                ('wedding_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SIBBill', to='TrangChu.weddingbill')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('active', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('hinh', models.ImageField(upload_to='service/%Y/%m')),
                ('service_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ServiceCategory', to='TrangChu.servicecategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(null=True)),
                ('is_contact', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='UserRating', to=settings.AUTH_USER_MODEL)),
                ('wedding_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BillRating', to='TrangChu.weddingbill')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='UserNotification', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MenuInBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='MIBMenu', to='TrangChu.menu')),
                ('wedding_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MIBBill', to='TrangChu.weddingbill')),
            ],
        ),
        migrations.CreateModel(
            name='MenuAndCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='MenuId', to='TrangChu.menu')),
                ('menu_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='MenuCategory', to='TrangChu.foodcategory')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_Employee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_Customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CostsIncurred',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('reason', models.TextField(null=True)),
                ('wedding_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Incurred', to='TrangChu.weddingbill')),
            ],
        ),
        migrations.CreateModel(
            name='BookTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('is_confirmed', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='EmployeeBook', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserBook', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
