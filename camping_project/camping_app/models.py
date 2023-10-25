from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Booking(models.Model):
    book_no = models.AutoField(primary_key=True)
    book_date = models.DateTimeField()
    stay_date = models.DateTimeField()
    camp_no = models.ForeignKey('CampInfo', models.DO_NOTHING, db_column='camp_no')
    id = models.ForeignKey('UsersAppUser', models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'booking'


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
    camp_name = models.CharField(max_length=100, blank=True, null=True)
    camp_s_tt = models.CharField(max_length=200, blank=True, null=True)
    camp_tag_li = models.CharField(max_length=500, blank=True, null=True)
    camp_address = models.CharField(max_length=100, blank=True, null=True)
    camp_call = models.CharField(max_length=100, blank=True, null=True)
    camp_environment = models.CharField(max_length=100, blank=True, null=True)
    camp_type = models.CharField(max_length=100, blank=True, null=True)
    camp_type = models.CharField(max_length=100, blank=True, null=True)
    camp_ope_period = models.CharField(max_length=100, blank=True, null=True)
    camp_ope_day = models.CharField(max_length=100, blank=True, null=True)
    camp_pagelink = models.CharField(max_length=500, blank=True, null=True)
    camp_book = models.CharField(max_length=100, blank=True, null=True)
    camp_ope_day = models.CharField(max_length=100, blank=True, null=True)
    camp_pagelink = models.CharField(max_length=500, blank=True, null=True)
    camp_book = models.CharField(max_length=100, blank=True, null=True)
    camp_itd = models.TextField(blank=True, null=True)

    def __str__(self) :
        return self.camp_name
    
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
    id = models.ForeignKey('UsersAppUser', models.DO_NOTHING, db_column='id', blank=True, null=True)
    approve = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'camp_memeber_info'


class CampReview(models.Model):
    review_no = models.AutoField(primary_key=True)
    rev_title = models.CharField(max_length=100, blank=True, null=True)
    rev_content = models.TextField(blank=True, null=True)
    rev_date = models.DateTimeField()
    rev_rate = models.FloatField(blank=True, null=True)
    id = models.ForeignKey('UsersAppUser', models.DO_NOTHING, db_column='id', blank=True, null=True)
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersAppUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FavoriteList(models.Model):
    camp_no = models.IntegerField(primary_key=True)  # The composite primary key (camp_no, id) found, that is not supported. The first column is selected.
    id = models.ForeignKey('UsersAppUser', models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'favorite_list'
        unique_together = (('camp_no', 'id'),)

# class FavoriteList(models.Model):
#     fav_id = models.AutoField(primary_key=True)
#     camp_no = models.ForeignKey(CampInfo, models.DO_NOTHING, db_column='camp_no')
#     # id = models.ForeignKey(User, models.DO_NOTHING, db_column='id',  primary_key=True)   
#     id = models.ForeignKey(User, models.DO_NOTHING, db_column='id')

#     class Meta:
#         managed = False
#         db_table = 'favorite_list'


class ImageLink(models.Model):
    camp_no = models.OneToOneField(CampInfo, models.DO_NOTHING, db_column='camp_no', primary_key=True)
    main_img_link = models.CharField(max_length=150, blank=True, null=True)
    col1_img_link = models.CharField(max_length=150, blank=True, null=True)
    col2_img_link = models.CharField(max_length=150, blank=True, null=True)
    col3_img_link = models.CharField(max_length=150, blank=True, null=True)
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
    rep_no = models.IntegerField(primary_key=True)
    rep_content = models.CharField(max_length=500)
    rep_date = models.DateField(blank=True, null=True)
    inq_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inq_reply'


class UserInquire(models.Model):
    inq_no = models.AutoField(primary_key=True)
    inq_title = models.CharField(max_length=500)
    inq_content = models.CharField(max_length=500)
    inq_date = models.DateField(blank=True, null=True)
    rep_status = models.CharField(max_length=50)
    id = models.ForeignKey('UsersAppUser', models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'user_inquire'


class UsersAppCompanyuser(models.Model):
    user_ptr = models.OneToOneField('UsersAppUser', models.DO_NOTHING, primary_key=True)
    company_name = models.CharField(max_length=30)
    company_tel = models.CharField(max_length=20)
    company_address = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'users_app_companyuser'


class UsersAppUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    user_name = models.CharField(max_length=30)
    user_age = models.IntegerField(blank=True, null=True)
    user_gender = models.IntegerField(blank=True, null=True)
    user_tel = models.CharField(max_length=20)
    user_address = models.CharField(max_length=200, blank=True, null=True)
    user_subscribe_sms = models.IntegerField()
    user_subscribe_email = models.IntegerField()

    def __str__(self) :
        return self.username

    class Meta:
        managed = False
        db_table = 'users_app_user'


class UsersAppUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersAppUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_app_user_groups'
        unique_together = (('user', 'group'),)


class UsersAppUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersAppUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_app_user_user_permissions'
        unique_together = (('user', 'permission'),)