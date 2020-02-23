# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User, Tenant,CustomerProfileType,CustomerProfile,PaymentProfile,BillingProfile,Country,State,Municipality
from .models import City,PostalCode,District,AddressType,Address,Position,CustomerCompany,CostCenter,PhysicalLocation
from .models import WorkArea,School,FieldStudy,EducationLevel,Degree,Language,LanguageLevel,LanguageLevelLanguage
from .models import IndustryExperience,PreferredGender,WorkingHours,Knowledge,Ability,AgeRange,TypeSourceContact
from .models import ContactSource,Employee,VacancyProfile,EmployeeRequisition,CandidateNote,CandidateStatus,CompanyProfile
from .models import ProfessionalExperience,ProfessionalProfile,ServiceProfile,Person,CivilStatus

#BPM
from .models import User, Role


# Register your models here.
#Catalogos
admin.site.register(Tenant)
admin.site.register(PaymentProfile)
admin.site.register(BillingProfile)
admin.site.register(ServiceProfile)
admin.site.register(Position)
admin.site.register(CostCenter)
admin.site.register(PhysicalLocation)
admin.site.register(WorkArea)
admin.site.register(School)
admin.site.register(FieldStudy)
admin.site.register(EducationLevel)
admin.site.register(Degree)
admin.site.register(Language)
admin.site.register(LanguageLevel)
admin.site.register(IndustryExperience)
admin.site.register(WorkingHours)
admin.site.register(Knowledge)
admin.site.register(Ability)
admin.site.register(CivilStatus)
#Tablas de administración
admin.site.register(CustomerCompany)
admin.site.register(Employee)
admin.site.register(PreferredGender)
admin.site.register(VacancyProfile)
admin.site.register(AgeRange)
admin.site.register(LanguageLevelLanguage)

#Business Process Management
admin.site.register(User)
admin.site.register(Role)


