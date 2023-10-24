# Generated by Django 4.2.6 on 2023-10-24 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camping_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampMemeberInfo',
            fields=[
                ('camp_no', models.AutoField(primary_key=True, serialize=False)),
                ('camp_name', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_s_tt', models.CharField(blank=True, max_length=200, null=True)),
                ('camp_tag_li', models.CharField(blank=True, max_length=500, null=True)),
                ('camp_address', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_call', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_environment', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_type', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_ope_period', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_ope_day', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_pagelink', models.CharField(blank=True, max_length=500, null=True)),
                ('camp_book', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_itd', models.TextField(blank=True, null=True)),
                ('id', models.BigIntegerField(blank=True, null=True)),
                ('approve', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'camp_memeber_info',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='CampReview',
        ),
        migrations.DeleteModel(
            name='FavoriteList',
        ),
        migrations.DeleteModel(
            name='InqReply',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
        migrations.DeleteModel(
            name='UserInquire',
        ),
    ]