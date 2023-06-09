from django.urls import path
from django.views.generic import TemplateView
from cbv.models import Post

appname = 'website'

urlpatterns = [
    path('ex1',TemplateView.as_view(template_name='ex1.html',extra_content={'title':'custom Title'})),
]
