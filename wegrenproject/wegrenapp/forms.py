from django import forms  
from wegrenapp.models import *  
class HrmOrganizationForm(forms.ModelForm):  
    class Meta:  
        model = HrmOrganization  
        fields = "__all__" 

class HrmDynamicFormMasterForm(forms.ModelForm):
	class Meta:
		model=HrmDynamicFormMaster
		fields="__all__"

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['branch'].queryset = HrmBranch.objects.none()
		if 'organization' in self.data:
		    try:
		        orgid = int(self.data.get('organization'))
		        self.fields['branch'].queryset = HrmBranch.objects.filter(orgid=orgid).order_by('branchname')
		    except (ValueError, TypeError):
		        pass  # invalid input from the client; ignore and fallback to empty organization queryset
		elif self.instance.id:
			self.fields['branch'].queryset = self.instance.organization.branches.order_by('branchname')