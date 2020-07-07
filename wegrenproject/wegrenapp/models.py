from django.db import models

class hrm_branch(models.Model):
    id=models.AutoField(db_column='id',primary_key=True)
    branchname=models.CharField(max_length=255)
    
    class Meta:
        db_table= 'hrm_branch'

    def __str__(self):
        return self.id

class hrm_organization(models.Model):
    id=models.AutoField(db_column='id',primary_key=True)
    orgname=models.CharField(max_length=255)
    
    class Meta:
        db_table= 'hrm_organization'

    def __str__(self):
        return self.id

class hrm_dynamic_form_master(models.Model):

    id=models.AutoField(db_column='id',primary_key=True)
    title=models.CharField(null=False,max_length=255)
    description=models.CharField(max_length=1000)
    formurl=models.CharField(null=False,max_length=500)
    created_at=models.DateTimeField()
    updated_at = models.DateTimeField()
    branch_id=models.ForeignKey(hrm_branch,db_column='branch_id',on_delete=models.CASCADE)
    organization_id=models.ForeignKey(hrm_organization,db_column='organization_id',on_delete=models.CASCADE)

    class Meta:
        db_table= 'hrm_dynamic_form_master'

    def __str__(self):
        return self.id

class hrm_dynamic_form_field(models.Model):
    id=models.AutoField(db_column='id',primary_key=True)
    field_description=models.CharField(max_length=500,null=False)
    field_type=models.IntegerField(null=False)
    field_original_name=models.CharField(max_length=50)
    field_hidden=models.SmallIntegerField(null=False)
    field_order=models.IntegerField(null=False)
    created_at=models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=False)
    form_master_id=models.ForeignKey(hrm_dynamic_form_master,db_column='form_master_id',on_delete=models.CASCADE)
    class Meta:
        db_table= 'hrm_dynamic_form_field'

    def __str__(self):
        return self.id

class hrm_dynamic_form_dropdown(models.Model):
    id=models.AutoField(db_column='id',primary_key=True)
    dropdown_label=models.CharField(null=False,max_length=500)
    dropdown_value=models.CharField(null=False,max_length=500)
    created_at=models.DateTimeField()
    updated_at = models.DateTimeField()
    form_field_id=models.ForeignKey(hrm_dynamic_form_field,db_column='form_field_id',on_delete=models.CASCADE)
    class Meta:
        db_table= 'hrm_dynamic_form_dropdown'

    def __str__(self):
        return self.id

