# Generated by Django 3.1.3 on 2021-01-20 16:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=100, unique=True)),
                ('acoount_no', models.CharField(max_length=220, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('current_balance', models.FloatField(validators=[django.core.validators.MinValueValidator(3000.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(validators=[django.core.validators.MaxValueValidator(100000.0)])),
                ('tx_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tx_from', to='core.customers')),
                ('tx_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tx_to', to='core.customers')),
            ],
        ),
    ]
