# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import generic

from datetime import date, datetime

from .models import EmployeeRequisition, CustomerCompany, Position,WorkArea,Language
from .models import CostCenter,PhysicalLocation,PreferredGender,WorkingHours,IndustryExperience
from .models import AgeRange,EducationLevel,Degree,VacancyProfile,Employee,LanguageLevelLanguage
from .models import Knowledge,Ability,ProfessionalProfile,School,Person,ProfessionalExperience
# Eror and loging management
import traceback
import logging
# Business Process Management
from .models import Role

# Config
from models import Tenant

'''
LISTA DE ACCIONES POSIBLES EN EL SISTEMA
'''
ACTION_VIEW="view"
ACTION_LIST="list"
ACTION_SEARCH="search"
ACTION_INSERT="insert"
ACTION_UPDATE="update"
ACTION_DELETE="delete"

'''
NOTAS Y REFERENCIAS
    MANEJO DE SESIONES:
    http://ech-db.readthedocs.io/ru/latest/chapter14.html
    FORMULARIOS:
    https://docs.djangoproject.com/en/1.11/topics/forms/
'''

URL_INDEX="recruitmen/index.html"
URL_LOGIN="recruitmen/login.html"
URL_LOGIN_ERROR="recruitmen/login_error.html"
URL_GENERIC_ERROR="recruitmen/generic_error.html"

EMAIL_SITE_ADMIN = "info@tulehr.com"

# Create your views here.
def index(request):
    page_title = "Tablero de control"
    latest_empleado_list = Employee.objects.order_by('-created_date')[:5]
    return render_to_response('recruitmen/index.html', locals())

def login(request):
    page_message=""
    if request.method == "POST":
        try:
            user_name = str(request.POST.get("user_name"))
            user_password = str(request.POST.get("user_password"))
            logging.debug("user_name: " + user_name)
            logging.debug("user_password: " + user_password)
            print("user_name: " + user_name)
            print("user_password: " + user_password)
            authUser = auth.authenticate(username=user_name, password=user_password)
            if authUser is not None:
                print "Usuario Correcto"
                auth.login(request, authUser)
                print("User Id:" + str(authUser.id))
                page_message="El usuario se autentico correctamente"
                # Get Tenant information
                if authUser.id>0:
                    try:
                        tenant = Tenant.objects.get(auth_user=authUser.id)
                        print(tenant.id)
                        request.session['tenant_id'] = tenant.id
                        print("Nombre del tenant: " + tenant.name)
                        request.session['auth_user_username'] = authUser.username
                        print "debug 1"
                        context = {'auth_user': str(authUser.username),'tenant':str(tenant.id),'page_message': page_message}
                        print "debug 2"
                        return render(request, URL_INDEX, context)
                    except:
                        print("No hay tenant dado de alta")
                        error_message = "Usuario no tiene un tenant asignado"
                        context = {'error_message': error_message}
                        traceback.print_exc()
                        return render(request, URL_LOGIN, context)
                else:
                    tenant=None
                    request.session['tenant_id'] = "None"
                    error_message = "El usuario indicado no tiene un Tenant dado de alta, favor de contactar al administrador del sitio: " + EMAIL_SITE_ADMIN
                    context = {'error_message': error_message}
                    return render(request, URL_LOGIN, context)
            else:
                print "Usuario Invalido"
                error_message = "Usuario invalido, favor de validar el nombre de usuario y password"
                context = {'auth_user': authUser,'error_message': error_message}
                page_message="El correo electronico o password no existen, favor de validar"
                return render(request, URL_LOGIN, context)
        except:
            print("Error in login")
            error_message = "Hubo un error al momento de autenticar, favor de contactar al administrador del sitio: " + EMAIL_SITE_ADMIN
            context = {'error_message': error_message}
            return render(request, URL_LOGIN, context)
    context = {'page_message': page_message}
    return render(request, URL_LOGIN, context)


''' *******************************************************************************
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: www.tulehr.com Technologies S.A. de C.V:
@license: MIT
@summary: Controlador login out
************************************************************************************ '''
def log_out(request):
    print("Logout of user")
    logout(request)
    return render(request, URL_LOGIN)
''' ************************************************************************************ '''


'''
Requisition View
########################################################################
'''
URL_REQUISITION_LIST="recruitmen/requisition/requisition_list.html"
URL_REQUISITION_NEW="recruitmen/requisition/requisition_new.html"
URL_REQUISITION_UPDATE="recruitmen/requisition/requisition_update.html"
URL_REQUISITION_DELETE="recruitmen/requisition/requisition_update.html"
URL_REQUISITION_VIEW="recruitmen/requisition/requisition_view.html"
URL_PROSPECT_LIST="recruitmen/prospect/prospect_list.html"
URL_PROSPECT_NEW="recruitmen/prospect/prospect_new.html"
URL_PROSPECT_UPDATE="recruitmen/prospect/prospect_update.html"

def requisition_list(request):
    page_title = "Lista de Requisiciones"
    requisition_list = EmployeeRequisition.objects.order_by('employee_requisition_number')
    context = {'requisition_list': requisition_list}
    return render(request,URL_REQUISITION_LIST, context)
#    return render_to_response('recruitmen/requisition/requisition_list.html', locals())

def compute_detail(request):
    page_title = "Creacion de Instancia"
    context = {'page_title': page_title}
    return render(request, 'portal/resource/compute/compute_detail.html', context)


def requisition_view(request):
    page_title = "Detalle de la Requisicion"
    return render_to_response('recruitmen/requisition/requisition_view.html', locals())

#def requisition_new(request):
#    page_title = "Nueva Requisicion"
#    return render_to_response('recruitmen/requisition/requisition_new.html', locals())

def requisition_new(request):
    PositionList = Position.objects.order_by('name')
    WorkAreaList = WorkArea.objects.order_by('name')
    CostCenterList=CostCenter.objects.order_by('name')
    CustomerCompanyList=CustomerCompany.objects.order_by('comercial_name')
    EmployeeList=Employee.objects.order_by('employee_number')
    PhysicalLocationList=PhysicalLocation.objects.order_by('name')
    PreferredGenderList=PreferredGender.objects.order_by('name')
    WorkingHoursList=WorkingHours.objects.order_by('name')
    IndustryExperienceList=IndustryExperience.objects.order_by('name')
    AgeRangeList=AgeRange.objects.order_by('edad_inicial')
    EducationLevelList=EducationLevel.objects.order_by('name')
    DegreeList=Degree.objects.order_by('name')
    LanguageLevelLanguageList=LanguageLevelLanguage.objects.order_by('name')
    KnowledgeList=Knowledge.objects.order_by('name')
    AbilityList=Ability.objects.order_by('name')
    vm_pooling=0
    message=""
    page_title = "Nueva Requisicion"
    if request.method == "POST":
            #service = AwsComputeService()
            #enableMonitoring= service.to_bool(request.POST.get("enableMonitoring"))
            requisition_requested_by = request.POST.get("requisition_requested_by")
            position = request.POST.get("position")
            company_destination=request.POST.get("company_destination")
            work_area=request.POST.get("work_area")
            cost_center=request.POST.get("cost_center")
            physical_location=request.POST.get("physical_location")
            company_extencion_phone=request.POST.get("company_extencion_phone")
            immediate_boss_position=request.POST.get("immediate_boss_position")
            immediate_boss=request.POST.get("immediate_boss")
            immediate_boss_direccion=request.POST.get("immediate_boss_direccion")
            #Perfil de la Vacante
            position_to_search=request.POST.get("position_to_search")
            requested_amount=request.POST.get("requested_amount")
            education_level=request.POST.get("education_level")
            possible_degree=request.POST.get("possible_degree")
            language_level=request.POST.get("language_level")
            description_experience=request.POST.get("description_experience")
            years_experience=request.POST.get("years_experience")
            industry_experience=request.POST.get("industry_experience")
            knowledge=request.POST.get("knowledge")
            ability=request.POST.get("ability")
            prioritize_knowledge=request.POST.get("prioritize_knowledge")
            position_salary=request.POST.get("position_salary")
            position_salary_total=request.POST.get("position_salary_total")
            working_hours_profile=request.POST.get("working_hours_profile")
            preferred_gender=request.POST.get("preferred_gender")
            location=request.POST.get("location")
            age_range=request.POST.get("age_range")
            profile_company_contractor=request.POST.get("profile_company_contractor")
            employee_internal_interviewer=request.POST.get("employee_internal_interviewer")
            position_emp=request.POST.get("position_emp")
            location_emp=request.POST.get("location_emp")
            position_seg=request.POST.get("position_seg")
            location_seg=request.POST.get("location_seg")
            company_extencion_phone_seg=request.POST.get("company_extencion_phone_seg")
            employee_tracing=request.POST.get("employee_tracing")
            manager_tracing=request.POST.get("manager_tracing")
            search_start_date=request.POST.get("search_start_date")
            commitment_date=request.POST.get("commitment_date")
            hr_process_tracing=request.POST.get("hr_process_tracing")
            position_hr=request.POST.get("position_hr")
            location_hr=request.POST.get("location_hr")
            company_extencion_phone_hr=request.POST.get("company_extencion_phone_hr")
            hr_contractor_area=request.POST.get("hr_contractor_area")
            req = EmployeeRequisition()
            req.employee_requisition_number="001" 
            req.name="Requisicion de personal" 
            req.requisition_requested_by=Employee.objects.get(pk=requisition_requested_by) # Requisición solicitada por
            req.company_destination=CustomerCompany.objects.get(pk=company_destination)#Empresa de destino
            req.work_area =WorkArea.objects.get(pk=work_area)#�?rea de trabajo 
            req.cost_center=CostCenter.objects.get(pk=cost_center)#Centro de costos
            req.physical_location=PhysicalLocation.objects.get(pk=physical_location)#Localizacion fisica
            req.immediate_boss =Employee.objects.get(pk=immediate_boss)#Jefe inmediato
            req.immediate_boss_position=Position.objects.get(pk=immediate_boss_position)#Puesto del Jefe inmediato
            req.immediate_boss_direccion =WorkArea.objects.get(pk=immediate_boss_direccion) ##Direccion Jefe inmediato 
            req.start_date=datetime.today()
            
            vp=VacancyProfile()
            vp.profile_code ="002" # Código de perfil solicitado
            vp.profile_name ="Perfil generico" # Nombre del perfil solicitado
            vp.requested_position=Position.objects.get(pk=position_to_search) # Posición solicitada para alguna área
            vp.requested_amount =requested_amount # Cantidad de posición solicitada
            vp.description_experience=description_experience #Descripción de su experiencia
            vp.years_experience =years_experience #Años de experiencia
            vp.industry_experience=IndustryExperience.objects.get(pk=industry_experience) #Experiencia industrial
            vp.age_range=AgeRange.objects.get(pk=age_range) #rango de edad
            vp.insert_date=datetime.today()
            vp.save()
            vp.education_level.add(EducationLevel.objects.get(pk=education_level)) #Nivel de formación del perfil solicitado
            vp.possible_degree.add(Degree.objects.get(pk=possible_degree)) # Posible licenciatura
            vp.language_level.add(LanguageLevelLanguage.objects.get(pk=language_level)) # Nivel del idioma
            vp.knowledge.add(Knowledge.objects.get(pk=knowledge)) # Conocimiento del candidato
            vp.ability.add(Ability.objects.get(pk=ability)) #Habilidad
            vp.prioritize_knowledge.add(Knowledge.objects.get(pk=prioritize_knowledge)) #Priorizar el conocimiento
            #vp.tenant_code
            #vp.country_code
            #vp.langage_code
            #vp.time_zone_code
            #vp.update_date
            #vp.delete_date
            #vp.logical_status
            #vp.is_historical
            req.vacancy_position_profile =vp
            req.position_salary=position_salary #Sueldo del puesto
            req.position_salary_total =position_salary_total  # Sueldo bruto del puesto
            req.profile_company_contractor=CustomerCompany.objects.get(pk=profile_company_contractor)# Empresa que contrata el perfil
            req.working_hours_profile=WorkingHours.objects.get(pk=working_hours_profile)# Horario de trabajo
            req.preferred_gender=PreferredGender.objects.get(pk=preferred_gender)# Genero preferido
            req.position_work_area=WorkArea.objects.get(pk=1)
            req.employee_internal_interviewer=Employee.objects.get(pk=1)
            req.position_to_search=Position.objects.get(pk=position_to_search)# Posicion buscada
                #Cliente
            req.location=WorkArea.objects.get(pk=1)
            req.location_phone_internal=company_extencion_phone_seg #Teléfono interno de la ubicación
            req.employee_tracing=Employee.objects.get(pk=employee_tracing)#Empleado interno que dara seguimiento
                #Gerente CAT
            req.manager_tracing=Employee.objects.get(pk=manager_tracing)#Gerente que dara seguimiento
            req.search_start_date=search_start_date#Fecha de inicio de la búsqueda
            req.commitment_date=commitment_date#Fecha de compromiso
                #Cliente HR
            req.hr_process_tracing=Employee.objects.get(pk=hr_process_tracing) # Empleado de RH responsable de darle seguimiento
            req.hr_contractor_area=WorkArea.objects.get(pk=hr_contractor_area)# Area de RH responsable de contratar
            #req.tenant_code
            #req.country_code
            #req.langage_code
            #req.time_zone_code
            req.insert_date=datetime.today()
            #req.update_date
            #req.delete_date
            #req.logical_status
            #req.is_historical
                        
            req.save()
            page_title = "Lista de Requisiciones"
            requisition_list = EmployeeRequisition.objects.order_by('employee_requisition_number')
            context = {'requisition_list': requisition_list}
            return render(request, URL_REQUISITION_LIST, context)
    else:
        print("Mostrar formulario vacio: ")
        message=""
        context = {'page_title': page_title,
                   'vm_pooling': vm_pooling,
                   'message': message,
                   'PositionList': PositionList,
                   'WorkAreaList': WorkAreaList,
                   'CostCenterList':CostCenterList,
                   'CustomerCompanyList':CustomerCompanyList,
                   'EmployeeList':EmployeeList,
                   'PhysicalLocationList':PhysicalLocationList,
                   'PreferredGenderList':PreferredGenderList,
                   'WorkingHoursList':WorkingHoursList,
                   'IndustryExperienceList':IndustryExperienceList,
                   'AgeRangeList':AgeRangeList,
                   'EducationLevelList':EducationLevelList,
                   'DegreeList':DegreeList,
                   'LanguageLevelLanguageList':LanguageLevelLanguageList,
                   'KnowledgeList':KnowledgeList,
                   'AbilityList':AbilityList}
        return render(request, URL_REQUISITION_NEW, context)

def requisition_cancel(request):
    page_title = "Cancelar la Requisicion"
    return render_to_response('recruitmen/requisition/requisition_cancel.html', locals())

def requisition_update(request,requisition_id):
    objRequisition = EmployeeRequisition.objects.get(pk=requisition_id)
    PositionList = Position.objects.order_by('name')
    WorkAreaList = WorkArea.objects.order_by('name')
    CostCenterList=CostCenter.objects.order_by('name')
    CustomerCompanyList=CustomerCompany.objects.order_by('comercial_name')
    EmployeeList=Employee.objects.order_by('employee_number')
    PhysicalLocationList=PhysicalLocation.objects.order_by('name')
    PreferredGenderList=PreferredGender.objects.order_by('name')
    WorkingHoursList=WorkingHours.objects.order_by('name')
    IndustryExperienceList=IndustryExperience.objects.order_by('name')
    AgeRangeList=AgeRange.objects.order_by('edad_inicial')
    EducationLevelList=EducationLevel.objects.order_by('name')
    DegreeList=Degree.objects.order_by('name')
    LanguageLevelLanguageList=LanguageLevelLanguage.objects.order_by('name')
    KnowledgeList=Knowledge.objects.order_by('name')
    AbilityList=Ability.objects.order_by('name')
    vm_pooling=0
    page_title = "Actualizacion de Requisicion"
    if request.method == "POST":
            #service = AwsComputeService()
            #enableMonitoring= service.to_bool(request.POST.get("enableMonitoring"))
            requisition_requested_by = request.POST.get("requisition_requested_by")
            position = request.POST.get("position")
            company_destination=request.POST.get("company_destination")
            work_area=request.POST.get("work_area")
            cost_center=request.POST.get("cost_center")
            physical_location=request.POST.get("physical_location")
            company_extencion_phone=request.POST.get("company_extencion_phone")
            immediate_boss_position=request.POST.get("immediate_boss_position")
            immediate_boss=request.POST.get("immediate_boss")
            immediate_boss_direccion=request.POST.get("immediate_boss_direccion")
            #Perfil de la Vacante
            position_to_search=request.POST.get("position_to_search")
            requested_amount=request.POST.get("requested_amount")
            education_level=request.POST.get("education_level")
            possible_degree=request.POST.get("possible_degree")
            language_level=request.POST.get("language_level")
            description_experience=request.POST.get("description_experience")
            years_experience=request.POST.get("years_experience")
            industry_experience=request.POST.get("industry_experience")
            knowledge=request.POST.get("knowledge")
            ability=request.POST.get("ability")
            prioritize_knowledge=request.POST.get("prioritize_knowledge")
            position_salary=request.POST.get("position_salary")
            position_salary_total=request.POST.get("position_salary_total")
            working_hours_profile=request.POST.get("working_hours_profile")
            preferred_gender=request.POST.get("preferred_gender")
            location=request.POST.get("location")
            age_range=request.POST.get("age_range")
            profile_company_contractor=request.POST.get("profile_company_contractor")
            employee_internal_interviewer=request.POST.get("employee_internal_interviewer")
            position_emp=request.POST.get("position_emp")
            location_emp=request.POST.get("location_emp")
            position_seg=request.POST.get("position_seg")
            location_seg=request.POST.get("location_seg")
            company_extencion_phone_seg=request.POST.get("company_extencion_phone_seg")
            employee_tracing=request.POST.get("employee_tracing")
            manager_tracing=request.POST.get("manager_tracing")
            search_start_date=request.POST.get("search_start_date")
            commitment_date=request.POST.get("commitment_date")
            hr_process_tracing=request.POST.get("hr_process_tracing")
            position_hr=request.POST.get("position_hr")
            location_hr=request.POST.get("location_hr")
            company_extencion_phone_hr=request.POST.get("company_extencion_phone_hr")
            hr_contractor_area=request.POST.get("hr_contractor_area")
            req = objRequisition
            req.employee_requisition_number="001" 
            req.name="Requisicion de personal" 
            req.requisition_requested_by=Employee.objects.get(pk=requisition_requested_by) # Requisición solicitada por
            req.company_destination=CustomerCompany.objects.get(pk=company_destination)#Empresa de destino
            req.work_area =WorkArea.objects.get(pk=work_area)#�?rea de trabajo 
            req.cost_center=CostCenter.objects.get(pk=cost_center)#Centro de costos
            req.physical_location=PhysicalLocation.objects.get(pk=physical_location)#Localizacion fisica
            req.immediate_boss =Employee.objects.get(pk=immediate_boss)#Jefe inmediato
            req.immediate_boss_position=Position.objects.get(pk=immediate_boss_position)#Puesto del Jefe inmediato
            req.immediate_boss_direccion =WorkArea.objects.get(pk=immediate_boss_direccion) ##Direccion Jefe inmediato 
            req.start_date=datetime.today()
            
            vp=objRequisition.vacancy_position_profile
            vp.profile_code ="002" # Código de perfil solicitado
            vp.profile_name ="Perfil generico" # Nombre del perfil solicitado
            vp.requested_position=Position.objects.get(pk=position_to_search) # Posición solicitada para alguna área
            vp.requested_amount =requested_amount # Cantidad de posición solicitada
            vp.description_experience=description_experience #Descripción de su experiencia
            vp.years_experience =years_experience #Años de experiencia
            vp.industry_experience=IndustryExperience.objects.get(pk=industry_experience) #Experiencia industrial
            vp.age_range=AgeRange.objects.get(pk=age_range) #rango de edad
            #vp.insert_date=datetime.today()
            vp.save()
            vp.education_level.add(EducationLevel.objects.get(pk=education_level)) #Nivel de formación del perfil solicitado
            vp.possible_degree.add(Degree.objects.get(pk=possible_degree)) # Posible licenciatura
            vp.language_level.add(LanguageLevelLanguage.objects.get(pk=language_level)) # Nivel del idioma
            vp.knowledge.add(Knowledge.objects.get(pk=knowledge)) # Conocimiento del candidato
            vp.ability.add(Ability.objects.get(pk=ability)) #Habilidad
            vp.prioritize_knowledge.add(Knowledge.objects.get(pk=prioritize_knowledge)) #Priorizar el conocimiento
            #vp.tenant_code
            #vp.country_code
            #vp.langage_code
            #vp.time_zone_code
            vp.update_date=datetime.today()
            #vp.delete_date
            #vp.logical_status
            #vp.is_historical
            req.vacancy_position_profile =vp
            req.position_salary=position_salary #Sueldo del puesto
            req.position_salary_total =position_salary_total  # Sueldo bruto del puesto
            req.profile_company_contractor=CustomerCompany.objects.get(pk=profile_company_contractor)# Empresa que contrata el perfil
            req.working_hours_profile=WorkingHours.objects.get(pk=working_hours_profile)# Horario de trabajo
            req.preferred_gender=PreferredGender.objects.get(pk=preferred_gender)# Genero preferido
            req.position_work_area=WorkArea.objects.get(pk=1)
            req.employee_internal_interviewer=Employee.objects.get(pk=1)
            req.position_to_search=Position.objects.get(pk=position_to_search)# Posicion buscada
                #Cliente
            req.location=WorkArea.objects.get(pk=1)
            req.location_phone_internal=company_extencion_phone_seg #Teléfono interno de la ubicación
            req.employee_tracing=Employee.objects.get(pk=employee_tracing)#Empleado interno que dara seguimiento
                #Gerente CAT
            req.manager_tracing=Employee.objects.get(pk=manager_tracing)#Gerente que dara seguimiento
            req.search_start_date=search_start_date#Fecha de inicio de la búsqueda
            req.commitment_date=commitment_date#Fecha de compromiso
                #Cliente HR
            req.hr_process_tracing=Employee.objects.get(pk=hr_process_tracing) # Empleado de RH responsable de darle seguimiento
            req.hr_contractor_area=WorkArea.objects.get(pk=hr_contractor_area)# Area de RH responsable de contratar
            #req.tenant_code
            #req.country_code
            #req.langage_code
            #req.time_zone_code
            #req.insert_date=datetime.today()
            req.update_date=datetime.today()
            #req.delete_date
            #req.logical_status
            #req.is_historical
                        
            req.save()
            page_title = "Lista de Requisiciones"
            requisition_list = EmployeeRequisition.objects.order_by('employee_requisition_number')
            context = {'requisition_list': requisition_list}
            return render(request, URL_REQUISITION_LIST, context)
    else:
        print("Response generico")
        message=""
        context = {'page_title': page_title,
               'vm_pooling': vm_pooling,
               'message': message,
               'PositionList': PositionList,
               'WorkAreaList': WorkAreaList,
               'CostCenterList':CostCenterList,
               'CustomerCompanyList':CustomerCompanyList,
               'EmployeeList':EmployeeList,
               'PhysicalLocationList':PhysicalLocationList,
               'PreferredGenderList':PreferredGenderList,
               'WorkingHoursList':WorkingHoursList,
                'IndustryExperienceList':IndustryExperienceList,
                'AgeRangeList':AgeRangeList,
                'EducationLevelList':EducationLevelList,
                'DegreeList':DegreeList,
                'LanguageLevelLanguageList':LanguageLevelLanguageList,
                'KnowledgeList':KnowledgeList,
                'AbilityList':AbilityList,
                'objRequisition':objRequisition}
        return render(request, URL_REQUISITION_UPDATE, context)
        #return render('recruitmen/requisition/requisition_update.html', locals())

def requisition_timeline(request):
    page_title = "Seguimiento de la Requisicion"
    return render_to_response('recruitmen/requisition/requisition_timeline.html', locals())
'''
########################################################################
'''


'''
Requisition View
########################################################################
'''
def statistics_timeline(request):
    page_title = "Estadisticas de seguimiento"
    return render_to_response('recruitmen/statistics/statistics_timeline.html', locals())

def statistics_prospect(request):
    page_title = "Estadisticas de Candidatos"
    return render_to_response('recruitmen/statistics/statistics_prospect.html', locals())

def statistics_requisition(request):
    page_title = "Estadisticas de Candidatos"
    return render_to_response('recruitmen/statistics/statistics_requisition.html', locals())
'''
########################################################################
'''

'''
User
########################################################################
'''
def tenant_user_list(request):
    page_title = "Estadisticas de seguimiento"
    return render_to_response('recruitmen/tenant/user/user_list.html', locals())

def tenant_user_new(request):
    page_title = "Estadisticas de seguimiento"
    return render_to_response('recruitmen/tenant/user/user_new.html', locals())

def tenant_user_view(request):
    page_title = "Estadisticas de seguimiento"
    return render_to_response('recruitmen/tenant/user/user_view.html', locals())

def tenant_user_update(request):
    page_title = "Estadisticas de seguimiento"
    return render_to_response('recruitmen/tenant/user/user_update.html', locals())

def tenant_user_delete(request):
    page_title = "Borrar Uusuario"
    return render_to_response('recruitmen/tenant/user/user_delete.html', locals())

'''
########################################################################
'''

'''
Role
########################################################################
'''
def tenant_role_list(request):
    page_title = "Estadisticas de seguimiento"
    return render_to_response('recruitmen/tenant/role/role_list.html', locals())

def tenant_role_new(request):
    page_title = "Estadisticas de seguimiento"
    return render_to_response('recruitmen/tenant/role/role_new.html', locals())

def tenant_role_view(request):
    page_title = "Estadisticas de seguimiento"
    return render_to_response('recruitmen/tenant/role/role_view.html', locals())

def tenant_role_update(request):
    page_title = "Estadisticas de seguimiento"
    return render_to_response('recruitmen/tenant/role/role_update.html', locals())

def tenant_role_delete(request):
    page_title = "Borrar Uusuario"
    return render_to_response('recruitmen/tenant/role/role_delete.html', locals())

'''
########################################################################
'''

'''
Role
########################################################################
'''
def tenant_preference_list(request):
    page_title = "Estadisticas de seguimiento"
    return render_to_response('recruitmen/tenant/preference/preference_list.html', locals())

def tenant_preference_new(request):
    page_title = "Estadisticas de seguimiento"
    return render_to_response('recruitmen/tenant/preference/preference_new.html', locals())

def tenant_preference_view(request):
    page_title = "Estadisticas de seguimiento"
    return render_to_response('recruitmen/tenant/preference/preference_view.html', locals())

def tenant_preference_update(request):
    page_title = "Estadisticas de seguimiento"
    return render_to_response('recruitmen/tenant/preference/preference_update.html', locals())

def tenant_preference_delete(request):
    page_title = "Borrar Uusuario"
    return render_to_response('recruitmen/tenant/preference/preference_delete.html', locals())

'''
########################################################################
'''

'''
########################################################################
PAGINAS UTILIZADAS EN EL PROCESO DE SEGUIMIENTO
'''
def recruitment_process_update(request):
    page_title = "Hoja de Vida"
    return render_to_response('recruitmen/prospect.html', locals())
'''
########################################################################
'''

'''
########################################################################
PROSPECT PAGES
'''
def prospect_list(request):
    page_title = "Hoja de Vida del Prospecto"
    prospect_list = ProfessionalProfile.objects.order_by('candidate_number')
    context = {'prospect_list': prospect_list}
    return render(request,URL_PROSPECT_LIST, context)

def prospect_new(request):
    PositionList = Position.objects.order_by('name')
    WorkAreaList = WorkArea.objects.order_by('name')
    CustomerCompanyList=CustomerCompany.objects.order_by('comercial_name')
    KnowledgeList=Knowledge.objects.order_by('name')
    DegreeList=Degree.objects.order_by('name')
    SchoolList=School.objects.order_by('name')
    AbilityList=Ability.objects.order_by('name')
    vm_pooling=0
    message=""
    page_title = "Nueva de la Hoja de Vida"
    if request.method == "POST":
        name = request.POST.get("name")
        first_name=request.POST.get("first_name")
        second_name = request.POST.get("second_name")
        summary = request.POST.get("summary")
        profile_company_contractor=request.POST.get("profile_company_contractor")
        search_start_date=request.POST.get("search_start_date")
        commitment_date=request.POST.get("commitment_date")
        position=request.POST.get("position")
        work_area=request.POST.get("work_area")
        work_start_date=request.POST.get("work_start_date")
        work_end_date=request.POST.get("work_end_date")
        work_position=request.POST.get("work_position")
        work_area2=request.POST.get("work_area2")
        position_salary=request.POST.get("position_salary")
        position_salary_total=request.POST.get("position_salary_total")
        possible_degree=request.POST.get("possible_degree")
        college=request.POST.get("college")
        start_date=request.POST.get("start_date")
        end_date=request.POST.get("end_date")
        birthdate=request.POST.get("birthdate")
        civil_status=request.POST.get("civil_status")
        number_of_children=request.POST.get("number_of_children")
        number_of_dependents=request.POST.get("number_of_dependents")
        personal_home_phone=request.POST.get("personal_home_phone")
        personal_cellphone=request.POST.get("personal_cellphone")
        personal_email=request.POST.get("personal_email")
        company_emal=request.POST.get("company_emal")
        profP = ProfessionalProfile()
        profP.candidate_number="001"
        pers=Person()
        pers.name=name
        pers.first_name=first_name
        pers.second_name=second_name
        pers.birthdate=birthdate
        pers.civil_status=civil_status
        profP.person=pers
        profP.summary=summary
        profP.number_of_children=number_of_children
        profP.number_of_dependents=number_of_dependents
        profP.personal_home_phone=personal_home_phone
        profP.personal_cellphone=personal_cellphone
        profP.personal_email=personal_email
        profExp=ProfessionalExperience()
        profExp.code="001"
        profExp.since=work_start_date
        profExp.till=work_end_date
        profExp.position=work_position
        profExp.I_work_here_now=True
        profExp.description="ABC"
        profExp.profile=profP
        pers.save()
        profP.save()
        profExp.save()
    else:
        print("Mostrar formulario vacio: ")
        message=""
        context = {'page_title': page_title,
                   'vm_pooling': vm_pooling,
                   'message': message,
                   'PositionList': PositionList,
                   'WorkAreaList': WorkAreaList,
                   'CustomerCompanyList':CustomerCompanyList,
                   'KnowledgeList':KnowledgeList,
                   'DegreeList':DegreeList,
                   'SchoolList':SchoolList,
                   'AbilityList':AbilityList}
        return render(request, URL_PROSPECT_NEW, context)

def prospect_view(request):
    page_title = "Dealles Hoja de Vida"
    return render_to_response('recruitmen/prospect/prospect_view.html', locals())

def prospect_update(request,prospect_id):
    #objProspect = ProfessionalProfile.objects.get(pk=prospect_id)
    PositionList = Position.objects.order_by('name')
    WorkAreaList = WorkArea.objects.order_by('name')
    CustomerCompanyList=CustomerCompany.objects.order_by('comercial_name')
    KnowledgeList=Knowledge.objects.order_by('name')
    DegreeList=Degree.objects.order_by('name')
    SchoolList=School.objects.order_by('name')
    AbilityList=Ability.objects.order_by('name')
    vm_pooling=0
    message=""
    page_title = "Nueva de la Hoja de Vida"
    if request.method == "POST":
        name = request.POST.get("name")
        first_name=request.POST.get("first_name")
        second_name = request.POST.get("second_name")
        summary = request.POST.get("summary")
        search_start_date=request.POST.get("search_start_date")
        commitment_date=request.POST.get("commitment_date")
        position=request.POST.get("position")
        work_area=request.POST.get("work_area")
        work_start_date=request.POST.get("work_start_date")
        work_end_date=request.POST.get("work_end_date")
        work_position=request.POST.get("work_position")
        work_area2=request.POST.get("work_area2")
        position_salary=request.POST.get("position_salary")
        position_salary_total=request.POST.get("position_salary_total")
        possible_degree=request.POST.get("possible_degree")
        college=request.POST.get("college")
        start_date=request.POST.get("start_date")
        end_date=request.POST.get("end_date")
        birthdate=request.POST.get("birthdate")
        civil_status=request.POST.get("civil_status")
        number_of_children=request.POST.get("number_of_children")
        number_of_dependents=request.POST.get("number_of_dependents")
        personal_home_phone=request.POST.get("personal_home_phone")
        personal_cellphone=request.POST.get("personal_cellphone")
        personal_email=request.POST.get("personal_email")
        company_emal=request.POST.get("company_emal")
        profP = ProfessionalProfile()
        profP.candidate_number="001"
        pers=Person()
        pers.name=name
        pers.first_name=first_name
        pers.second_name=second_name
        pers.birthdate=birthdate
        pers.civil_status=civil_status
        profP.person=pers
        profP.summary=summary
        profP.number_of_children=number_of_children
        profP.number_of_dependents=number_of_dependents
        profP.personal_home_phone=personal_home_phone
        profP.personal_cellphone=personal_cellphone
        profP.personal_email=personal_email
        profExp=ProfessionalExperience()
        profExp.code="001"
        profExp.since=work_start_date
        profExp.till=work_end_date
        profExp.position=work_position
        profExp.I_work_here_now=True
        profExp.description="ABC"
        profExp.profile=profP
        pers.save()
        profP.save()
        profExp.save()
    else:
        print("Mostrar formulario vacio: ")
        message=""
        context = {'page_title': page_title,
                   'vm_pooling': vm_pooling,
                   'message': message,
                   'PositionList': PositionList,
                   'WorkAreaList': WorkAreaList,
                   'CustomerCompanyList':CustomerCompanyList,
                   'KnowledgeList':KnowledgeList,
                   'DegreeList':DegreeList,
                   'SchoolList':SchoolList,
                   'AbilityList':AbilityList}
        return render(request, URL_PROSPECT_UPDATE, context)

def prospect_delete(request):
    page_title = "Borrar de Hoja de Vida"
    return render_to_response('recruitmen/prospect/prospect_delete.html', locals())
'''
########################################################################
'''


def menu(request):
    return render(request, 'recruitmen/menu.html')

def base(request):
    current_date = datetime.datetime.now()
    return render_to_response('library/base.html', locals())
    #return render(request, 'library/base.html')
