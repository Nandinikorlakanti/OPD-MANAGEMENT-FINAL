# Generated by Django 5.1.7 on 2025-03-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_remove_appointment_description_appointment_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='doctorName',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patientName',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='status',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='symptom',
            field=models.CharField(max_length=100),
        ),
    ]
