from rest_framework import serializers 
from .models import *
 
 
class BranchSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = hrm_branch
        fields = ('id',
                  'branchname'
                  )

class OrganizationSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = hrm_organization
        fields = "__all__"

class FormDropdownSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = hrm_dynamic_form_dropdown
        fields = "__all__"

class FormFieldSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = hrm_dynamic_form_field
        fields = "__all__"

class FormMasterSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = hrm_dynamic_form_master
        fields = "__all__"