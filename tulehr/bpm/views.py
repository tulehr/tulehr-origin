# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date, datetime
from django.shortcuts import render, render_to_response
from .models import ProcessInstance,Activity,ActivityInstanceStatus,ActivityInstance, Process, ProcessInstanceStatus, ProcessStatus
from recruitmen.models import Role,Tenant

from MetaData import Router

# Create your views here.
''' ########################################################################
BUSINESS PROCESS MANAGEMENT
######################################################################## '''

URL_BPM_WORKLIST="bpm/worklist/bpm_worklist.html"
URL_BPM_TIMELINE_VIEW="bpm/timeline/bpm_timeline.html"

def bpm_worklist(request):
    page_title="Listado de Tareas"
    process_instance_list = ProcessInstance.objects.order_by('name')
    context = {
                'page_title': page_title,
                'process_instance_list': process_instance_list,
               }
    return render(request, URL_BPM_WORKLIST, context)

def bpm_timeline(request):
    page_title = "Seguimiento del Proceso de Requisicion de Personal"
    if request.method == "GET":
        processInstanceId = request.GET.get("processInstanceId")
        activity_instance_list = ActivityInstance.objects.filter(business_process_instance=processInstanceId,
                                                                 country_code="MX").order_by('name')
        context = {
                    'page_title': page_title,
                    'activity_instance_list': activity_instance_list,
                   }
        print("processInstanceId: " + str(processInstanceId))
    return render_to_response(URL_BPM_TIMELINE_VIEW, locals())


def bpm_create_process(auth_user,tenant,requisition_id):
    process=Process().objects.filter(code="BPM/HR/RP001")
    process_status=ProcessStatus().objects.filter(code="ACTIVE")
    role = Role().objects.filter(code="RQSTN_RL")
    process_instance=ProcessInstance()
    process_instance.name = ""
    process_instance.description = ""
    process_instance.observation = ""
    process_instance.notes = ""
    process_instance.business_process = process
    process_instance.status = process_status
    process_instance.role = role
    process_instance.tenant_code = tenant
    process_instance.country_code = "MX"
    process_instance.langage_code = "es-MX"
    process_instance.time_zone_code = "UTC-6"
    process_instance.insert_user=auth_user
    process_instance.insert_date = datetime.today()
    process_instance.logical_status = "INSERT"
    process_instance.is_historical = "NO"
    #Create Activity Instance
    activity_instance_status=ActivityInstanceStatus()
    #Create Activity
    activity=Activity().objects.filter(code="BPM/HR/RP001/ACT001")
    activity_instance=ActivityInstance()
    activity_instance.name = ""
    activity_instance.description = ""
    activity_instance.observation = ""
    activity_instance.notes = ""
    activity_instance.business_process_instance = process_instance
    activity_instance.activity = activity
    activity_instance.status = activity_instance_status
    activity_instance.role = role #Role of the activity
    activity_instance.tenant_code = tenant
    activity_instance.country_code = "MX"
    activity_instance.langage_code = "es-MX"
    activity_instance.time_zone_code = "UTC-6"
    activity_instance.insert_user=auth_user
    activity_instance.insert_date = datetime.today()
    activity_instance.logical_status = "INSERT"
    activity_instance.is_historical = "NO"
    return ""

'''########################################################################'''


def router_list(request):
    page_title="Listado de Roters"
    
    cadena="fferferfer frefreferfre ferferferf referfre \n fferferfer frefreferfre ferferferf referfre"
    registros= cadena.split("\n")
    for linea in registros:        
        lista_renglon = linea.split(" ")
        r = Router(linea[0])

    lista = [r]
    process_instance_list = []
    context = {
                'page_title': page_title,
                'lista': lista,
               }
    return render(request, URL_BPM_WORKLIST, context)

