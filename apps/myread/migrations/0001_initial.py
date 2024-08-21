# Generated by Django 5.1 on 2024-08-20 10:16

import django.contrib.postgres.fields.ranges
import django.contrib.postgres.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatusPercent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage_read_range', django.contrib.postgres.fields.ranges.IntegerRangeField(blank=True, null=True, validators=[django.contrib.postgres.validators.RangeMinValueValidator(0), django.contrib.postgres.validators.RangeMaxValueValidator(101)])),
                ('read_status', models.CharField(choices=[('pending', 'Pending'), ('reading', 'Reading'), ('done', 'Done')], default='pending', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Status Percentages',
                'constraints': [models.CheckConstraint(condition=models.Q(('read_status__in', ['pending', 'reading', 'done'])), name='myread_statuspercent_read_status_check')],
            },
        ),
    ]
