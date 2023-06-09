from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post
# Create your views here.

class Ex2view(TemplateView):
    '''TemplateResponseMixin
    Provides a mechanism to construct a TemplateResponse, given suitable context'''


    # Attritube:
    
    template_name = "ex2.html"
    #template_engine = tne NAME of a template engine to use for loading the templates
    # response_class = Custom template loading or custom context object instantiation
    #content-type = default Django uses 'text/html'

    ''' get_contxt_data(**kwargs) is a method inherited from contextMIxing'''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.get(id=1)
        context['data'] = "Context Data for Ex2"
        return context