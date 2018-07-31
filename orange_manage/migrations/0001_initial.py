# Generated by Django 2.0.7 on 2018-07-26 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddresLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('superior_id', models.IntegerField(blank=True, null=True)),
                ('site_name', models.CharField(max_length=255)),
                ('character', models.IntegerField()),
            ],
            options={
                'db_table': 'addres_library',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orangeapiadminaccount',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=255)),
                ('admin_pwd', models.CharField(max_length=255)),
                ('admin_key', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'orangeapiadminaccount',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.AutoField(primary_key=True, serialize=False)),
                ('region_name', models.CharField(blank=True, max_length=255, null=True)),
                ('team_id', models.IntegerField()),
                ('province_id', models.IntegerField()),
                ('city_id', models.IntegerField()),
                ('area_id', models.IntegerField()),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_name', models.CharField(max_length=255)),
                ('shop_logo', models.CharField(max_length=255)),
                ('university_id', models.IntegerField()),
                ('campus_id', models.IntegerField()),
                ('region_id', models.IntegerField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=255)),
                ('shop_type', models.IntegerField()),
                ('province', models.IntegerField()),
                ('city', models.IntegerField()),
                ('county', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('business_license', models.CharField(max_length=255)),
                ('catering_license', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('manager_id', models.IntegerField()),
                ('default_account', models.IntegerField(blank=True, null=True)),
                ('alipay_account', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_account', models.CharField(blank=True, max_length=255, null=True)),
                ('shop_photos', models.CharField(blank=True, max_length=255, null=True)),
                ('packing_commission', models.IntegerField()),
                ('auth', models.IntegerField(blank=True, null=True)),
                ('start_business_time', models.DateTimeField(blank=True, null=True)),
                ('end_business_time', models.DateTimeField(blank=True, null=True)),
                ('notice', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField()),
                ('money', models.FloatField()),
                ('money_state', models.IntegerField(blank=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'shop',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ShopAssistant',
            fields=[
                ('shop_assistant_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('profile_image', models.CharField(blank=True, max_length=255, null=True)),
                ('is_assistant', models.IntegerField()),
                ('university_id', models.IntegerField()),
                ('campus_id', models.IntegerField()),
                ('shop_id', models.IntegerField()),
                ('register_time', models.DateTimeField()),
                ('last_login', models.DateTimeField()),
                ('permission', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'shop_assistant',
                'managed': False,
            },
        ),
    ]
