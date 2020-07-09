from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from wegrenapp import views

app_name = 'wegrenapp'
router = routers.DefaultRouter()

router.register('branches', views.HrmBranchAPI)
router.register('organizations', views.HrmOrganizationAPI)
#router.register('formdropdowns', views.HrmFormDropdownAPI)
router.register('formfield', views.HrmFormFieldAPI)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    #path('api/org/',views.org,name='org'),
    
    path('api/formmaster/',views.formmaster,name='formmaster'),
    path('api/formmaster/show/',views.show,name='showformmaster'),
    path('api/formmaster/edit/<int:id>',views.edit,name='editformmaster'),
    path('api/formmaster/update/<int:id>',views.update,name='updateformmaster'),
    path('api/formmaster/delete/<int:id>',views.destroy,name='destroyformmaster'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches')
]