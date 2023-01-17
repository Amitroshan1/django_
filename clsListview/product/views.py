from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView
from product.models import company
from django.urls import reverse_lazy
# Create your views here.

    
    
class template_view(TemplateView):
    template_name = 'index.html'
    
class company_name(ListView):
    context_object_name = 'companies'
    model = company
    
    
class companydetails(DetailView):
    context_object_name="company_details"
    model = company
    template_name = "product/company_detail.html"
    
    
class createcompany(CreateView):
    fields= ('name','ceo','origin')
    model = company
    
    
class companyupdateview(UpdateView):
    fields = ('name','ceo')
    model = company
    
class com_delete(DeleteView):
    model= company
    success_url = reverse_lazy("product:list")