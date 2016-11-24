# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 01:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('montanha', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=248, verbose_name='Name')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Supplier Activity',
                'verbose_name_plural': 'Supplier Activities',
            },
        ),
        migrations.CreateModel(
            name='SupplierJuridicalNature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=248, verbose_name='Name')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Supplier Juridical Nature',
                'verbose_name_plural': 'Supplier Juridical Nature',
            },
        ),
        migrations.CreateModel(
            name='SupplierSituation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Supplier Situation',
                'verbose_name_plural': 'Supplier Situations',
            },
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='main_economic_activity',
        ),
        migrations.AddField(
            model_name='supplier',
            name='address_complement',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Address Complement'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='address_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Address Number'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='enterprise_type',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Enterprise Type'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='federative_officer',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Federative Officer'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='last_update',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last Update'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='neighborhood',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Neighborhood'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='postal_code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='situation_date',
            field=models.DateField(blank=True, null=True, verbose_name='Situation Date'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='situation_reason',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Situation Reason'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='special_situation',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Special Situation'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='special_situation_date',
            field=models.DateField(blank=True, null=True, verbose_name='Special Situation Date'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='state',
            field=models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='juridical_nature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='montanha.SupplierJuridicalNature', verbose_name='Juridical Nature'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='status',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='main_activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='montanha.SupplierActivity', verbose_name='Main Activity'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='secondary_activities',
            field=models.ManyToManyField(blank=True, related_name='secondary_activities', to='montanha.SupplierActivity', verbose_name='Secondary Activities'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='situation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='montanha.SupplierSituation', verbose_name='Situation'),
        ),
    ]