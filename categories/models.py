from django.db import models
import datetime
# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=200)
	time_stamp = models.DateTimeField('date published')

	def __str__(self):
		return self.name


class SubCategory(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	time = models.DateTimeField('date published') 

	def __str__(self):
		return self.name


		# from django.db import connection, reset_queries
        # reset_queries()
        # print(len(connection.queries))
        # print(connection.queries)


