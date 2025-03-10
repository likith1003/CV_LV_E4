from django.urls import path
from app.views import *


urlpatterns = [
    path('fbv_school', fbv_school, name='fbv_school'),
    path('cbv_school', cbv_school.as_view(), name='cbv_school'),
    path('list_schools', list_schools.as_view(), name='list_schools'),
    path('Addstd', Addstd.as_view(), name='Addstd'),
    path('viewschool<pk>', viewschool.as_view(), name='viewschool'),
    path('update_school<pk>', update_school.as_view(), name='update_school'),
    path('delete_school<pk>', delete_school.as_view(), name='delete_school')
]
