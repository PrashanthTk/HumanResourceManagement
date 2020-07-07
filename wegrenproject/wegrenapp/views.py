from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *

class BranchAPI(viewsets.ModelViewSet):
    serializer_class = BranchSerializer
    queryset = hrm_branch.objects.all()

class OrganizationAPI(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = hrm_organization.objects.all()

class FormDropdownAPI(viewsets.ModelViewSet):
    serializer_class = FormDropdownSerializer
    queryset = hrm_dynamic_form_dropdown.objects.all()

class FormFieldAPI(viewsets.ModelViewSet):
    serializer_class = FormFieldSerializer
    queryset = hrm_dynamic_form_field.objects.all()

class FormMasterAPI(viewsets.ModelViewSet):
    serializer_class = FormMasterSerializer
    queryset = hrm_dynamic_form_master.objects.all()