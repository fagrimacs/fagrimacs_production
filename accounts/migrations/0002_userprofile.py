# Generated by Django 3.0.7 on 2020-09-18 06:25

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_pic', models.ImageField(default='profile_pics/user.png', upload_to=accounts.models.profile_pic_filename, verbose_name='Profile Picture')),
                ('website', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Profile',
            },
        ),
    ]
