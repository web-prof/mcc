from django.urls import path
from .views import *

app_name = 'acc'

urlpatterns = [
  path('delete_operation/',delete_operation,name='delete_operation'),
  path('acc_manager/',acc_manager,name='acc_manager'),
  path('managing_Site_details/<str:name>/',managing_site_detail,name='managing_site_details')
]
