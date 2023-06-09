from django.urls import path,include
from .views import comapnyvieset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies',comapnyvieset)

urlpatterns = [
    path("",include(router.urls))
]
