from recruitmen.models import EmployeeRequisition

#https://docs.djangoproject.com/en/1.11/topics/db/models/

class RequisitionService(object):
    
    def saveRequisition(self):
        requsitionByCountry = EmployeeRequisition.objects.filter(country_code="MX")
        
        req = EmployeeRequisition(employee_requisition_number="1000")
        req.save()
         
        print requsitionByCountry 
        return True

    print "Hola"
    
    if __name__ == '__main__':
        pass