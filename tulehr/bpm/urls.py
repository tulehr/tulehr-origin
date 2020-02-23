from django.conf.urls import url

from . import views

app_name = 'bpm'
urlpatterns = [
        #Business Process Management
    url(r'^worklist/list/$', views.bpm_worklist, name='bpm_worklist'),
    url(r'^timeline/view/$', views.bpm_timeline, name='bpm_timeline'),
]
