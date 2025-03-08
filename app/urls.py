from django.urls import path
from app.views import *


urlpatterns = [
    path('fbv_school', fbv_school, name='fbv_school'),
    path('cbv_school', cbv_school.as_view(), name='cbv_school'),
    path('list_schools', list_schools.as_view(), name='list_schools')
]
