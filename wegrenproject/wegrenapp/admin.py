from django.contrib import admin

# Register your models here.
from . import *

admin.site.register(models.HrmBranch)
admin.site.register(models.HrmOrganization)
admin.site.register(models.HrmDynamicFormField)
admin.site.register(models.HrmDynamicFormDropdown)
admin.site.register(models.HrmDynamicFormMaster)
