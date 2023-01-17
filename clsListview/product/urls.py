from django.urls import path
from product import views

app_name = "product"
urlpatterns = [
    path('',views.company_name.as_view(),name='list'),
    path('index/',views.template_view.as_view(),name="index"),
    path('<int:pk>/',views.companydetails.as_view(),name="details"),
    path('create/',views.createcompany.as_view(),name = 'create'),
    path('update/<int:pk>/',views.companyupdateview.as_view(),name='update'),
    path('delete/<int:pk>/',views.com_delete.as_view(),name='delete'),
    
]
