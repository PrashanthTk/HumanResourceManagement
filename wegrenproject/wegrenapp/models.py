# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class HrmBranch(models.Model):
    branchname = models.CharField(max_length=255)
    orgid = models.ForeignKey('HrmOrganization', models.DO_NOTHING, db_column='orgid')

    class Meta:
        managed = False
        db_table = 'hrm_branch'


class HrmDynamicFormDropdown(models.Model):
    dropdown_label = models.CharField(max_length=255)
    dropdown_value = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    form_field = models.ForeignKey('HrmDynamicFormField', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hrm_dynamic_form_dropdown'


class HrmDynamicFormField(models.Model):
    field_title = models.CharField(max_length=255)
    field_description = models.CharField(max_length=500)
    field_type = models.IntegerField()
    field_original_name = models.CharField(max_length=50, blank=True, null=True)
    field_hidden = models.SmallIntegerField()
    field_order = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    form_master = models.ForeignKey('HrmDynamicFormMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hrm_dynamic_form_field'


class HrmDynamicFormMaster(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    form_url = models.CharField(max_length=500)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    branch = models.ForeignKey(HrmBranch, models.DO_NOTHING, blank=True, null=True)
    organization = models.ForeignKey('HrmOrganization', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hrm_dynamic_form_master'


class HrmOrganization(models.Model):
    orgname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'hrm_organization'
