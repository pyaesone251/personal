from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Service(models.Model):
    title = RichTextField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    note = RichTextField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

class Service1(models.Model):
    image = models.ImageField(upload_to='service1',null=True,blank=True)
    title = RichTextField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    note = RichTextField(null=True,blank=True)
    note1 = RichTextField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

class Blog(models.Model):
    title = RichTextField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

class Blog_Model(models.Model):
    image = models.ImageField(upload_to='blog_model',null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
