from django.urls import path
from users import views
from django.views.generic import TemplateView, View

app_name = 'users'

urlpatterns = [
	
	path('', views.Index.as_view(), name='index'),
	path('login/', views.LoginView.as_view(), name='login_view'),
	path('register/',views.Register.as_view(), name='register'),
	path('logout/', views.LogoutView.as_view(), name='logout_view'),
	

]