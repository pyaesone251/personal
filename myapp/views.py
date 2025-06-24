from django.shortcuts import render
from .models import *

# Create your views here.

def indexview(request):
    service = Service.objects.all().order_by('id')[:1]
    service1 = Service1.objects.all().order_by('id')[:4]
    blog = Blog.objects.all()
    blog_model = Blog_Model.objects.all().order_by('id')[:3]
    contex = {
       'service':service,
       'service1':service1,
       'blog':blog,
       'blog_model':blog_model,
       
    }
    return render(request,'index.html',contex)
