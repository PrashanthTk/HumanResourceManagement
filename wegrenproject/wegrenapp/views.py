from django.shortcuts import render, redirect
from rest_framework import viewsets
from wegrenapp.forms import *
from wegrenapp.models import *
from .serializers import *

class HrmBranchAPI(viewsets.ModelViewSet):
    serializer_class = HrmBranchSerializer
    queryset = HrmBranch.objects.all()

class HrmOrganizationAPI(viewsets.ModelViewSet):
    serializer_class = HrmOrganizationSerializer
    queryset = HrmOrganization.objects.all()

class HrmFormDropdownAPI(viewsets.ModelViewSet):
    serializer_class = HrmFormDropdownSerializer
    queryset = HrmDynamicFormDropdown.objects.all()

class HrmFormFieldAPI(viewsets.ModelViewSet):
    serializer_class = HrmFormFieldSerializer
    queryset = HrmDynamicFormField.objects.all()

    """def create(self, request, *args, **kwargs):
        response = super(HrmFormFieldAPI, self).create(request, *args, **kwargs)
        # here may be placed additional operations for
        # extracting id of the object and using reverse()
        
        
        if request.POST.get("field_type","")=='2':
                                    
            return redirect('/api/formdropdowns/')
        return response"""

    
class HrmFormMasterAPI(viewsets.ModelViewSet):
    serializer_class = HrmFormMasterSerializer
    queryset = HrmDynamicFormMaster.objects.all()


def formmaster(request):  

    if request.method == "POST":  
        form = HrmDynamicFormMasterForm(request.POST)
        print("Form has been posted")
        print(form)
        if form.is_valid():
            print("Form is valid")    
            try:

                form.save()  
                
                return redirect('/api/formmaster/show/')  
            except:  
                pass  
    else:  
        form = HrmDynamicFormMasterForm()
        print("Form data needs to be checked")
        print(form)
    orgs=HrmOrganization.objects.all()
    return render(request,'index.html',{'form':form,'organizations':orgs})
def show(request):  
    formmasters = HrmDynamicFormMaster.objects.all()
    return render(request,"show.html",{'formmasters':formmasters})  
def edit(request, id):  
    formmasters = HrmDynamicFormMaster.objects.get(id=id)  
    return render(request,'edit.html', {'formmaster':formmaster})  
def update(request, id):  
    formmasters = HrmDynamicFormMaster.objects.get(id=id)  
    form = HrmDynamicFormMaster(request.POST, instance = formmaster)  
    if form.is_valid():  
        form.save()  
        return redirect("/api/formmaster/show/")  
    return render(request, 'edit.html', {'formmaster': formmaster})  
def destroy(request, id):  
    formmaster = HrmDynamicFormMaster.objects.get(id=id)  
    formmaster.delete()  
    return redirect("/api/formmaster/show/")  

def load_branches(request):
    org_id = request.GET.get('organization')
    branches = HrmBranch.objects.filter(orgid=org_id).order_by('branchname')
    return render(request, 'branch_dropdown_list_options.html', {'branches': branches})