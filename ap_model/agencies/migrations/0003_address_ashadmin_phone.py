# Generated by Django 2.1.11 on 2019-09-03 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agencies', '0002_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_active', models.BooleanField(default=False)),
                ('is_default', models.BooleanField(default=True)),
                ('address', models.TextField(blank=True, default='')),
                ('zipcode', models.CharField(blank=True, default='', max_length=6)),
                ('agent_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agencies.AgentProfile')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Agent Address',
            },
        ),
        migrations.CreateModel(
            name='AshAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('ash_code', models.CharField(blank=True, max_length=255)),
                ('ash_username', models.CharField(blank=True, max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ash Admin',
                'verbose_name_plural': 'Ash Admins',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Fix Line'), (2, 'Mobile')], null=True)),
                ('number', models.CharField(blank=True, default='', max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('is_default', models.BooleanField(default=True)),
                ('agent_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agencies.AgentProfile')),
            ],
            options={
                'verbose_name': 'Phone',
                'verbose_name_plural': 'Agent Phones',
            },
        ),
    ]