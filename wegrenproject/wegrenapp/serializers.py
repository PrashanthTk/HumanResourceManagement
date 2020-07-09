from rest_framework import serializers 
from .models import *
 
 
class HrmBranchSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = HrmBranch
        fields = "__all__"

class HrmOrganizationSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = HrmOrganization
        fields = "__all__"

class HrmFormDropdownSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = HrmDynamicFormDropdown
        fields = "__all__"

class HrmFormFieldSerializer(serializers.ModelSerializer):
    #dropdownmodel=HrmFormDropdownSerializer()
    class Meta:
        model = HrmDynamicFormField
        fields = "__all__"
    def create(self, validated_data):
       dddata = validated_data['field_description']
       print("=============Atleast I came here")
       form_field = HrmDynamicFormField.objects.create(**validated_data)
       if validated_data['field_type']==2:
           
           csv=dddata.split(',')
           dropdowndata=dict()
           print("OOOOOOOOOOOOOut of cuiroisity")
           #print(form_field['id'])
           for kv in csv:
                items=kv.split(':')
                dropdowndata['dropdown_label']=items[0]
                dropdowndata['dropdown_value']=items[1]
                dropdowndata['created_at']=validated_data['created_at']
                dropdowndata['updated_at']=validated_data['updated_at']
                #dropdowndata['form_field']=form_field['id']
                HrmDynamicFormDropdown.objects.create(form_field=form_field,**dropdowndata)

       return form_field

class HrmFormMasterSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = HrmDynamicFormMaster
        fields = "__all__"