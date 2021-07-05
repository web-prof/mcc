from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', main, name='main'),
    path('log_in/',log_in,name='log_in')

]
