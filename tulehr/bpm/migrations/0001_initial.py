# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-03 22:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recruitmen', '0003_auto_20171003_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('observation', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('country_code', models.CharField(default='MX', max_length=5)),
                ('langage_code', models.CharField(default='es-MX', max_length=10)),
                ('time_zone_code', models.CharField(default='UTC-6', max_length=5)),
                ('insert_date', models.DateTimeField(verbose_name='Insert Date')),
                ('update_date', models.DateTimeField(verbose_name='Update Date')),
                ('delete_date', models.DateTimeField(verbose_name='Delete Date')),
                ('logical_status', models.CharField(default='INSERT', max_length=10)),
                ('is_historical', models.CharField(default='NO', max_length=3)),
                ('delete_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmsactivity_deleteuser', to=settings.AUTH_USER_MODEL)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmsactivity_insertuser', to=settings.AUTH_USER_MODEL)),
                ('role', models.ManyToManyField(to='recruitmen.Role')),
            ],
            options={
                'db_table': 'BPM_ACTIVITY',
            },
        ),
        migrations.CreateModel(
            name='ActivityInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('observation', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('country_code', models.CharField(default='MX', max_length=5)),
                ('langage_code', models.CharField(default='es-MX', max_length=10)),
                ('time_zone_code', models.CharField(default='UTC-6', max_length=5)),
                ('insert_date', models.DateTimeField(verbose_name='Insert Date')),
                ('update_date', models.DateTimeField(verbose_name='Update Date')),
                ('delete_date', models.DateTimeField(verbose_name='Delete Date')),
                ('logical_status', models.CharField(default='INSERT', max_length=10)),
                ('is_historical', models.CharField(default='NO', max_length=3)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bpm.Activity')),
            ],
            options={
                'db_table': 'BPM_ACTIVITY_INSTANCE',
            },
        ),
        migrations.CreateModel(
            name='ActivityInstanceStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('observation', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('country_code', models.CharField(default='MX', max_length=5)),
                ('langage_code', models.CharField(default='es-MX', max_length=10)),
                ('time_zone_code', models.CharField(default='UTC-6', max_length=5)),
                ('insert_date', models.DateTimeField(verbose_name='Insert Date')),
                ('update_date', models.DateTimeField(verbose_name='Update Date')),
                ('delete_date', models.DateTimeField(verbose_name='Delete Date')),
                ('logical_status', models.CharField(default='INSERT', max_length=10)),
                ('is_historical', models.CharField(default='NO', max_length=3)),
                ('delete_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmactinstcestts_deleteuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'BPM_ACTIVITY_INSTANCE_STATUS',
            },
        ),
        migrations.CreateModel(
            name='ActivityStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('observation', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('country_code', models.CharField(default='MX', max_length=5)),
                ('langage_code', models.CharField(default='es-MX', max_length=10)),
                ('time_zone_code', models.CharField(default='UTC-6', max_length=5)),
                ('insert_date', models.DateTimeField(verbose_name='Insert Date')),
                ('update_date', models.DateTimeField(verbose_name='Update Date')),
                ('delete_date', models.DateTimeField(verbose_name='Delete Date')),
                ('logical_status', models.CharField(default='INSERT', max_length=10)),
                ('is_historical', models.CharField(default='NO', max_length=3)),
                ('delete_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmactivitystatus_deleteuser', to=settings.AUTH_USER_MODEL)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmactivitystatus_inseruser', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmactivitystatus_updateuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'BPM_ACTIVITY_STATUS',
            },
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('observation', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('country_code', models.CharField(default='MX', max_length=5)),
                ('langage_code', models.CharField(default='es-MX', max_length=10)),
                ('time_zone_code', models.CharField(default='UTC-6', max_length=5)),
                ('insert_date', models.DateTimeField(verbose_name='Insert Date')),
                ('update_date', models.DateTimeField(verbose_name='Update Date')),
                ('delete_date', models.DateTimeField(verbose_name='Delete Date')),
                ('logical_status', models.CharField(default='INSERT', max_length=10)),
                ('is_historical', models.CharField(default='NO', max_length=3)),
                ('delete_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmactivitytype_deleteuser', to=settings.AUTH_USER_MODEL)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmactivitytype_inseruser', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmactivitytype_updateuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'BPM_ACTIVITY_TYPE',
            },
        ),
        migrations.CreateModel(
            name='FormInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('table_name', models.CharField(max_length=100)),
                ('table_row_id', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('observation', models.CharField(max_length=200)),
                ('country_code', models.CharField(default='MX', max_length=5)),
                ('langage_code', models.CharField(default='es-MX', max_length=10)),
                ('time_zone_code', models.CharField(default='UTC-6', max_length=5)),
                ('insert_date', models.DateTimeField(verbose_name='Insert Date')),
                ('update_date', models.DateTimeField(verbose_name='Update Date')),
                ('delete_date', models.DateTimeField(verbose_name='Delete Date')),
                ('logical_status', models.CharField(default='INSERT', max_length=10)),
                ('is_historical', models.CharField(default='NO', max_length=3)),
                ('delete_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmforminstance_deleteuser', to=settings.AUTH_USER_MODEL)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmforminstance_insertuser', to=settings.AUTH_USER_MODEL)),
                ('tenant_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitmen.Tenant')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmforminstance_updateuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'BPM_FORM_INSTANCE',
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('sub_title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('observation', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('country_code', models.CharField(default='MX', max_length=5)),
                ('langage_code', models.CharField(default='es-MX', max_length=10)),
                ('time_zone_code', models.CharField(default='UTC-6', max_length=5)),
                ('insert_date', models.DateTimeField(verbose_name='Insert Date')),
                ('update_date', models.DateTimeField(verbose_name='Update Date')),
                ('delete_date', models.DateTimeField(verbose_name='Delete Date')),
                ('logical_status', models.CharField(default='INSERT', max_length=10)),
                ('is_historical', models.CharField(default='NO', max_length=3)),
                ('delete_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmprocess_deleteuser', to=settings.AUTH_USER_MODEL)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmprocess_insertuser', to=settings.AUTH_USER_MODEL)),
                ('role', models.ManyToManyField(to='recruitmen.Role')),
            ],
            options={
                'db_table': 'BPM_PROCESS',
            },
        ),
        migrations.CreateModel(
            name='ProcessInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('observation', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('country_code', models.CharField(default='MX', max_length=5)),
                ('langage_code', models.CharField(default='es-MX', max_length=10)),
                ('time_zone_code', models.CharField(default='UTC-6', max_length=5)),
                ('insert_date', models.DateTimeField(verbose_name='Insert Date')),
                ('update_date', models.DateTimeField(verbose_name='Update Date')),
                ('delete_date', models.DateTimeField(verbose_name='Delete Date')),
                ('logical_status', models.CharField(default='INSERT', max_length=10)),
                ('is_historical', models.CharField(default='NO', max_length=3)),
                ('business_process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bpm.Process')),
                ('delete_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmsprocessinstance_deleteuser', to=settings.AUTH_USER_MODEL)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmsprocessinstance_insertuser', to=settings.AUTH_USER_MODEL)),
                ('role', models.ManyToManyField(to='recruitmen.Role')),
            ],
            options={
                'db_table': 'BPM_PROCESS_INSTANCE',
            },
        ),
        migrations.CreateModel(
            name='ProcessInstanceStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('observation', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('country_code', models.CharField(default='MX', max_length=5)),
                ('langage_code', models.CharField(default='es-MX', max_length=10)),
                ('time_zone_code', models.CharField(default='UTC-6', max_length=5)),
                ('insert_date', models.DateTimeField(verbose_name='Insert Date')),
                ('update_date', models.DateTimeField(verbose_name='Update Date')),
                ('delete_date', models.DateTimeField(verbose_name='Delete Date')),
                ('logical_status', models.CharField(default='INSERT', max_length=10)),
                ('is_historical', models.CharField(default='NO', max_length=3)),
                ('delete_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmprcssnstncstts_deleteuser', to=settings.AUTH_USER_MODEL)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmprcssnstncstts_inseruser', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmprcssnstncstts_updateuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'BPM_PROCESS_INSTANCE_STATUS',
            },
        ),
        migrations.CreateModel(
            name='ProcessPool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('sub_title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('observation', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('country_code', models.CharField(default='MX', max_length=5)),
                ('langage_code', models.CharField(default='es-MX', max_length=10)),
                ('time_zone_code', models.CharField(default='UTC-6', max_length=5)),
                ('insert_date', models.DateTimeField(verbose_name='Insert Date')),
                ('update_date', models.DateTimeField(verbose_name='Update Date')),
                ('delete_date', models.DateTimeField(verbose_name='Delete Date')),
                ('logical_status', models.CharField(default='INSERT', max_length=10)),
                ('is_historical', models.CharField(default='NO', max_length=3)),
                ('delete_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmsprocesspool_deleteuser', to=settings.AUTH_USER_MODEL)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmsprocesspool_insertuser', to=settings.AUTH_USER_MODEL)),
                ('tenant_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitmen.Tenant')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmsprocesspool_updateuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'BPM_PROCESS_POOL',
            },
        ),
        migrations.CreateModel(
            name='ProcessStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('observation', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('country_code', models.CharField(default='MX', max_length=5)),
                ('langage_code', models.CharField(default='es-MX', max_length=10)),
                ('time_zone_code', models.CharField(default='UTC-6', max_length=5)),
                ('insert_date', models.DateTimeField(verbose_name='Insert Date')),
                ('update_date', models.DateTimeField(verbose_name='Update Date')),
                ('delete_date', models.DateTimeField(verbose_name='Delete Date')),
                ('logical_status', models.CharField(default='INSERT', max_length=10)),
                ('is_historical', models.CharField(default='NO', max_length=3)),
                ('delete_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmprocessstatus_deleteuser', to=settings.AUTH_USER_MODEL)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmprocessstatus_inseruser', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmprocessstatus_updateuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'BPM_PROCESS_STATUS',
            },
        ),
        migrations.CreateModel(
            name='ProcessType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('observation', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('country_code', models.CharField(default='MX', max_length=5)),
                ('langage_code', models.CharField(default='es-MX', max_length=10)),
                ('time_zone_code', models.CharField(default='UTC-6', max_length=5)),
                ('insert_date', models.DateTimeField(verbose_name='Insert Date')),
                ('update_date', models.DateTimeField(verbose_name='Update Date')),
                ('delete_date', models.DateTimeField(verbose_name='Delete Date')),
                ('logical_status', models.CharField(default='INSERT', max_length=10)),
                ('is_historical', models.CharField(default='NO', max_length=3)),
                ('delete_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmprocesstype_deleteuser', to=settings.AUTH_USER_MODEL)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmprocesstype_insertuser', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmprocesstype_updateuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'BPM_PROCESS_TYPE',
            },
        ),
        migrations.AddField(
            model_name='processinstance',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bpm.ProcessStatus'),
        ),
        migrations.AddField(
            model_name='processinstance',
            name='tenant_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitmen.Tenant'),
        ),
        migrations.AddField(
            model_name='processinstance',
            name='update_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmsprocessinstance_updateuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='process',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bpm.ProcessStatus'),
        ),
        migrations.AddField(
            model_name='process',
            name='tenant_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitmen.Tenant'),
        ),
        migrations.AddField(
            model_name='process',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bpm.ProcessType'),
        ),
        migrations.AddField(
            model_name='process',
            name='update_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmprocess_updateuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activityinstancestatus',
            name='form_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bpm.FormInstance'),
        ),
        migrations.AddField(
            model_name='activityinstancestatus',
            name='insert_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmactinstcestts_inseruser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activityinstancestatus',
            name='update_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmactinstcestts_updateuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activityinstance',
            name='business_process_instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bpm.ProcessInstance'),
        ),
        migrations.AddField(
            model_name='activityinstance',
            name='delete_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmactivityinstance_deleteuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activityinstance',
            name='insert_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmactivityinstance_insertuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activityinstance',
            name='role',
            field=models.ManyToManyField(to='recruitmen.Role'),
        ),
        migrations.AddField(
            model_name='activityinstance',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bpm.ActivityInstanceStatus'),
        ),
        migrations.AddField(
            model_name='activityinstance',
            name='tenant_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitmen.Tenant'),
        ),
        migrations.AddField(
            model_name='activityinstance',
            name='update_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmactivityinstance_updateuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bpm.ActivityStatus'),
        ),
        migrations.AddField(
            model_name='activity',
            name='tenant_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitmen.Tenant'),
        ),
        migrations.AddField(
            model_name='activity',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bpm.ActivityType'),
        ),
        migrations.AddField(
            model_name='activity',
            name='update_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bpmsactivity_updateuser', to=settings.AUTH_USER_MODEL),
        ),
    ]