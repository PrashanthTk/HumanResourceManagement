from django.contrib import admin

# Register your models here.
from . import *

admin.site.register(models.hrm_branch)
admin.site.register(models.hrm_organization)
admin.site.register(models.hrm_dynamic_form_field)
admin.site.register(models.hrm_dynamic_form_dropdown)
admin.site.register(models.hrm_dynamic_form_master)