# Generated by Django 2.1.11 on 2019-09-03 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agencies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Tokio Marine Management'), (10, 'Tokio Marine Sub Management'), (2, 'Branch Admin'), (102, 'Branch Management'), (3, 'Senior Regional Sales Head'), (4, 'Regional Sales Head'), (5, 'Regional Director'), (6, 'Regional Manager Builder'), (7, 'Agency Manager Builder'), (14, 'Agency Manager Producer'), (8, 'Regional Manager Producer'), (9, 'Financial Consultant'), (11, 'Takumi Director'), (12, 'Takumi Manager'), (13, 'Takumi Consultant'), (15, 'Executive Takumi Consultant'), (16, 'Senior Takumi Consultant'), (17, 'Regional Bancassurance Manager'), (18, 'Executive Bancassurance Consultant'), (19, 'Senior Bancassurance Consultant'), (20, 'Bancassurance Consultant')], null=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='agencies.Level')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Level',
                'verbose_name_plural': 'Agent Level',
            },
        ),
    ]
