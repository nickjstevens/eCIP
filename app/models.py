from django.db import models
from django.contrib import admin

class Product(models.Model):
    product_text = models.CharField(max_length=200)
    product_COD = models.FloatField()

    def __str__(self):
        return self.product_text


class ProductAdmin(admin.ModelAdmin):
    # fields displayed on edit and add pages
    fields = ('product_text', 'product_COD')

    # to display read only fields (like date added) set the readonly options
    # readonly_fields = ('todo_date_added', 'todo_date_modified')

    # this gives a automatic date filtering capability
    # date_hierarchy = 'todo_date_added'

    # this adds fields to the main list page
    list_display = ('product_text', 'product_COD')
