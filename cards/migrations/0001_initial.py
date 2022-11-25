# Generated by Django 4.1.1 on 2022-11-19 22:24

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.IntegerField(max_length=20)),
                ('number', models.CharField(blank=True, max_length=16, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Card number must be entered in the format: '9999888877776666'.", regex='^\\+?1?\\d{16}$')])),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created date')),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='activity end date')),
                ('cvv', models.IntegerField()),
                ('balance', models.FloatField(default=0)),
                ('status', models.CharField(choices=[('INACTIVE', 'card is not active'), ('ACTIVE', 'card is active'), ('OVERDUE', 'card is overdue')], max_length=13)),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
    ]
