# Generated by Django 2.1.11 on 2019-09-03 09:20

import ap_model.ap_models_utils.functions
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agencies', '0005_accountlockoutnew_agentdashboard_agentlevelash_agentnewrecruit_loggedinuser_manpowersummary_manpower'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashBoardImageSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, upload_to=ap_model.ap_models_utils.functions.image_path)),
                ('description', models.TextField(blank=True)),
                ('published', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dashboard Image Slider',
                'verbose_name_plural': 'Dashboard Image Slider',
            },
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Memo'), (2, 'Form'), (3, 'Training'), (4, 'HospitalProvider'), (5, 'MedicalTable'), (6, 'SalesIlustration'), (7, 'Guidance'), (8, 'GuideAms'), (9, 'FundFactSheet'), (10, 'GuideTmc')])),
                ('target', models.PositiveSmallIntegerField(choices=[(1, 'All'), (2, 'Agency'), (3, 'Takumi'), (4, 'Banca')], default=1)),
                ('name', models.CharField(max_length=255)),
                ('effective_date_start', models.DateField(blank=True, null=True)),
                ('effective_date_end', models.DateField(blank=True, null=True)),
                ('filename', models.FileField(upload_to=ap_model.ap_models_utils.functions.form_upload_path)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agencies.Department')),
                ('department_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agencies.DepartmentCategory')),
            ],
            options={
                'verbose_name': 'FileUpload',
                'verbose_name_plural': 'FileUploads',
            },
        ),
    ]
