# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# DJANGO Imports
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

from recruitmen.models import Role,Tenant



# Create your models here.
''' ####################################################################################### 
                       MODELO PARA EL SEGUIMIENTO Y CONTROL DE PROCESOS                 
########################################################################################### '''

''' *******************************************************************************
BPM_BUSINESS_PROCESS_STATUS
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: www.thulehr.com
@license: Apache 2.0 Licence
@summary: Entidad que almacena la definición de los procesos del sistema
************************************************************************************ '''
@python_2_unicode_compatible   
class ProcessStatus(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    country_code = models.CharField(max_length=5,default="MX") #Default Mexico
    langage_code = models.CharField(max_length=10,default="es-MX") #Default 
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_user=models.ForeignKey(User,related_name='bpmprocessstatus_inseruser')
    update_user=models.ForeignKey(User,related_name='bpmprocessstatus_updateuser')
    delete_user=models.ForeignKey(User,related_name='bpmprocessstatus_deleteuser')
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    class Meta:
        db_table = 'BPM_PROCESS_STATUS'
    def __str__(self): # __unicode__ on Python 2
        return self.name
''' ******************************************************************************* '''

''' *******************************************************************************
BPM_BUSINESS_PROCESS_TYPE
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: www.thulehr.com
@license: Apache 2.0 Licence
@summary: Entidad que almacena la definición de los procesos del sistema
************************************************************************************ '''
@python_2_unicode_compatible   
class ProcessType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    country_code = models.CharField(max_length=5,default="MX") #Default Mexico
    langage_code = models.CharField(max_length=10,default="es-MX") #Default 
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_user=models.ForeignKey(User,related_name='bpmprocesstype_insertuser')
    update_user=models.ForeignKey(User,related_name='bpmprocesstype_updateuser')
    delete_user=models.ForeignKey(User,related_name='bpmprocesstype_deleteuser')
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    class Meta:
        db_table = 'BPM_PROCESS_TYPE'
    def __str__(self): # __unicode__ on Python 2
        return self.name
''' ******************************************************************************* '''


''' *******************************************************************************
BPM_PROCESS
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: www.thulehr.com
@license: Apache 2.0 Licence
@summary: Entidad que almacena la definición de los procesos del sistema
************************************************************************************ '''
@python_2_unicode_compatible   
class Process(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    type = models.ForeignKey(ProcessType)
    status = models.ForeignKey(ProcessStatus)
    role = models.ManyToManyField(Role)
    tenant_code = models.ForeignKey(Tenant) #Indicar que fue creado en el tenant maestro
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_user=models.ForeignKey(User,related_name='bpmprocess_insertuser')
    update_user=models.ForeignKey(User,related_name='bpmprocess_updateuser')
    delete_user=models.ForeignKey(User,related_name='bpmprocess_deleteuser')
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    class Meta:
        db_table = 'BPM_PROCESS'
    def __str__(self): # __unicode__ on Python 2
        return self.name

''' *******************************************************************************
BPM_PROCESS_POOL
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: www.thulehr.com
@license: Apache 2.0 Licence
@summary: Entidad que almacena la definición de los procesos del sistema
************************************************************************************ '''
@python_2_unicode_compatible   
class ProcessPool(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    tenant_code = models.ForeignKey(Tenant) #Indicar que fue creado en el tenant maestro
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_user=models.ForeignKey(User,related_name='bpmsprocesspool_insertuser')
    update_user=models.ForeignKey(User,related_name='bpmsprocesspool_updateuser')
    delete_user=models.ForeignKey(User,related_name='bpmsprocesspool_deleteuser')
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    class Meta:
        db_table = 'BPM_PROCESS_POOL'
    def __str__(self): # __unicode__ on Python 2
        return self.name


''' *******************************************************************************
BPM_ACTIVITY_STATUS
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: www.thulehr.com
@license: Apache 2.0 Licence
@summary: Entidad que almacena la definición de los procesos del sistema
************************************************************************************ '''
@python_2_unicode_compatible   
class ActivityStatus(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    country_code = models.CharField(max_length=5,default="MX") #Default Mexico
    langage_code = models.CharField(max_length=10,default="es-MX") #Default 
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_user=models.ForeignKey(User,related_name='bpmactivitystatus_inseruser')
    update_user=models.ForeignKey(User,related_name='bpmactivitystatus_updateuser')
    delete_user=models.ForeignKey(User,related_name='bpmactivitystatus_deleteuser')
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    class Meta:
        db_table = 'BPM_ACTIVITY_STATUS'
    def __str__(self): # __unicode__ on Python 2
        return self.name
''' ******************************************************************************* '''

''' *******************************************************************************
BPM_ACTIVITY_TYPE
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: www.thulehr.com
@license: Apache 2.0 Licence
@summary: Entidad que almacena la definición de los procesos del sistema
************************************************************************************ '''
@python_2_unicode_compatible   
class ActivityType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    country_code = models.CharField(max_length=5,default="MX") #Default Mexico
    langage_code = models.CharField(max_length=10,default="es-MX") #Default 
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_user=models.ForeignKey(User,related_name='bpmactivitytype_inseruser')
    update_user=models.ForeignKey(User,related_name='bpmactivitytype_updateuser')
    delete_user=models.ForeignKey(User,related_name='bpmactivitytype_deleteuser')
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    class Meta:
        db_table = 'BPM_ACTIVITY_TYPE'
    def __str__(self): # __unicode__ on Python 2
        return self.name
''' ******************************************************************************* '''

''' *******************************************************************************
BPM_ACTIVITY
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: www.thulehr.com
@license: Apache 2.0 Licence
@summary: Entidad que almacena la definición las actividades del sistema
************************************************************************************ '''
@python_2_unicode_compatible   
class Activity(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    type = models.ForeignKey(ActivityType)
    status = models.ForeignKey(ActivityStatus)
    role = models.ManyToManyField(Role)
    tenant_code = models.ForeignKey(Tenant) #Indicar que fue creado en el tenant maestro
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_user=models.ForeignKey(User,related_name='bpmsactivity_insertuser')
    update_user=models.ForeignKey(User,related_name='bpmsactivity_updateuser')
    delete_user=models.ForeignKey(User,related_name='bpmsactivity_deleteuser')
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    class Meta:
        db_table = 'BPM_ACTIVITY'
    def __str__(self): # __unicode__ on Python 2
        return self.name

''' *******************************************************************************
BPM_PROCESS_INSTANCE_STATUS
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: www.thulehr.com
@license: Apache 2.0 Licence
@summary: Entidad que almacena la definición de los procesos del sistema
************************************************************************************ '''
@python_2_unicode_compatible   
class ProcessInstanceStatus(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    country_code = models.CharField(max_length=5,default="MX") #Default Mexico
    langage_code = models.CharField(max_length=10,default="es-MX") #Default 
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_user=models.ForeignKey(User,related_name='bpmprcssnstncstts_inseruser')
    update_user=models.ForeignKey(User,related_name='bpmprcssnstncstts_updateuser')
    delete_user=models.ForeignKey(User,related_name='bpmprcssnstncstts_deleteuser')
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    class Meta:
        db_table = 'BPM_PROCESS_INSTANCE_STATUS'
    def __str__(self): # __unicode__ on Python 2
        return self.name
''' ******************************************************************************* '''

''' *******************************************************************************
BPM_PROCESS_INSTANCE
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: www.thulehr.com
@license: Apache 2.0 Licence
@summary: Entidad que almacena las instancias de un proceso
************************************************************************************ '''
@python_2_unicode_compatible   
class ProcessInstance(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    business_process = models.ForeignKey(Process)
    status = models.ForeignKey(ProcessStatus)
    role = models.ManyToManyField(Role)
    tenant_code = models.ForeignKey(Tenant) #Indicar que fue creado en el tenant maestro
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_user=models.ForeignKey(User,related_name='bpmsprocessinstance_insertuser')
    update_user=models.ForeignKey(User,related_name='bpmsprocessinstance_updateuser')
    delete_user=models.ForeignKey(User,related_name='bpmsprocessinstance_deleteuser')
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    class Meta:
        db_table = 'BPM_PROCESS_INSTANCE'
    def __str__(self): # __unicode__ on Python 2
        return self.name

''' *******************************************************************************
BPM_ACTIVITY_INSTANCE_STATUS
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: www.thulehr.com
@license: Apache 2.0 Licence
@summary: Entidad que almacena un formulario relacionado con una actividad
************************************************************************************ '''
@python_2_unicode_compatible   
class FormInstance(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    table_name = models.CharField(max_length=100) #Nombre de la tabla referenciada
    table_row_id = models.CharField(max_length=100) #Id del registro del formulario
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    tenant_code = models.ForeignKey(Tenant) #Tenant del cliente
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_user=models.ForeignKey(User,related_name='bpmforminstance_insertuser')
    update_user=models.ForeignKey(User,related_name='bpmforminstance_updateuser')
    delete_user=models.ForeignKey(User,related_name='bpmforminstance_deleteuser')
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    class Meta:
        db_table = 'BPM_FORM_INSTANCE'
    def __str__(self): # __unicode__ on Python 2
        return self.name
    
''' *******************************************************************************
BPM_ACTIVITY_INSTANCE_STATUS
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: www.thulehr.com
@license: Apache 2.0 Licence
@summary: Entidad que almacena la definición de los procesos del sistema
************************************************************************************ '''
@python_2_unicode_compatible   
class ActivityInstanceStatus(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    form_id = models.ForeignKey(FormInstance) #Referencia un formulario relacionado con la actividad
    country_code = models.CharField(max_length=5,default="MX") #Default Mexico
    langage_code = models.CharField(max_length=10,default="es-MX") #Default 
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_user=models.ForeignKey(User,related_name='bpmactinstcestts_inseruser')
    update_user=models.ForeignKey(User,related_name='bpmactinstcestts_updateuser')
    delete_user=models.ForeignKey(User,related_name='bpmactinstcestts_deleteuser')
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    class Meta:
        db_table = 'BPM_ACTIVITY_INSTANCE_STATUS'
    def __str__(self): # __unicode__ on Python 2
        return self.name
''' ******************************************************************************* '''

''' *******************************************************************************
BPM_ACTIVITY_INSTANCE
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: www.thulehr.com
@license: Apache 2.0 Licence
@summary: Entidad que almacena la definición las actividades del sistema
************************************************************************************ '''
@python_2_unicode_compatible   
class ActivityInstance(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    business_process_instance = models.ForeignKey(ProcessInstance)
    activity = models.ForeignKey(Activity)
    status = models.ForeignKey(ActivityInstanceStatus)
    role = models.ManyToManyField(Role)
    tenant_code = models.ForeignKey(Tenant) #Tenant del cliente
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_user=models.ForeignKey(User,related_name='bpmactivityinstance_insertuser')
    update_user=models.ForeignKey(User,related_name='bpmactivityinstance_updateuser')
    delete_user=models.ForeignKey(User,related_name='bpmactivityinstance_deleteuser')
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    class Meta:
        db_table = 'BPM_ACTIVITY_INSTANCE'
    def __str__(self): # __unicode__ on Python 2
        return self.name