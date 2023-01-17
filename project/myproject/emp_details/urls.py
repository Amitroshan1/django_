from django.urls import path
from emp_details import views


urlpatterns = [
    path('',views.index,name='index')
]
