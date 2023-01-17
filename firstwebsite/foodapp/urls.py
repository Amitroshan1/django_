from foodapp import views
from django.urls import path

app_name='foodapp'
urlpatterns = [
    path('',views.Indexclassview.as_view(), name= 'index'),
    path('<int:pk>/',views.fooddetails.as_view(),name='detail'),
    path('add',views.createitem.as_view(),name='create_item'),
    path('update/<int:id>/',views.update_item,name='update_item'),
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
]
