from users import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('register/',views.register,name='register'),
]
