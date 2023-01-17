from django.shortcuts import render,redirect
from foodapp.models import Item
from django.http import HttpResponse
from django.template import loader
from foodapp.forms import Itemform
from django.views.generic import ListView,DetailView,CreateView

# Create your views here.
def index(request):
    Item_list=Item.objects.all()
    context={
        'Item_list':Item_list,
    }
    return render(request,'index.html',context)


# in place of above index function we can create a class
class Indexclassview(ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'Item_list'
    

def detail(request,Item_id):
    item=Item.objects.get(pk=Item_id) # for class pass pk in urls.py
    context ={
       'item':item,
    }
    return render(request,'detail.html',context)

    
# for details we can use class based details view

class fooddetails(DetailView):
    model = Item
    template_name = 'detail.html'


def create_item(request):
    form = Itemform(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('foodapp:index')
    return render(request,'form.html',{'form':form})

# class view for createitem

class createitem(CreateView):
    model= Item
    fields= ['item_name','item_desc','item_price','item_image']
    template_name = 'form.html'
    
    
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        
        return super().form_valid(form)
    
    
def update_item(request,id):
    item = Item.objects.get(id=id)
    form = Itemform(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('foodapp:index')
    return render(request,'form.html',{'form':form,'item':item})

def delete_item(request,id):
    item = Item.objects.get(id=id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('foodapp:index')
    
    return render(request,'delete.html',{'item':item})
    
    
        