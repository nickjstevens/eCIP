from django.contrib import admin

# Register your models here.
from .models import Product, ProductAdmin

admin.site.register(Product, ProductAdmin)


# superuser:
# nickjstevens, nickjstevens@gmail.com, mysuperuserpassword

