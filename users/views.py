from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import TemplateView, View
from categories.models import Category, SubCategory

# Create your views here.
class Index(View):
    
    def get(self, request):
        category_objs = Category.objects.all()
        context = {'category_objs':category_objs}
        return render(request, 'users/index.html',context)

class LoginView(View):

	def get(self, request):
		return render(request, 'users/login_view.html',{})

	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request,user)
			return redirect('users:index')
		else:
			return redirect('users:index')

class LogoutView(View):
	def get(self,request):
		logout(request)
		return redirect('users:index')
	
		
class Register(View):
		
		def get(self, request):
			return render(request, 'users/register.html',{})	

		def post(self,request):
			fname = request.POST.get('fname')
			lname = request.POST.get('lname')
			username = request.POST.get('username')
			password = request.POST.get('password')	
			email = request.POST.get('email')
			user = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email)
			user.set_password(password)
			user.save()
			return redirect('users:index')

