from django.conf.urls import url

from . import views

app_name = 'recruitmen'
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^index/', views.index, name='index'),
    #Requisition url
    url(r'^requisition/list/$', views.requisition_list, name='requisition_list'),
    url(r'^requisition/new/$', views.requisition_new, name='requisition_new'),
    url(r'^requisition/view/$', views.requisition_view, name='requisition_view'),
    url(r'^(?P<requisition_id>[0-9]+)/requisition/update/$', views.requisition_update, name='requisition_update'),
    url(r'^(?P<requisition_id>[0-9]+)/requisition/cancel/$', views.requisition_cancel, name='requisition_cancel'),
    url(r'^(?P<requisition_id>[0-9]+)/requisition/timeline/$', views.requisition_timeline, name='requisition_timeline'),
    #Prospect url
    url(r'^prospect/list/$', views.prospect_list, name='prospect'),
    url(r'^prospect/new/$', views.prospect_new, name='prospect'),
    url(r'^prospect/view/$', views.prospect_view, name='prospect'),
    url(r'^(?P<prospect_id>[0-9]+)/prospect/update/$', views.prospect_update, name='prospect_update'),
    url(r'^(?P<prospect_id>[0-9]+)/prospect/delete/$', views.prospect_delete, name='prospect_delete'),
    # Statistics
    url(r'^statistics/timeline/$', views.statistics_timeline, name='statistics_timeline'),
    url(r'^statistics/requisition/$', views.statistics_requisition, name='statistics_requisition'),
    url(r'^statistics/prospect/$', views.statistics_prospect, name='statistics_prospect'),
    # Administration User
    url(r'^administration/user/list/$', views.tenant_user_list, name='user_list'),
    url(r'^administration/user/new/$', views.tenant_user_new, name='user_new'),
    url(r'^administration/user/view/$', views.tenant_user_view, name='user_view'),
    url(r'^administration/user/update/$', views.tenant_user_update, name='user_update'),
    url(r'^administration/user/delete/$', views.tenant_user_delete, name='user_delete'),
    # Administration Role
    url(r'^administration/role/list/$', views.tenant_role_list, name='role_list'),
    url(r'^administration/role/new/$', views.tenant_role_new, name='role_new'),
    url(r'^administration/role/view/$', views.tenant_role_view, name='role_view'),
    url(r'^administration/role/update/$', views.tenant_role_update, name='role_update'),
    url(r'^administration/role/delete/$', views.tenant_role_delete, name='role_delete'),
    # Administration Preference
    url(r'^administration/preference/list/$', views.tenant_preference_list, name='preference_list'),
    url(r'^administration/preference/new/$', views.tenant_preference_new, name='preference_new'),
    url(r'^administration/preference/view/$', views.tenant_preference_view, name='preference_view'),
    url(r'^administration/preference/update/$', views.tenant_preference_update, name='preference_update'),
    url(r'^administration/preference/delete/$', views.tenant_preference_delete, name='preference_delete'),
    # Administration Role
    url(r'^menu/', views.menu, name='menu'),
    url(r'^base/', views.base, name='base'),
]
