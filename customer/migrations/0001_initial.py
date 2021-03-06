# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-11 22:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='name')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'customer',
                'verbose_name_plural': 'customers',
            },
        ),
        migrations.CreateModel(
            name='CustomerContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(choices=[(b'Mr', b'Mr'), (b'Ms', b'Ms'), (b'Mrs', b'Mrs')], max_length=10, null=True, verbose_name='salutation')),
                ('name', models.CharField(max_length=120, verbose_name='name of contact')),
                ('designation', models.CharField(max_length=120, null=True, verbose_name='contact designation')),
                ('address', models.TextField(blank=True, null=True, verbose_name='contact address')),
                ('telephone', models.CharField(max_length=20, null=True, verbose_name='contact telephone')),
                ('fax', models.CharField(max_length=20, null=True, verbose_name='contact fax')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='contact email')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer', verbose_name=b'customer')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'customer detail',
                'verbose_name_plural': 'customer details',
            },
        ),
    ]
