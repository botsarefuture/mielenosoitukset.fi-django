# Generated by Django 5.0.1 on 2024-01-16 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Protest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('details', models.TextField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organization')),
                ('topics', models.ManyToManyField(to='topics.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('incompatible_roles', models.ManyToManyField(blank=True, to='protests.role')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('protest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protests.protest')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protests.role')),
            ],
        ),
    ]
