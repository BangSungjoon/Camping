from django.db import models

# Create your models here.
class Camping(models.Model):
    cam_name = models.CharField(max_length=45)
    cam_address = models.CharField(max_length=45)
    cam_tel = models.CharField(max_length=45)
    cam_env = models.CharField(max_length=45, blank=True, null=True)
    cam_type = models.CharField(max_length=45, blank=True, null=True)
    cam_period = models.CharField(max_length=45, blank=True, null=True)
    cam_day = models.CharField(max_length=45, blank=True, null=True)
    cam_no = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'camping'
        
class CampImages(models.Model):
    main_image_id = models.AutoField(primary_key=True)
    main_image_name = models.CharField(max_length=255, blank=True, null=True)
    main_image_path = models.CharField(max_length=255, blank=True, null=True)
    cam_no = models.ForeignKey('Camping', models.DO_NOTHING, db_column='cam_no', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'camp_images'

# python manage.py inspectdb 하여 나오는 결과 복사 붙여 넣기!
class CampUtility(models.Model):
    camp_no = models.IntegerField(blank=True, null=True)
    electric = models.IntegerField(blank=True, null=True)
    wifi = models.IntegerField(blank=True, null=True)
    firewood = models.IntegerField(blank=True, null=True)
    warm_water = models.IntegerField(blank=True, null=True)
    walking_load = models.IntegerField(blank=True, null=True)
    sports_ground = models.IntegerField(blank=True, null=True)
    market = models.IntegerField(blank=True, null=True)
    water_playground = models.IntegerField(blank=True, null=True)       
    athletic_fac = models.IntegerField(blank=True, null=True)
    adv_ground = models.IntegerField(blank=True, null=True)
    trampoline = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'camp_utility'