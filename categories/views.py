from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Category, SubCategory
from django.views import View
import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.



class AddCategory(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            category_objs = Category.objects.all()
            context = {'category_objs':category_objs}
            return render(request, 'categories/add_category.html',context)
        else:
            return redirect('users:login_view')

    def post(self, request):
        
        category_name = request.POST.get('category_name')
        name = Category.objects.create(name=category_name, time_stamp=datetime.datetime.now())
        return redirect('users:index')
        

    
class ShowCategory(View):

    def get(self, request):
        if request.user.is_authenticated:
            category_objs = Category.objects.all()
            context = {'category_objs':category_objs}
            return render(request, 'categories/show_category.html', context)
        else:
            return redirect('users:login_view')



    
class AddSubCategory(View):

    def get(self, request):
        if request.user.is_authenticated:
            category_objs = Category.objects.all()
            context = {'category_objs':category_objs}
            return render(request, 'categories/add_sub_category.html',context)
        else:
            return redirect('users:login_view')



    def post(self, request):
        category = request.POST.get('category_name')
        category_obj = Category.objects.get(name=category)
        sub_category = request.POST.get('sub_category')
        category = SubCategory.objects.create(category=category_obj,name=sub_category,time=datetime.datetime.now())
        return redirect('users:index')       
        

    

