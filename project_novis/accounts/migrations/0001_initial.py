# Generated by Django 2.2 on 2019-04-10 12:46

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='Email address')),
                ('name', models.CharField(blank=True, help_text='Your real name, used only for user/callsign validation.', max_length=200, verbose_name='Name')),
                ('display_name', models.CharField(blank=True, help_text='Your name, shown on your callsign page.', max_length=200, verbose_name='Display name')),
                ('address', models.TextField(blank=True, max_length=512)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('bio', models.TextField(blank=True)),
                ('twitter', models.CharField(blank=True, help_text='Twitter username without @', max_length=64)),
                ('youtube', models.CharField(blank=True, help_text='YouTube channel ID', max_length=64, verbose_name='YouTube')),
                ('facebook', models.CharField(blank=True, help_text='Facebook username', max_length=64)),
                ('flickr', models.CharField(blank=True, help_text='flickr username', max_length=64)),
                ('vimeo', models.CharField(blank=True, help_text='Vimeo username', max_length=64)),
                ('skype', models.CharField(blank=True, max_length=64)),
                ('matrix', models.CharField(blank=True, max_length=128)),
                ('jabber', models.CharField(blank=True, max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserValidation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('approved_at', models.DateTimeField(blank=True, null=True)),
                ('validation_comment', models.TextField(blank=True)),
                ('validation_file', models.FileField(blank=True, null=True, upload_to='user_validation/')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='approved_from', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
