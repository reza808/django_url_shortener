# Generated by Django 2.2.8 on 2021-09-28 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_url_shortener.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=256, validators=[django_url_shortener.validators.validate_url])),
                ('shortcode', models.CharField(blank=True, max_length=15, unique=True)),
                ('expiry_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('password', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='short_urls', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='ClickEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sh_url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='clicks', to='django_url_shortener.ShortUrl')),
            ],
        ),
    ]
