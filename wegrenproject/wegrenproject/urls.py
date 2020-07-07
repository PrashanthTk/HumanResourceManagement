from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from wegrenapp import views

router = routers.DefaultRouter()

router.register('branches', views.BranchAPI)
router.register('organizations', views.OrganizationAPI)
router.register('formdropdowns', views.FormDropdownAPI)
router.register('formfield', views.FormFieldAPI)
router.register('formmaster', views.FormMasterAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]