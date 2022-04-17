from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
	
	path('add_category/', views.AddCategory.as_view(), name='add_category'),
	path('show_category/', views.ShowCategory.as_view(), name='show_category'),
	path('add_sub_category', views.AddSubCategory.as_view(), name='add_sub_category'),
	


]