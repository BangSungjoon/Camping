from django.db import models
class CampFacInfo(models.Model):
    camp_no = models.OneToOneField('CampInfo', models.DO_NOTHING, db_column='camp_no', primary_key=True)
    camp_main_fac = models.CharField(max_length=100, blank=True, null=True)
    camp_etc_info = models.CharField(max_length=45, blank=True, null=True)
    camp_brazier = models.CharField(max_length=10, blank=True, null=True)
    camp_safe_fac = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'camp_fac_info'


class CampInfo(models.Model):
    camp_no = models.AutoField(primary_key=True)
    camp_name = models.CharField(max_length=100, blank=True, null=True)
    camp_s_tt = models.CharField(max_length=200, blank=True, null=True)
    camp_tag_li = models.CharField(max_length=500, blank=True, null=True)
    camp_address = models.CharField(max_length=100, blank=True, null=True)
    camp_call = models.CharField(max_length=100, blank=True, null=True)
    camp_environment = models.CharField(max_length=100, blank=True, null=True)
    camp_type = models.CharField(max_length=100, blank=True, null=True)
    camp_ope_period = models.CharField(max_length=100, blank=True, null=True)
    camp_ope_day = models.CharField(max_length=100, blank=True, null=True)
    camp_pagelink = models.CharField(max_length=500, blank=True, null=True)
    camp_book = models.CharField(max_length=100, blank=True, null=True)
    camp_itd = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'camp_info'


class CampMemeberInfo(models.Model):
    camp_no = models.AutoField(primary_key=True)
    camp_name = models.CharField(max_length=100, blank=True, null=True)
    camp_s_tt = models.CharField(max_length=200, blank=True, null=True)
    camp_tag_li = models.CharField(max_length=500, blank=True, null=True)
    camp_address = models.CharField(max_length=100, blank=True, null=True)
    camp_call = models.CharField(max_length=100, blank=True, null=True)
    camp_environment = models.CharField(max_length=100, blank=True, null=True)
    camp_type = models.CharField(max_length=100, blank=True, null=True)
    camp_ope_period = models.CharField(max_length=100, blank=True, null=True)
    camp_ope_day = models.CharField(max_length=100, blank=True, null=True)
    camp_pagelink = models.CharField(max_length=500, blank=True, null=True)
    camp_book = models.CharField(max_length=100, blank=True, null=True)
    camp_itd = models.TextField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    approve = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'camp_memeber_info'


class CampTypePrice(models.Model):
    camp_no = models.OneToOneField(CampInfo, models.DO_NOTHING, db_column='camp_no', primary_key=True)
    camp_normal_off_season_price_wd = models.IntegerField(blank=True, null=True)
    camp_normal_off_season_price_we = models.IntegerField(blank=True, null=True)
    camp_normal_peak_season_price_wd = models.IntegerField(blank=True, null=True)
    camp_normal_peak_season_price_we = models.IntegerField(blank=True, null=True)
    camp_auto_off_season_price_wd = models.IntegerField(blank=True, null=True)
    camp_auto_off_season_price_we = models.IntegerField(blank=True, null=True)
    camp_auto_peak_season_price_wd = models.IntegerField(blank=True, null=True)
    camp_auto_peak_season_price_we = models.IntegerField(blank=True, null=True)
    camp_glam_off_season_price_wd = models.IntegerField(blank=True, null=True)
    camp_glam_off_season_price_we = models.IntegerField(blank=True, null=True)
    camp_glam_peak_season_price_wd = models.IntegerField(blank=True, null=True)
    camp_glam_peak_season_price_we = models.IntegerField(blank=True, null=True)
    camp_crv_off_season_price_wd = models.IntegerField(blank=True, null=True)
    camp_crv_off_season_price_we = models.IntegerField(blank=True, null=True)
    camp_crv_peak_season_price_wd = models.IntegerField(blank=True, null=True)
    camp_crv_peak_season_price_we = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'camp_type_price'


class CampUtility(models.Model):
    camp_no = models.OneToOneField(CampInfo, models.DO_NOTHING, db_column='camp_no', primary_key=True)
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

class ImageLink(models.Model):
    camp_no = models.OneToOneField(CampInfo, models.DO_NOTHING, db_column='camp_no', primary_key=True)
    main_img_link = models.CharField(max_length=150, blank=True, null=True)
    col1_img_link = models.CharField(max_length=150, blank=True, null=True)
    col2_img_link = models.CharField(max_length=150, blank=True, null=True)
    col3_img_link = models.CharField(max_length=150, blank=True, null=True)
    last1_img_link = models.CharField(max_length=150, blank=True, null=True)
    last2_img_link = models.CharField(max_length=150, blank=True, null=True)
    last3_img_link = models.CharField(max_length=150, blank=True, null=True)
    last4_img_link = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_link'