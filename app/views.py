from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from . models import Product
from .serializers import ProductSerializer


# Create your views here.
# Use function-based views (rather than class-based views)


def index(request):
    all_products = Product.objects.all()
    context = {'all_products': all_products}
    return render(request, 'app/index.html', context)


class ProductAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



#
#
# # this uses class based views, so i need to think whether i want to change this or not.....
# class ProductAPI(APIView):
#
#     def get(self, request):
#         all_products = Product.objects.all()
#         serlializer = ProductSerializer(all_products, many=True)
#         return Response(serlializer.data)
#
#     def post(self):
#         pass
#
#
