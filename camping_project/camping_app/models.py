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
class AllCamp(models.Model):
    camp_no = models.IntegerField(blank=True, null=True)
    camp_name = models.TextField(blank=True, null=True)
    camp_s_tt = models.TextField(blank=True, null=True)
    camp_tag_li = models.TextField(blank=True, null=True)
    camp_address = models.TextField(blank=True, null=True)
    camp_call = models.TextField(blank=True, null=True)
    camp_environment = models.TextField(blank=True, null=True)
    camp_type = models.TextField(blank=True, null=True)
    camp_ope_period = models.TextField(blank=True, null=True)
    camp_ope_day = models.TextField(blank=True, null=True)
    camp_pagelink = models.TextField(blank=True, null=True)
    camp_book = models.TextField(blank=True, null=True)
    camp_itd = models.TextField(blank=True, null=True)
    electric = models.TextField(blank=True, null=True)
    wifi = models.TextField(blank=True, null=True)
    firewood = models.TextField(blank=True, null=True)
    warm_water = models.TextField(blank=True, null=True)
    walking_load = models.TextField(blank=True, null=True)
    sports_ground = models.TextField(blank=True, null=True)
    market = models.TextField(blank=True, null=True)
    water_playground = models.TextField(blank=True, null=True)
    athletic_fac = models.TextField(blank=True, null=True)
    adv_ground = models.TextField(blank=True, null=True)
    trampoline = models.TextField(blank=True, null=True)
    camp_normal_off_season_price_wd = models.TextField(blank=True, null=True)   
    camp_normal_off_season_price_we = models.TextField(blank=True, null=True)   
    camp_normal_peak_season_price_wd = models.TextField(blank=True, null=True)  
    camp_normal_peak_season_price_we = models.TextField(blank=True, null=True)  
    camp_auto_off_season_price_wd = models.TextField(blank=True, null=True)     
    camp_auto_off_season_price_we = models.TextField(blank=True, null=True)     
    camp_auto_peak_season_price_wd = models.TextField(blank=True, null=True)    
    camp_auto_peak_season_price_we = models.TextField(blank=True, null=True)    
    camp_glam_off_season_price_wd = models.TextField(blank=True, null=True)     
    camp_glam_off_season_price_we = models.TextField(blank=True, null=True)     
    camp_glam_peak_season_price_wd = models.TextField(blank=True, null=True)    
    camp_glam_peak_season_price_we = models.TextField(blank=True, null=True)    
    camp_crv_off_season_price_wd = models.TextField(blank=True, null=True)      
    camp_crv_off_season_price_we = models.TextField(blank=True, null=True)      
    camp_crv_peak_season_price_wd = models.TextField(blank=True, null=True)     
    camp_crv_peak_season_price_we = models.TextField(blank=True, null=True)     
    camp_main_fac = models.TextField(blank=True, null=True)
    camp_etc_info = models.TextField(blank=True, null=True)
    camp_brazier = models.TextField(blank=True, null=True)
    camp_safe_fac = models.TextField(blank=True, null=True)
    main_img_link = models.TextField(blank=True, null=True)
    col1_img_link = models.TextField(blank=True, null=True)
    col2_img_link = models.TextField(blank=True, null=True)
    col3_img_link = models.TextField(blank=True, null=True)
    last1_img_link = models.TextField(blank=True, null=True)
    last2_img_link = models.TextField(blank=True, null=True)
    last3_img_link = models.TextField(blank=True, null=True)
    last4_img_link = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_camp'


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
    company_id = models.CharField(max_length=100, blank=True, null=True)        

    class Meta:
        managed = False
        db_table = 'camp_info'


class CampReview(models.Model):
    review_no = models.AutoField(primary_key=True)
    rev_title = models.CharField(max_length=100, blank=True, null=True)
    rev_content = models.TextField(blank=True, null=True)
    rev_date = models.DateTimeField(blank=True, null=True)
    rev_rate = models.FloatField(blank=True, null=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    camp_no = models.ForeignKey(CampInfo, models.DO_NOTHING, db_column='camp_no')

    class Meta:
        managed = False
        db_table = 'camp_review'


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


class FavoriteList(models.Model):
    camp_no = models.ForeignKey(CampInfo, models.DO_NOTHING, db_column='camp_no')
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'favorite_list'


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


class InqReply(models.Model):
    rep_no = models.AutoField(primary_key=True)
    rep_content = models.CharField(max_length=500)
    rep_date = models.DateField(blank=True, null=True)
    inq_no = models.ForeignKey('UserInquire', models.DO_NOTHING, db_column='inq_no')

    class Meta:
        managed = False
        db_table = 'inq_reply'


class UserInfo(models.Model):
    user_id = models.CharField(primary_key=True, max_length=100)
    pwd = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    email = models.CharField(max_length=100, blank=True, null=True)
    tel = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user_info'


class UserInquire(models.Model):
    inq_no = models.AutoField(primary_key=True)
    inq_title = models.CharField(max_length=500)
    inq_content = models.CharField(max_length=500)
    inq_date = models.DateField(blank=True, null=True)
    rep_status = models.CharField(max_length=50)
    user = models.ForeignKey(UserInfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_inquire'