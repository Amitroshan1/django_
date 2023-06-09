from django.urls import path
from ecomweb import views

app_name ="ecomweb"

urlpatterns = [
    path('',views.index,name ='index'),
    path("<int:id>/",views.details,name="details")
]
