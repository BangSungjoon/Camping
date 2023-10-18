# Generated by Django 4.2.6 on 2023-10-16 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camping',
            fields=[
                ('cam_address', models.CharField(max_length=45)),
                ('cam_tel', models.CharField(max_length=45)),
                ('cam_env', models.CharField(blank=True, max_length=45, null=True)),
                ('cam_type', models.CharField(blank=True, max_length=45, null=True)),
                ('cam_period', models.CharField(blank=True, max_length=45, null=True)),
                ('cam_day', models.CharField(blank=True, max_length=45, null=True)),
                ('cam_no', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'camping',
                'managed': False,
            },
        ),
    ]