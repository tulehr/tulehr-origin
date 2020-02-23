# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import ProcessStatus, ProcessType, Process, ProcessPool, Activity, ProcessInstance, ActivityInstance, ActivityInstanceStatus, ActivityType, ActivityStatus, ProcessInstanceStatus

admin.site.register(ProcessStatus)
admin.site.register(ProcessType)
admin.site.register(Process)
admin.site.register(ProcessPool)
admin.site.register(ActivityInstanceStatus)
admin.site.register(ActivityType)
admin.site.register(ActivityStatus)
admin.site.register(Activity)
admin.site.register(ActivityInstance)
admin.site.register(ProcessInstanceStatus)
admin.site.register(ProcessInstance)


# Register your models here.
