# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
from django.utils.encoding import python_2_unicode_compatible

''' ######################################################################### '''

''' ***
Tabla de Paises 
*** '''
@python_2_unicode_compatible   
class Country(models.Model):
    iso_code  = models.CharField(max_length=100) #Code of the customer profile
    country_name = models.CharField(max_length=100) #Code of the customer profile
    country_description = models.CharField(max_length=100) #Code of the customer profile
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.iso_code

@python_2_unicode_compatible   
class State(models.Model):
    iso_code  = models.CharField(max_length=100) #Code of the customer profile
    state_name = models.CharField(max_length=100) #Code of the customer profile
    state_description = models.CharField(max_length=100) #Code of the customer profile
    country = models.ForeignKey(Country) # Pais al que pertenece el estado
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.iso_code

''' ***
Tabla de Municipios 
*** '''
@python_2_unicode_compatible   
class Municipality(models.Model):
    iso_code  = models.CharField(max_length=100) #Code of the customer profile
    name = models.CharField(max_length=100) #Code of the customer profile
    description = models.CharField(max_length=100) #Code of the customer profile
    state = models.ForeignKey(State) #Codigo del municipio al que ertenece la direccion
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name

''' ***
Tabla de Ciudades 
*** '''
@python_2_unicode_compatible   
class City(models.Model):
    iso_code  = models.CharField(max_length=100) #Code of the customer profile
    city_name = models.CharField(max_length=100) #Code of the customer profile
    city_description = models.CharField(max_length=100) #Code of the customer profile
    state = models.ForeignKey(State) #Codigo del municipio al que ertenece la direccion
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.tenant_name

''' ***
Tabla de Colonias, podria ser distrito 
*** '''
@python_2_unicode_compatible   
class PostalCode(models.Model):
    postal_code  = models.CharField(max_length=50) #Code of the customer profile
    state = models.ForeignKey(State) # Estado al que pertenece el codigo postal
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.district_name 
    
''' *******************************************************************************
@attention: tulehr_district
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: 
@license: 
@summary: Tabla que almacena los distritos o colonias de una localidad
************************************************************************************ '''
@python_2_unicode_compatible   
class District(models.Model):
    district_code  = models.CharField(max_length=50) #Code of the customer profile
    district_name = models.CharField(max_length=100) #Code of the customer profile
    district_description = models.CharField(max_length=100) #Code of the customer profile
    municipality = models.ForeignKey(Municipality) # Municipio o delegacion al que pertenece la colonia
    postal_code = models.ForeignKey(PostalCode) # Codigo postal
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.district_name 
''' ******************************************************************************* '''
   
''' ############################################################################### '''


''' ##################### MODELO MULTITENANT PARA EL SISTEMA ############### '''

''' *******************************************************************************
@attention: tulehr_TENANT
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: 
@license: 
@summary: Tabla Multitenant, en esta tabla se almacenan los tenant de un cliente, cada tabla del sistema tiene un codigo de tenant y 
    este se usa para identificar el cliente que creo el tenant.
************************************************************************************ '''
@python_2_unicode_compatible   
class Tenant(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date=models.DateTimeField('Insert Date')
    update_date=models.DateTimeField('Update Date')
    delete_date=models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name
''' ******************************************************************************* ''' 

''' *******************************************************************************
@attention: tulehr_USER
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: 
@license: 
@summary: Entidad de los usuarios del tenant del cliente
************************************************************************************ '''
@python_2_unicode_compatible   
class User(models.Model):
    number = models.CharField(max_length=10) # Numero de usuario creado, es autoincremental 
    name = models.EmailField(max_length=254, blank=False) # Nombre del usuario, se recomienda que sea el correo electronico
    password = models.CharField(max_length=30) # Password del usuario
    last_connection_date = models.DateTimeField('Last Connection Date')
    last_connection_ip = models.CharField(max_length=15)
    connection_country_code = models.CharField(max_length=5)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name
''' ******************************************************************************* '''
   
''' *******************************************************************************
@attention: tulehr_ROLE
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com
@copyright: 
@license: 
@summary: Entidad de los usuarios del sistema
************************************************************************************ '''
@python_2_unicode_compatible   
class Role(models.Model): 
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name
''' ******************************************************************************* '''

'''
Tipo de perfil del cliente, aqui podemos tener las siguientes opciones
Persona Fisica
Persona Moral
'''
@python_2_unicode_compatible   
class CustomerProfileType(models.Model):
    code = models.CharField(max_length=100) #Code of the customer profile
    type_name = models.CharField(max_length=200)
    type_description = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.code
    
@python_2_unicode_compatible   
class CustomerProfile(models.Model):
    code = models.CharField(max_length=100) #Code of the customer profile
    customer_name = models.CharField(max_length=200) # Nombre Solo en caso de personas fisicas
    customer_first_name = models.CharField(max_length=200) # Apellido Paterno Solo en caso de personas fisicas
    customer_second_name = models.CharField(max_length=200) # Apellido Materno Solo en caso de personas fisicas
    legal_name = models.CharField(max_length=500) # Razon social del cliente
    tax_id = models.CharField(max_length=15) # RFC del cliente
    customer_email = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=10)
    customer_second_phone = models.CharField(max_length=10)
    customer_cellphone = models.CharField(max_length=10)
    customer_second_cellphone = models.CharField(max_length=10)
    customer_page = models.CharField(max_length=300)
    customer_facebook = models.CharField(max_length=300)
    customer_twitter = models.CharField(max_length=300)
    customer_blog = models.CharField(max_length=300)
    customer_linkedin = models.CharField(max_length=300)
    customer_contact_email = models.CharField(max_length=50)
    customer_contact_phone = models.CharField(max_length=10)
    customer_contact_second_phone = models.CharField(max_length=10)
    customer_contact_cellphone = models.CharField(max_length=10)
    customer_contact_second_cellphone = models.CharField(max_length=10)
    customer_contact_page = models.CharField(max_length=300)
    customer_contact_facebook = models.CharField(max_length=300)
    customer_contact_twitter = models.CharField(max_length=300)
    customer_contact_blog = models.CharField(max_length=300)
    customer_contact_linkedin = models.CharField(max_length=300)
    user = models.ForeignKey(User)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.code
    
@python_2_unicode_compatible   
class PaymentProfile(models.Model):
    code = models.CharField(max_length=100) #Code of the customer profile
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.tenant_name

@python_2_unicode_compatible   
class BillingProfile(models.Model):
    code = models.CharField(max_length=100) #Code of the customer profile
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.tenant_name

@python_2_unicode_compatible   
class ServiceProfile(models.Model):
    code = models.CharField(max_length=100) #Code of the customer profile
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.tenant_name

''' ######################################################################### '''
   
   
   


''' 
************************************************************************************
* Autor: Arturo Vargas
* correo: juanarturovargas@gmail.com
* Derechos de Autor: 
* 2017
* Tabla de tipo de domicilios 
* Puede ser :
* Domicilio del Corporativo
* Domicilio de Sucursal
* Domicilio Fiscal
* Domicilio de Entrega o Recepcion
* Domicilio de Cobranza
* Domicilio Personal
* Domicilio de Servicio
***************************************************************************************** '''
@python_2_unicode_compatible   
class AddressType(models.Model):
    address_type_code  = models.CharField(max_length=50) #Code of the customer profile
    address_type_name = models.CharField(max_length=100) #Code of the customer profile
    address_type_description = models.CharField(max_length=100) #Code of the customer profile
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.tenant_name 

''' ***
Tabla de direcciones 
*** '''
@python_2_unicode_compatible   
class Address(models.Model):
    street_name  = models.CharField(max_length=100) # Nombre de la calle
    internal_number = models.CharField(max_length=100) # Numero de exterior
    external_number = models.CharField(max_length=100) # Numero de interior
    between_street1 = models.CharField(max_length=100) # La primera calle entre las que se encuentra su domicilio​
    between_street2 = models.CharField(max_length=100) # La segunda calle entre la que se encuentra su domicilio. Si su domicilio está en esquina, coloque la siguiente calle más cercana que permita identificar rápidamente su localización.​
    aditional_reference  = models.CharField(max_length=100) # Capture un punto relevante cercano a su domicilio fiscal. Puede ser el que siempre proporciona a sus conocidos para que puedan ubicar rápidamente este domicilio.​
    municipality = models.ForeignKey(Municipality) #Municipio del estado
    city  = models.ForeignKey(City) #Ciudad
    postal_code = models.ForeignKey(PostalCode) # Codigo postal
    addressType = models.ForeignKey(AddressType) #Tipo de direccion
    langage_code = models.CharField(max_length=10,default="es-MX") #Lenguaje del pais
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.tenant_name

''' ######################################################################### '''


# Entidades del modulo de administración de personal
@python_2_unicode_compatible   
class Position(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.description

# Entidades del modulo de administración de personal
@python_2_unicode_compatible   
class CivilStatus(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.description
    

@python_2_unicode_compatible   
class CustomerCompany(models.Model):
    code = models.CharField(max_length=200)
    comercial_name = models.CharField(max_length=200)
    legal_name = models.CharField(max_length=200)
    tax_code = models.CharField(max_length=200)#código de impuestos
    description = models.CharField(max_length=400)
    logo = models.ImageField(upload_to='company')
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.comercial_name

@python_2_unicode_compatible   
class CostCenter(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name

@python_2_unicode_compatible   
class PhysicalLocation(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name
    
@python_2_unicode_compatible   
class WorkArea(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.description
    
''' ############## CONFIGURACION DEL PERFIL EDUCATIVO DEL CANDIDATO ###############'''

''' *********************************************
Esta entidad es generica, no se va a particionar por tenant.
************************************************* '''
@python_2_unicode_compatible   
class School(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name

''' *********************************************
Campo de estudio.
Esta tabla almacena el campo de estudio o especialidad cursada durante la carrera,
por ejemplo: 
Esta entidad es generica, no se va a particionar por tenant.
************************************************* '''
@python_2_unicode_compatible   
class FieldStudy(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name
    
@python_2_unicode_compatible   
class EducationLevel(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name

# Bachelor's degree
# Licenciatura
@python_2_unicode_compatible   
class Degree(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    description = models.ManyToManyField(EducationLevel)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name

# Language
# Idioma
@python_2_unicode_compatible   
class Language(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name

@python_2_unicode_compatible   
class LanguageLevel(models.Model):
    nivel = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name

@python_2_unicode_compatible   
class LanguageLevelLanguage(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language)
    language_level = models.ForeignKey(LanguageLevel)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name
''' ############################################################################'''

''' ############################ CONFIGURACION DE LA EXPERIENCIA DEL EMPLEADO ####################################'''
@python_2_unicode_compatible   
class IndustryExperience(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name

@python_2_unicode_compatible   
class PreferredGender(models.Model):
    name = models.CharField(max_length=50)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name

@python_2_unicode_compatible   
class WorkingHours(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    tenant_code = models.CharField(max_length=100, default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name    

@python_2_unicode_compatible   
class Knowledge(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name

@python_2_unicode_compatible   
class Ability(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name

@python_2_unicode_compatible   
class AgeRange(models.Model):
    name = models.CharField(max_length=50)
    edad_inicial = models.CharField(max_length=10)
    edad_final = models.CharField(max_length=50)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name

# Tipo fuente de contacto
@python_2_unicode_compatible   
class TypeSourceContact(models.Model):    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name
    
# Fuente del contacto, ejemplo Facebook, LinkedIn, Computrabajo
@python_2_unicode_compatible   
class ContactSource(models.Model):    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    type_source_contact = models.ForeignKey(TypeSourceContact)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.name
 
@python_2_unicode_compatible   
class Person(models.Model):
    name = models.CharField(max_length=200)#Nombre
    first_name = models.CharField(max_length=200)#Nombre de pila
    second_name = models.CharField(max_length=200)#Segundo nombre  
    birthdate= models.DateTimeField('Birthdate')#Fecha de nacimiento 
    civil_status=  models.BooleanField()#Estado civil
    def __str__(self): # __unicode__ on Python 2
        return self.name+' '+self.first_name

@python_2_unicode_compatible   
class Employee(models.Model):
    employee_number = models.CharField(max_length=200)#Número de empleado
    person = models.ForeignKey(Person)#Persona
    company_phone = models.CharField(max_length=10)#Teléfono de la empresa
    company_extencion_phone = models.CharField(max_length=10)#Teléfono extencion de la empresa
    company_emal = models.CharField(max_length=50)#Email de la empresa
    personal_email = models.CharField(max_length=50)#Email personal
    personal_home_phone = models.CharField(max_length=10)# Teléfono personal de la casa
    personal_second_phone = models.CharField(max_length=10)#Segundo teléfono personal
    personal_cellphone = models.CharField(max_length=10)#Numero de celular personal
    personal_second_cellphone = models.CharField(max_length=10)# Segundo móvil personal
    personal_page = models.CharField(max_length=300)#Página personal
    personal_blog = models.CharField(max_length=300)#Blog personal
    personal_linkedin_profile = models.CharField(max_length=300)#Perfil linkedin personal
    personal_computrabajo_profile = models.CharField(max_length=300)#Perfil computrabajo personal
    personal_occ_profile = models.CharField(max_length=300)#Perfil occ personal
    personal_bumeran_profile = models.CharField(max_length=300)#Perfil bumeran personal
    personal_cornerjob_profile = models.CharField(max_length=300)#Perfil cornerjob personal
    position = models.ForeignKey(Position)#Puesto
    tenant_code = models.CharField(max_length=100,default="000")#Código de inquilino
    country_code = models.CharField(max_length=5,default="MX")#Código de país
    langage_code = models.CharField(max_length=10,default="es-MX")#Código de idioma
    time_zone_code = models.CharField(max_length=5,default="UTC-6")#Código de zona horaria
    insert_date = models.DateTimeField('Insert Date')#Fecha de inserción
    update_date = models.DateTimeField('Update Date',null=True,blank=True)#Fecha de actualización
    delete_date = models.DateTimeField('Delete Date',null=True,blank=True)#Fecha de eliminación
    logical_status = models.CharField(max_length=10,default="INSERT")#Estado lógico
    is_historical = models.CharField(max_length=3,default="NO")#Es histórico
    def __str__(self): # __unicode__ on Python 2
        return self.employee_number

@python_2_unicode_compatible   
class VacancyProfile(models.Model): #Perfil de la vacante
    profile_code = models.CharField(max_length=50) # Código de perfil solicitado
    profile_name = models.CharField(max_length=50) # Nombre del perfil solicitado
    requested_position = models.ForeignKey(Position) # Posición solicitada para alguna área
    requested_amount = models.CharField(max_length=5) # Cantidad de posición solicitada
    education_level = models.ManyToManyField(EducationLevel) #Nivel de formación del perfil solicitado
    possible_degree = models.ManyToManyField(Degree) # Posible licenciatura
    language_level = models.ManyToManyField(LanguageLevelLanguage) # Nivel del idioma
    description_experience = models.CharField(max_length=2000)#Descripción de su experiencia
    years_experience = models.CharField(max_length=3)##Años de experiencia
    industry_experience = models.ForeignKey(IndustryExperience)#Experiencia industrial
    knowledge = models.ManyToManyField(Knowledge,related_name='knowledge_base') # Conocimiento del candidato
    ability = models.ManyToManyField(Ability)#Habilidad
    prioritize_knowledge = models.ManyToManyField(Knowledge,related_name='conocimiento_prioriza')#Priorizar el conocimiento
    age_range = models.ForeignKey(AgeRange)#rango de edad
    tenant_code = models.CharField(max_length=100,default="000")#Código de inquilino
    country_code = models.CharField(max_length=5,default="MX")#Código de país
    langage_code = models.CharField(max_length=10,default="es-MX")#Código de idioma
    time_zone_code = models.CharField(max_length=5,default="UTC-6")#Código de zona horaria
    insert_date = models.DateTimeField('Insert Date')#Fecha de inserción
    update_date = models.DateTimeField('Update Date', null=True,blank=True)#Fecha de actualización
    delete_date = models.DateTimeField('Delete Date', null=True,blank=True)#Fecha de eliminación
    logical_status = models.CharField(max_length=10,default="INSERT")#Estado lógico
    is_historical = models.CharField(max_length=3,default="NO")#Es histórico
    def __str__(self): # __unicode__ on Python 2
        return self.profile_name

@python_2_unicode_compatible   
class EmployeeRequisition(models.Model):
    employee_requisition_number = models.CharField(max_length=50)#Número de solicitud de empleado
    name = models.CharField(max_length=50)#Nombre
    requisition_requested_by = models.ForeignKey(Employee,related_name='employee_requisition_requested_by') # Requisición solicitada por
    company_destination = models.ForeignKey(CustomerCompany,related_name='company_destination')#Empresa de destino
    work_area = models.ForeignKey(WorkArea,related_name='work_area') #Área de trabajo 
    cost_center = models.ForeignKey(CostCenter)#Centro de costos
    physical_location = models.ForeignKey(PhysicalLocation)#Localizacion fisica
    immediate_boss = models.ForeignKey(Employee,related_name='immediate_boss')#Jefe inmediato
    immediate_boss_position = models.ForeignKey(Position,related_name='immediate_boss_position') #Puesto del Jefe inmediato
    immediate_boss_direccion = models.ForeignKey(WorkArea,related_name='immediate_boss_direccion') #Direccion Jefe inmediato 
    start_date = models.DateTimeField('Start Date') #Fecha en la que el empleado iniciara labores
    vacancy_position_profile = models.ForeignKey(VacancyProfile)#Perfil de posición vacante
    position_salary = models.CharField(max_length=10)#Sueldo del puesto
    position_salary_total =  models.BooleanField() # Sueldo bruto del puesto
    profile_company_contractor = models.ForeignKey(CustomerCompany,related_name='profile_company_contractor') # Empresa que contrata el perfil
    working_hours_profile =  models.ForeignKey(WorkingHours) # Horario de trabajo
    preferred_gender =  models.ForeignKey(PreferredGender) # Genero preferido
    position_work_area = models.ForeignKey(WorkArea,related_name='position_work_area') #Area laboral en donde estara el perfil buscado
    employee_internal_interviewer = models.ForeignKey(Employee,related_name='employee_internal_interviewer') # Empleado que va a entrevistar al perfil requerido
    position_to_search = models.ForeignKey(Position,related_name='position_to_search') # Posicion buscada
    #Cliente
    location = models.ForeignKey(WorkArea,related_name='work_area_location')#Ubicación
    location_phone_internal = models.CharField(max_length=10)#Teléfono interno de la ubicación
    employee_tracing = models.ForeignKey(Employee,related_name='employee_tracing') #Empleado interno que dara seguimiento
    #Gerente CAT
    manager_tracing = models.ForeignKey(Employee,related_name='manager_tracing') #Gerente que dara seguimiento
    search_start_date = models.DateTimeField('Search Start Date')#Fecha de inicio de la búsqueda
    commitment_date = models.DateTimeField('Fecha de compromiso')#Fecha de compromiso
    #Cliente HR
    hr_process_tracing = models.ForeignKey(Employee,related_name='hr_process_tracing') # Empleado responsable de darle seguimiento
    hr_contractor_area = models.ForeignKey(WorkArea,related_name='hr_contractor_area') # Area de RH responsable de contratar
    tenant_code = models.CharField(max_length=100,default="000")#Código de inquilino
    country_code = models.CharField(max_length=5,default="MX")#Código de país
    langage_code = models.CharField(max_length=10,default="es-MX")#Código de idioma
    time_zone_code = models.CharField(max_length=5,default="UTC-6")#Código de zona horaria
    insert_date = models.DateTimeField('Insert Date')#Fecha de inserción
    update_date = models.DateTimeField('Update Date', null=True,blank=True)#Fecha de actualización
    delete_date = models.DateTimeField('Delete Date', null=True,blank=True)#Fecha de eliminación
    logical_status = models.CharField(max_length=10,default="INSERT")#Estado lógico
    is_historical = models.CharField(max_length=3,default="NO")#Es histórico
    def __str__(self): # __unicode__ on Python 2
        return self.employee_requisition_number


# *********************ADMINISTRACION DE CANDIDATOS****************************
@python_2_unicode_compatible   
class CandidateNote(models.Model):    
    note_name = models.CharField(max_length=200)
    note_description = models.CharField(max_length=200)
    note_observation = models.CharField(max_length=200)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.note_name

@python_2_unicode_compatible   
class CandidateStatus(models.Model):    
    status = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    notas = models.CharField(max_length=200)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.status


'''
    Entidad que representa el perfil de una compañia, este puede ser usado como extencion de otros tipos de compañias
    como pudiera ser un cliente o un proveedor.
'''
@python_2_unicode_compatible   
class CompanyProfile(models.Model):
    code = models.CharField(max_length=200)
    comercial_name = models.CharField(max_length=200)
    legal_name = models.CharField(max_length=200)
    tax_code = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    logo = models.ImageField(upload_to='company')
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.code
   
'''
Este perfil debe coincidir con el perfil cargado en linkedin para poderlo importar desde esa red social
El perfil profesional de una persona puede convertirse en un perfil de empleado, para esto se tendria que ligar el perfil 
profesional a una tabla de empleado para poder agregar otras caracteristicas como el numero de empleado
'''
    
@python_2_unicode_compatible   
class ProfessionalProfile(models.Model):    
    candidate_number = models.CharField(max_length=10)
    person = models.ForeignKey(Person)#Persona
    number_of_children=models.CharField(max_length=5) # Cantidad de hijos
    number_of_dependents=models.CharField(max_length=5) # Número de dependientes
    # Datos personales del perfil ####################################################################################
    work_title = models.CharField(max_length=200) # Titulo que ostenta como profesionista. ej. Arquitecto de Software
    college = models.ForeignKey(School) # Universidad donde estudio
    aptitudes = models.ManyToManyField(Ability)# Aptitudes y habilidades
    summary = models.CharField(max_length=2000) # Resumen profesional
    actual_position = models.CharField(max_length=2000) # Puesto Actual
    # Experiencia profesional ########################################################################################
    company_phone = models.CharField(max_length=10) # Telefono del trabajo
    company_extencion_phone = models.CharField(max_length=10) # Extencion del telefono del trabajo
    company_cellphone = models.CharField(max_length=10) # Celular del trabajo
    company_emal = models.CharField(max_length=50) # Email del trabajo
    personal_email = models.CharField(max_length=50) # Email personal 
    personal_home_phone = models.CharField(max_length=15) # Telefono de casa
    personal_second_phone = models.CharField(max_length=15) # Segundo telefono opcional
    personal_cellphone = models.CharField(max_length=15) # Telefono celular personal 
    personal_second_cellphone = models.CharField(max_length=10) # Segundo telefono celular
    personal_page = models.CharField(max_length=300) # Url de la pagina personal
    personal_blog = models.CharField(max_length=300) # Url del blog personal
    personal_linkedin_profile = models.CharField(max_length=300) # Url del perfil de linkedin
    personal_linkedin_linkedin = models.CharField(max_length=300) # Url del perfil de facebook
    personal_linkedin_twitter = models.CharField(max_length=300) # Url del perfil de twitter
    personal_linkedin_instagram = models.CharField(max_length=300) # Url del perfil de instagram
    personal_linkedin_snapchat = models.CharField(max_length=300) # Url del perfil de snapchat
    personal_computrabajo_profile = models.CharField(max_length=300) # Url del perfil personal de computrbajo
    personal_occ_profile = models.CharField(max_length=300)  # Url del perfil personal de occ
    personal_bumeran_profile = models.CharField(max_length=300) # Url del perfil personal de bumeran
    personal_cornerjob_profile = models.CharField(max_length=300) # Url del perfil personal de cornerjob
    requisicion_personal = models.ForeignKey(EmployeeRequisition,null=True,blank=True)# Relacion del Candidato a las ordenes de requisiciones
    contact_source = models.ForeignKey(ContactSource)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.candidate_number

'''
    Entidad de la experiencia profesional.
'''
@python_2_unicode_compatible   
class ProfessionalExperience(models.Model):
    code = models.CharField(max_length=200)
    profile = models.ForeignKey(ProfessionalProfile) #Perfil asociado
    position = models.ForeignKey(Position)#Cargo
    company = models.ForeignKey(CustomerCompany)#Empresa
    location = models.CharField(max_length=200)#Ubicación
    since = models.DateTimeField('Since Date')#De 
    till = models.DateTimeField('Till Date')#A 
    I_work_here_now = models.BooleanField()#Trabajo aquí actualmente
    description = models.CharField(max_length=200)#Descripción
    observation = models.CharField(max_length=200)
    notas = models.CharField(max_length=200)
    tenant_code = models.CharField(max_length=100,default="000")
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.code
      
    
# ********************* TERMINA ADMINISTRACION DE CANDIDATOS****************************


'''
    Una cuenta puede tener varios servicios activos.
    Cada servicio puede ser uno de los siguientes:
        1.- Servicio de Inbound Recruitment
                a.- Publicacion en redes sociales  (/recruitment/social/linkedin)
        2.- Servicios Profile Configuration
                I.- Profile Configuration   (/recruitment/profile/configuration)
        2.- Servicio de Following Recruitment Process
        3.- 100 Number of Recruitment process packeage
        3.- 500 Number of Recruitment process packeage
        3.- 1000 Number of Recruitment process packeage
    
    Estructura
    Service --- 
        Bundle --- 
            Product ---  
'''


class ProductType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.tenant_name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    product_type = models.ForeignKey(ProductType) #
    price = models.FloatField()
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.tenant_name
        
class ProductFeature(models.Model):
    name = models.CharField(max_length=200) # Velocidad de disco duro
    value = models.CharField(max_length=200) # 3000
    type_value = models.CharField(max_length=200) # Revoluciones por minuto
    description = models.CharField(max_length=400)
    product_type = models.ForeignKey(Product) #
    price = models.FloatField()
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.tenant_name

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    product = models.ForeignKey(Product) #Product of Service
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.tenant_name

class Bundle(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    price = models.FloatField()
    service = models.ForeignKey(Service)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.tenant_name

class ProductPriceList(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    price = models.FloatField()
    price_init_date = models.DateTimeField('Price Init Date')
    price_end_date = models.DateTimeField('Price End Date')
    product = models.ForeignKey(Product) #
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.tenant_name

class BundlePriceList(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    price = models.FloatField()
    price_init_date = models.DateTimeField('Price Init Date')
    price_end_date = models.DateTimeField('Price End Date')
    bundle = models.ForeignKey(Bundle) #
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.tenant_name

class PurchaseProduct(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    bundle = models.ForeignKey(Bundle)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.tenant_name
    
class PurchaseBundle(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    bundle = models.ForeignKey(Bundle)
    purchase_product = models.ForeignKey(PurchaseProduct)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.tenant_name   
    
'''******************************************************************************************'''
   
''' *******************************************************************************
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com;
@copyright: www.tulehr.com
@license: MIT
@summary: Tipo de contacto
************************************************************************************ '''
class ContactType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.code
''' ************************************************************************************ '''
   
''' *******************************************************************************
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com; jvargas@kionetworks.com
@copyright: 
@license: MIT
@summary: Tipo de contacto, Principal, Secundario 
************************************************************************************ '''
class Contact(models.Model):
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    contact_type = models.ForeignKey(ContactType)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.code
''' *******************************************************************************'''
   

''' *******************************************************************************
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com; jvargas@kionetworks.com
@copyright: www.tulehr.com
@license: MIT
@summary: Tipo Telefonos del cliente, Empresa, Personal, Empresa, Recados, Familiar, Celular
************************************************************************************ '''
class PhoneType(models.Model):
    type_name = models.CharField(max_length=200)
    type_description = models.CharField(max_length=200)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.code
''' *******************************************************************************'''    
   
   
''' *******************************************************************************
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com; jvargas@kionetworks.com
@copyright: www.tulehr.com S.A. de C.V.
@license: MIT
@summary: Tipo Telefonos del cliente, Empresa, Personal, Empresa, Recados, Familiar
************************************************************************************ '''
class Phone(models.Model):
    phone = models.CharField(max_length=20)
    phone_type = models.ForeignKey(PhoneType)
    contact = models.ForeignKey(Contact)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.code
''' *******************************************************************************'''    


''' *******************************************************************************
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com; jvargas@kionetworks.com
@copyright: www.tulehr.com S.A. de C.V.
@license: MIT
@summary: Tipo Telefonos del cliente, Empresa, Personal, Empresa, Recados, Familiar
************************************************************************************ '''
class EmailType(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.code
''' *******************************************************************************'''


''' *******************************************************************************
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com; jvargas@kionetworks.com
@copyright: www.tulehr.com S.A. de C.V.
@license: MIT
@summary: Email de contacto
************************************************************************************ '''
class Email(models.Model):
    email = models.CharField(max_length=100)
    email_type = models.ForeignKey(EmailType)
    contact = models.ForeignKey(Contact)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.code
''' *******************************************************************************'''


''' *******************************************************************************
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com; jvargas@kionetworks.com
@copyright: www.tulehr.com S.A. de C.V.
@license: MIT
@summary: Entidad tipo de redes sociales
************************************************************************************ '''
class SocialNetworkType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.code
''' ************************************************************************************ '''


''' *******************************************************************************
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com; jvargas@kionetworks.com
@copyright: www.tulehr.com S.A. de C.V.
@license: MIT
@summary: Cuenata de redes sociales
************************************************************************************ '''
class SocialNetwork(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    social_network_type = models.ForeignKey(SocialNetworkType)
    contact = models.ForeignKey(Contact)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.code
''' ************************************************************************************ '''
   

''' *******************************************************************************
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com; jvargas@kionetworks.com
@copyright: www.tulehr.com S.A. de C.V.
@license: MIT
@summary: Tipo de contacto, Principal, Secundario, Emprsarial, Personal, 
************************************************************************************ '''
class ContactInfoType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.code
''' *******************************************************************************'''


''' *******************************************************************************
@author: Arturo Vargas 
@contact: juanarturovargas@gmail.com; jvargas@kionetworks.com
@copyright: www.tulehr.com S.A. de C.V.
@license: MIT
@summary: Tipo de contacto, Principal, Secundario 
************************************************************************************ '''
class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    contact = models.ForeignKey(Contact)
    address = models.ForeignKey(Address)
    country_code = models.CharField(max_length=5,default="MX")
    langage_code = models.CharField(max_length=10,default="es-MX")
    time_zone_code = models.CharField(max_length=5,default="UTC-6")
    insert_date = models.DateTimeField('Insert Date')
    update_date = models.DateTimeField('Update Date')
    delete_date = models.DateTimeField('Delete Date')
    logical_status = models.CharField(max_length=10,default="INSERT")
    is_historical = models.CharField(max_length=3,default="NO")
    def __str__(self): # __unicode__ on Python 2
        return self.code
''' *******************************************************************************'''


