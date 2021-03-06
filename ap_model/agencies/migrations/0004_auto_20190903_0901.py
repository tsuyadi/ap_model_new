# Generated by Django 2.1.11 on 2019-09-03 09:01

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('agencies', '0003_address_ashadmin_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('account_no', models.CharField(blank=True, default='', max_length=255)),
                ('account_holder_name', models.CharField(blank=True, default='', max_length=255)),
                ('is_default', models.BooleanField(default=True)),
                ('agent_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agencies.AgentProfile')),
            ],
            options={
                'verbose_name': 'Bank',
                'verbose_name_plural': 'Agent Bank Account',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='DepartmentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'DepartmentCategory',
                'verbose_name_plural': 'DepartmentCategories',
            },
        ),
        migrations.CreateModel(
            name='Manpower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('ra', models.IntegerField(default=0)),
                ('aa', models.IntegerField(default=0)),
                ('nr', models.IntegerField(default=0)),
                ('at', models.IntegerField(default=0)),
                ('reactive_agent', models.IntegerField(default=0)),
                ('case_group', models.IntegerField(default=0)),
                ('case_personal', models.IntegerField(default=0)),
                ('qc_personal', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('qc_group', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('position', models.CharField(max_length=2)),
                ('hierdate', models.DateField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agencies.AgentProfile')),
            ],
            options={
                'verbose_name': 'manpower',
                'verbose_name_plural': 'Agent Manpower',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='department_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agencies.DepartmentCategory'),
        ),
    ]
